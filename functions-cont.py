""" define function ----> with default argument ----> with known of arguments """
# def sumnum(num1, num2=10):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#
# sumnum(15)
# sumnum(2,3)

# def sumnum(num1=10, num2=10):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
# sumnum()
# sumnum(15)
# sumnum(2,3)
###########################
print("iti", "devops", "Mansoura", "python", sep="_")
print("test")
# print("nnnn")

""" define function that accept zero or more argument """
# t= ()
# def askforstudents(*names):
#     print(names)
#     for n in names:
#         print(n)
#     print("--------------------------------")
#
# askforstudents()
# askforstudents("Ahmed")
# askforstudents("Ahmed", "Ali", True)
# askforstudents("ali", "omar", ["Ahmed", "Ali"])

#############################################
# def introduceyourself(**info):
#     print(info)
#     print(info.values())
#     print("-----------------------")
#
#
# introduceyourself()
# introduceyourself(name='Ahmed')
# introduceyourself(fname='ali',lname='omar', work='iti')
# introduceyourself(lname='test',email='a@gmail.com',egyption=True, salary=1000)
#
#
# # mystr="My name is {name}, I works at {work}"
# # print(mystr.format(name='noha', work='iti'))
#
#
#
# def askfordict(mydict):
#     print(mydict)
#
# askfordict({"name":"Haithem", "track":"devops"})


# def calculator(operation, *nums):
#     print(nums)
#     if operation=="+":
#         res = 0
#         # for num in nums:
#         #     res +=num
#         res = sum(nums)
#         print(res)
#
# calculator("+", 3,4,5,6,7,6,20)
