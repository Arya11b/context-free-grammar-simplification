import re
# we define 0 as λ
class context_free:
    rules = []
    def __init__(self):
        self.split_grammer()
        self.trim_lambda()
        self.trim_unit()
        self.unify()
        self.trim_useless()
        self.beautify()
    def get_input(self):
        file = open("test.txt","r")
        return file.readlines()
    def split_grammer(self):
        strings = self.get_input()
        for st in strings:
            self.rules.append(" ".join(re.findall("[a-zA-Z0]+", st)))
            print(self.rules[-1])
    def trim_useless(self):
        v=[]
        v.append(self.rules[0][0])
        for l in v:
            rule = self.find_rule(l)
            for s in rule:
                if s.isupper():
                    if s not in v:
                        v.append(s)
        i=0
        while i < (len(self.rules)):
            if self.rules[i][0] not in v:
                self.rules.pop(i)
            else: i+=1
        self.trim_inf()
    def find_rule(self,exp):
        for rule in self.rules:
            if rule[0] in exp:
                return rule
        return ''
    def trim_inf(self):
        for rule in self.rules[1:]:
            hasInf = True
            literals = rule.split()
            for literal in literals[1:]:
                if (literal).find(literals[0]) == -1:
                    hasInf = False
            if hasInf:
                self.rules.remove(rule)
                temp_r = self.rules[0].split()
                for temp in temp_r[1:]:
                    if temp.find(rule[0]) != -1:
                        temp_r.remove(temp)
                self.rules[0] = " ".join(temp_r)
                for i in range(len(self.rules)):
                    literals2 = self.rules[i].split()
                    for literal2 in literals2:
                        if rule[0] in literal2:
                            self.rules[i] = self.rules[i].replace(literal2,'')
    def trim_lambda(self):
        vn = ['0']
        for i in range(len(self.rules)):
            for rule in self.rules:
                literals = rule.split()
                for literal in literals[1:]:
                        if self.char_in_list(vn,literal):
                            if literals[0] not in vn:
                                vn.append(literals[0])
        for rule in self.rules:
            literals = rule.split()
            for literal in literals[1:]:
                for v in vn:
                    if v in literal:
                        temp = rule[0] + rule[1:].replace(v, '')
                        if temp not in self.rules:self.rules.append(temp)
        # delete rules with zeros
        i=0
        while i<len(self.rules):
            if '0' in self.rules[i]:
                self.rules.pop(i)
            else: i+=1
    def unify(self):
        v=[]
        for rule in self.rules:
            if rule[0] not in v:
                v.append(rule[0])
        for rule in self.rules:
            for i in range(len(v)):
                if rule[0] == v[i][0]:
                    v[i]+= rule[1:]
        self.rules = v
    def beautify(self):
        for i in range(len(self.rules)):
            l = self.rules[i][1:].split()
            self.rules[i] = self.rules[i][0] + " -> " + " | ".join(l)
    def trim_unit(self):
        #get exps
        unit1=[]
        unit2=[]
        for i in range(len(self.rules)):
            literals = self.rules[i].split()
            for literal in literals[1:]:
                if self.is_unit(literal):
                    unit1.append(literals[0])
                    unit2.append(literal)
                    self.rules[i] = self.rules[i].replace(literal,'')
        r = len(unit1)
        for k in range(r):
            for i in range(len(unit1)):
                for j in range(len(unit1)):
                    if unit2[i] in unit1[j]:
                        if unit1[i]!=unit2[j] and self.unit_check(unit1[i],unit2[j],unit1,unit2):
                            unit1.append(unit1[i])
                            unit2.append(unit2[j])

        for i in range(len(unit1)):
            self.rules.append(unit1[i]+self.get_r(unit2[i]))
    def unit_check(self,u1,u2,ul1,ul2):
        for i in range(len(ul1)):
            if u1 in ul1[i] and u2 in ul2[i]:
                return False
        return True
    def get_r(self,unit):
        for rule in self.rules:
            if rule[0] == unit:
                return rule[1:]
        return ''

    def is_unit(self,literal):
        if len(literal) != 1: return False
        if literal.islower(): return False
        return True
    def print_rules(self):
        print(self.rules)
    def save_results(self):
        file = open("results.txt","w+")
        lines = [x+"\n" for x in self.rules]
        file.writelines(lines)
    def char_in_list(self,li,st):
        for ch in st:
            if ch in li:
                return True
        return False
c = context_free()
c.print_rules()
c.save_results()

