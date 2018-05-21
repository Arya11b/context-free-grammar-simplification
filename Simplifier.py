import re
# we define 0 as λ
class context_free:
    rules = []
    def __init__(self):
        self.split_grammer()
        self.trim_useless()
        self.trim_inf()
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
    def get_expression(self,rule):
        return rule[0]
    def print_rules(self):
        print(self.rules)
    def save_results(self):
        file = open("results.txt","w+")
        lines = [x+"\n" for x in self.rules]
        file.writelines(lines)
c = context_free()
c.print_rules()
c.save_results()

