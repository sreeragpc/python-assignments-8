number1 = int(input("enter 2 numbers"))
number2 = int(input())
print(type(number1))#type of number 1
tempfile = number1
number1 = number2
number2 = tempfile
print(str(number1)+ "," +str(number2))