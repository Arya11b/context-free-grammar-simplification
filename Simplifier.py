import re
# we define 0 as λ
class context_free:
    rules = []
    def __init__(self):
        self.split_grammer()
        self.trim_useless()
        self.trim_inf()
        self.trim_lambda()
    def get_input(self):
        file = open("test.txt","r")
        return file.readlines()
    def split_grammer(self):
        strings = self.get_input()
        for st in strings:
            self.rules.append(" ".join(re.findall("[a-zA-Z0]+", st)))
            print(self.rules[-1])
    def trim_useless(self):
        for rule in self.rules[1:]:
            if (self.rules[0]).find(self.get_expression(rule)) == -1:
                self.rules.remove(rule)
    def trim_inf(self):
        for rule in self.rules[1:]:
            hasInf = True
            literals = rule.split()
            for literal in literals[1:]:
                if (literal).find(self.get_expression(literals)) == -1:
                    hasInf = False
            if hasInf:
                self.rules.remove(rule)
                temp_r = self.rules[0].split()
                for temp in temp_r[1:]:
                    if temp.find(self.get_expression(rule)) != -1:
                        temp_r.remove(temp)
                self.rules[0] = " ".join(temp_r)
    def trim_lambda(self):
        vn = []
        for rule in self.rules:
            length = -1
            literals = rule.split()
            for literal in literals:
                    if '0' in literal or self.char_in_list(vn,literal):
                        if literals[0] not in vn:
                            vn.append(literals[0])
        for rule in self.rules:
            literals = rule.split()
            for literal in literals[1:]:
                for v in vn:
                    if v in literal or '0' in literal:
                        temp = rule.replace(v,'')
                        self.rules.append(temp)

    def get_expression(self,rule):
        return rule[0]
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

