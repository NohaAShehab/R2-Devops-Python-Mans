
# emp = {
#     "id":1,
#     "name":"Ahmed",
#     "company": "VOIS"
# }
#
# emp2 = {
#     "empid":1,
#     "username":"Ahmed",
#     "companyname": "VOIS"
# }

############### define our own datatype ---> OOP oriented principles ?

"""
    item ----> properties
        ---> functionalities

"""
l = [3,4,5,6]
l.append("2")

# "1- create class ---> template defin. "
# class Employee:
#     pass
#
# "2- object 000> your own copy from the class ---> contain data , functionality. "
# #### create object or instance from the class
# emp =  Employee()
############################################

"1- create class ---> template defin. ---> object factory "
# class Employee:
#     """ built-in constructor function ---> calling when you create object """
#     def __init__(self): # self refers to the object address in the memory
#         print("------ the __init__ function called --> while creating object")
#         print(f"self={self}")
#         self.id = 1
#         self.name = 'Ahmed'
#         self.email = 'ahmed@gmail.com'
#
#
# emp =  Employee()   # this is an object
# print(emp)
# print('----------------------------------------------------------')
# emp2 =  Employee()   # this is an object
# print(emp2)
#############################################
class Employee:
    def __init__(self, id , name, email):
        # id , name , email ---> instance variables
        self.id = id
        self.name = name
        self.email = email

    #### instance method
    def printEmp(self):
        print(f"id={self.id}, name={self.name}, email={self.email}")



emp =  Employee(1, "Ahmed", "ahmed@gmail.com")   # this is an object
emp.printEmp()
print(emp.name)
print(emp.email)
emp.name= 'Ahmed Mohamed'
print('----------------------------------------------------------')
emp2 =  Employee(2, "Ali", "ali@gmail")   # this is an object
emp2.printEmp()























