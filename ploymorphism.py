
class Person:

    def __init__(self,name, bdate):
        self.name = name
        self.bdate = bdate


    def sayhello(self):
        print(f"Hello {self.name} ---> the parent class version ")

    def test(self):
        print("----- test function ")

class Employee(Person):  # inheritance relation
    def __init__(self,name, bdate, email, salary):
        super().__init__(name, bdate) # call parent constructor
        self.email = email
        self.salary  = salary

    def printEmp(self):
        print(f"My name is {self.name}, You can reach me {self.email}")

    def sayhello(self):
        super().sayhello()  # optional
        print("----- called from the child Employee class")

e = Employee("Ahmed", "june", 'ahmeed@gmail.com', 10000)
e.sayhello()  #
e.test()

p = Person("Hiedy", 'July')
p.sayhello()
p.test()

print(isinstance(e,Person))




"""
    polymorphism 
    overriding ---> 2 functions with the same name in 2 classes have inheritance relation 
    ---> each function do something else...  
    overloading ====> 
    2 functions with same name in the same class ---> different in number of arguments or 
    type of arguments

"""


"no explicit overloading in python ---> "
# class Test:
#
#
#     def sayhi(self,name=""):
#         print(f"hi {name}")
#
# t =Test()
# t.sayhi()
### pip install dispatch package --> overloading