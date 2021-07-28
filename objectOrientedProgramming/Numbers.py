'''
Write a program which contains one class named as Numbers. 
Arithmetic class contains one instance variables as Value. 
Inside init method initialise that instance variables to the value which is accepted from user. 
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), 
Factors(). 
ChkPrime() method will returns true if number is prime otherwise return false. 
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable. 
SumFactors() method will return addition of all factors. Use this method in any another method 
as a helper method if required. 
After designing the above class call all instance methods by creating multiple objects.
'''


class Numbers:
    def __init__(self, num):
        self.value = num

    def chkPrime(self):
        if(self.value <= 1):
            return False

        for i in range(2, self.value):
            if(self.value % i == 0):
                return False

        return True

    def chkPerfect(self):
        if(self.value == (self.sumFactors() - self.value)):
            return True

        return False

    def sumFactors(self):
        sum = 0
        for i in range(1, self.value + 1):
            if(self.value % i == 0):
                sum += i

        return sum

    def factors(self):
        print("Factors of " + str(self.value) + " are: ")
        for i in range(1, self.value + 1):
            if(self.value % i == 0):
                print(i, end=" ")
        print()


def main():
    obj1 = Numbers(6)
    print("Is prime: ", obj1.chkPrime())
    print("Is Perfect: ", obj1.chkPerfect())
    obj1.factors()
    print("Sum of factors: ", obj1.sumFactors())

    obj2 = Numbers(17)
    print("Is prime: ", obj2.chkPrime())
    print("Is Perfect: ", obj2.chkPerfect())
    obj2.factors()
    print("Sum of factors: ", obj2.sumFactors())


if(__name__ == "__main__"):
    main()
