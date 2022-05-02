"""Write an object oriented program to store and display the values of a 2D array
Program should contains 3 functions including the main function
main()
Declare an array
Call function getArray()
Call function displayArray()
		getArray()
Get values to the array
		displayArray()
Display the array values
"""
class array:
    def getarray(self,l, d):
        self.l=l
        self.d=d
        size = d
        print("enter the elements of array : ")
        for i in range(size):
            m = []
            for j in range(size):
                m.append(int(input()))
            l.append(m)
        return l

    def displayarray(self,k):
        self.k=k
        print("array = " + str(k))


n = int(input("enter the size of array : "))
arr = []
x = array()
l1 = x.getarray(arr, n)
x.displayarray(l1)
