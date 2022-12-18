
# x = 10
# print(x)
# print('iti')
# M = 100

""" logical error """
#
# def sumnum(num1, num2):
#     res = num1 * num2
#     print(res)
#
# sumnum(2,2)
# sumnum(2,3)

""" runtime error ----> exceptions """

# age = input("please enter your age : ")
# if age.isdigit():
#     age = int(age)
#     print(age)


""" unexpected runtime errors ---> exceptions """
# exception handling
# print("--------------- before ---------------")
# try:
#     print(portnumber)
# except :
#     print("------------- error happened --------- ")
#     portnumber=3306
# print("----------- after------------")


########################################


# print("--------------- before ---------------")
# try:
#     num = input("please enter number ")
#     num = int(num)
# except Exception as e :
#     print(f"------------- error happened \n {e} --------- ")
#
#
# print("----------- after------------")

#################33

# print("--------------- before ---------------")
# try:
#     m = int('e')
# except NameError as ne :
#     print(f"------------- error happened \n {ne} --------- ")
# except ZeroDivisionError as ze :
#     print(f"------------- {ze} --------- ")
# except Exception as e :
#     print(f"------------- {e} --------- ")
#
# print("----------- after------------")

##############################################
# try:
#     num = input("please enter number : ")
#     num = int(num)
# except Exception as e:
#     print(f"{e}")
# else:
#     num += 10
#     print(num)


# num = input("please enter number : ")
# num = int(num)


#################### finally block #######################

# try:
#     num = input("please enter number : ")
#     num = int(num)
# except Exception as e:
#     print(f"{e}")
# else:
#     num += 10
#     print(num)
# finally:
#     print("-------------- operation done -------------")
# print("-----------------------------")


#############################################################

# def divnums():
#     num1 = input("please enter num1 : ")
#     num2 = input("please enter num2 : ")
#     if num2=='0':
#         raise Exception("cannot divide by zero")
#
#     if num1.isdigit() and num2.isdigit():
#         num1 =  int(num1)
#         num2 = int(num2)
#         res = num1/num2
#
#         print(res)
# divnums()


def divnums():
    while True:
        num1 = input("please enter num1 : ")
        num2 = input("please enter num2 : ")
        if num2=='0':
            continue

        if num1.isdigit() and num2.isdigit():
            break
    num1 =  int(num1)
    num2 = int(num2)
    res = num1/num2

    print(res)
divnums()














