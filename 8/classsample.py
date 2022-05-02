class MySampleClass:
    year=2020
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1
    def relocate(self,place):
        self.place=place
    def display(self):
        print("year:"+str(MySampleClass.year))
        print("name "+self.name)
        print("age:" +str(self.age))
        print("place:"+self.place)
    @classmethod
    def add_year(cls):
        cls.year = cls.year + 1
    @staticmethod
    def display_welcome():
        print("Welcome")

MySampleClass.display_welcome()
x=MySampleClass("sreerag",21,"calicut")
y=MySampleClass("me",52,"palakkad")

x.display()
y.display()
print("___________________________________________________")

MySampleClass.year=MySampleClass.year+1
x.add_age()
y.add_age()

x.display()
y.display()
print("___________________________________________________")
MySampleClass.add_year()

x.add_age()
y.add_age()
x.relocate("delhi")
y.relocate("kerala")
x.display()
y.display()



"""    def hello(self,k):
        self.s=k
    def print_name(self):
        print(self.s)

x=MySampleClass()
y=MySampleClass()
s="sree"
x.hello(s)
y.hello("me")
x.print_name()
y.print_name()"""
