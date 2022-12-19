"""
    access modifiers for the instance properties

    public  :::: direct access to the properties and function using the object (anywhere in the script)
    protected :::: direct access to the properties and function using the object
                (in the class or the derived / child classes)
    private ::::  direct access to the properties and function using the object
                (only in the class)

    =======================> No Access Modifiers <=========================
    alpahs ----> public
    _property ----> protected
    __property/method ----> private ----> limit accessibility & apply logic on this data.
"""


# class Employee():
#     def __init__(self,name, email, salary):
#         self.name = name
#         self._email = email
#         self.__salary  = salary
#
#     def printEmp(self):
#         print(f"My name is {self.name}, You can reach me {self._email}")

# e = Employee("Ahmed", 'ahmeed@gmail.com', 10000)
# e.printEmp()
# print(e.name)
# e.name = 'updated'
#
# print(e._email)  # ethically don't do this
# e._email = 'updated@gmail.com'
###################################3

# class Employee():
#     def __init__(self,name, email, salary):
#         self.name = name
#         self._email = email
#
#         if isinstance(salary, int):
#             self.__salary = salary
#         else:
#             self.__salary = 0
#
#     def printEmp(self):
#         print(f"My name is {self.name}, You can reach me {self._email}")
#
#
#     def getSalary(self):
#         return self.__salary*.89
#
#     # def setSalary(self, sal):
#     #     if isinstance(sal, int):
#     #         self.__salary = sal
#     #     else:
#     #         self.__salary = 0
#
# e = Employee("Ahmed", "ahmed@gmail.com", 100000)
# # e.setSalary(20000)
# print(e.getSalary())
###########################################################################
"""
    class Employee(){
        private name;
        protected id;
        public name; 
        
        
        function Employee(){}
        
        function setName()
        
    }


"""
class Employee():
    def __init__(self,name, email, salary):
        self.name = name
        self._email = email
        self.salary = salary


    def printEmp(self):
        print(f"My name is {self.name}, You can reach me {self._email}")

    @property
    def salary(self):
        return self.__salary*.89
    #
    @salary.setter
    def salary(self, sal):
        if isinstance(sal, int):
            self.__salary = sal
        else:
            self.__salary = 0

e = Employee("Ahmed", "ahmed@gmail.com", "iti")
# e.setSalary(20000)
# print(e.getSalary())

# print(e.salary)

# print(e.getsalary)
print(e.name)
# e.name = 'updated '
e.salary = 500000



print(isinstance(e, object))


q = [3,4,5,6,7]

{
    "q": [3,4,5,6,7]
}












