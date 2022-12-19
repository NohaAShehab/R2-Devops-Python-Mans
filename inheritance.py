

# class Person:
#
#     def __init__(self,name, bdate):
#         self.name = name
#         self.bdate = bdate
#
#
#     def sayhello(self):
#         print(f"Hello {self.name}")
#
# class Employee(Person):  # inheritance relation
#     pass
#
#
# e = Employee("Ahmed", "Ali")
# e.sayhello()

###################################


class Person:

    def __init__(self,name, bdate):
        self.name = name
        self.bdate = bdate


    def sayhello(self):
        print(f"Hello {self.name}")

class Employee(Person):  # inheritance relation
    def __init__(self,name, bdate, email, salary):
        super().__init__(name, bdate) # call parent constructor
        self.email = email
        self.salary  = salary

    def printEmp(self):
        print(f"My name is {self.name}, You can reach me {self.email}")

e = Employee("Ahmed", "june", 'ahmeed@gmail.com', 10000)
e.sayhello()
e.printEmp()




""" python support mutiple inheritance"""

# class Parent1:
#     pass
#
# class Parent2:
#     pass
#
# class Child(Parent1, Parent2):
#     pass
