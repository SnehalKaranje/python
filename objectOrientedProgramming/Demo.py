'''
Write a program which contains one class named as Demo. 
Demo class contains two instance variables as no1 ,no2. 
That class contains one class variable as Value. 
There are two instance methods of class as Fun and Gun which displays values of instance 
variables. 
Initialise instance variable in init method by accepting the values from user. 
 
After creating the class create the two objects of Demo class as 
Obj1 = Demo(11,21) 
Obj2 = Demo(51,101) 
Now call the instance methods as 
Obj1.Fun() 
Obj2.Fun() 
Obj1.Gun() 
Obj2.Gun()
'''


class Demo:
    Value = 10

    def __init__(self, value1, value2):
        self.no1 = value1
        self.no2 = value2

    def Fun(self):
        print("No1: " + str(self.no1))

    def Gun(self):
        print("No2: " + str(self.no2))


def main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj2.Fun()

    Obj1.Gun()
    Obj2.Gun()


if (__name__ == "__main__"):
    main()
