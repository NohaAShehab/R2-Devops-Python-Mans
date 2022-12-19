class Employee:
    #### class variable ----> property ---> depend on the class itself not on the objects
    human = True
    nationality = "Egyptian"
    count = 0
    def __init__(self, id , name, email, salary=1000):
        # id , name , email ---> instance variables
        self.id = id
        self.name = name
        self.email = email
        Employee.count +=1
        self.salary = salary

    #### instance method
    def printEmp(self):
        print(f"id={self.id}, name={self.name}, email={self.email}")

    # class method ---> behaviour related to the class
    @classmethod
    def get_no_of_employees(cls):  # cls ---> represent the class itself
        # print(cls)
        print(cls.count)

    @staticmethod  # define helper method
    def calnetsal(salary):
        return salary * .88


emp =  Employee(1, "Ahmed", "ahmed@gmail.com")
print(Employee.human)

emp2 =  Employee(2, "ali", "ali@gmail.com", 2000)   # this is an object

Employee.get_no_of_employees()

print(Employee.calnetsal(emp2.salary))

print(Employee.calnetsal(200000))


# def calnetsal(salary):
#     return salary*.88
#
# print(calnetsal(emp2.salary))
#
# print(calnetsal(200000))
