class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print("Name of person is {} and idnumber is {}".format(self.name,self.idnumber))

class employee((person)):
    def __init__(self,name,idnumber,salary,post):
        person.__init__(self,name,idnumber)
        self.salary=salary
        self.post=post

emp1=employee("Pragyan",1295,50000,"Senior Developer and Head coder")
emp1.display()
emp2=employee("Tabassum",1,120000,"CEO")
emp2.display()
emp3=employee("Basob",1221,5000,"Intern and P.A of Senior Developer")
emp3.display()