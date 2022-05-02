"""Write a menu driven program to calculate the area of a given object.
Program should contain two classes
Class 1: MyClass
Class 2: Area
Class MyClass should inherit class Area and should contain the following functions
main()
circle()
square()
rectangle()
triangle()
Class Area should contain the following functions to calculate the area of different objects
circle()
square()
rectangle()
triangle()
"""

class Area:
    def circle(self):
        r=int(input("enter the radius :"))
        area=3.14*r*r
        print("Area = "+str(area))
    def square(self):
        s=int(input("enter the length of one side :"))
        area=s*s
        print("Area = "+str(area))
    def rectangle(self):
        a=int(input("enter the length :"))
        b=int(input("enter the breadth :"))
        area=a*b
        print("Area = "+str(area))
    def triangle(self):
        h=int(input("enter the height of triangle :"))
        l=int(input("enter the length of base of triangle :"))
        area=0.5*l*h
        print("Area ="+str(area))
class Myclass(Area):
    def circle(self):
        super().circle()
    def square(self):
        super().square()
    def rectangle(self):
        super().rectangle()
    def triangle(self):
        super().triangle()
x=Myclass()
print("select your option\n"
      "1-circle\n"
      "2-square\n"
      "3-rectangle\n"
      "4-triangle")
choice=int(input("enter the option number :"))
if choice==1:
    x.circle()
elif choice==2:
    x.square()
elif choice==3:
    x.rectangle()
elif choice==4:
    x.triangle()
else:
    print("invalid entry")
