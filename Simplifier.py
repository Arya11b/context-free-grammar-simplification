class context_free:
    def __init__(self):
        self.get_input()
    def get_input(self):
        file = open("test.txt","r")
        print(file.read())
c = context_free()