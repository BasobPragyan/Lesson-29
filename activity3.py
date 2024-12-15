class bird:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("I am {} of {} years old")
    def whoisthis(self):
        print("Bird")
    def swim(self):
        print("I swim fast")

class penguin(bird):
    def __init__(self,name,age):
        super().__init__()
        print("Penguin is ready")
    def whoisthis(self):
        print("Penguin")
    def run(self):
        print("Penguins run faster")

p1=penguin()
p1.whoisthis()
p1.swim()
p1.run()