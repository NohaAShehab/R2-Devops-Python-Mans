name = 'Noha'
# def sumnum(num1, num2):
#     res = num1 + num2
#     print(res)
#
# sumnum(10 ,20)


"""
    Any variable define in the python file ---> has scope ---> global scope
    you can access it anywhere in the script...

    Any variable defined in the python function ---> has scope ---. local scope
"""

# course = 'python' # global scope --->
#
# def test():
#     print(f"from inside the function -----> {course}")
#     print('--- hello world----')
#
# test()
# print(course)

#############################################

# course = 'python' # global scope --->
#
# def test():
#     course='django'  # any variable defined inside a function ---> local scope ?
#     ## can be accessed only inside the function
#     print(f"from inside the function -----> {course}")
#     print('--- hello world----')
# test()
# print(course)

########################################################

# course = 'python' # global scope --->
# def test():
#     global course
#     course ='django'  # any variable defined inside a function ---> local scope ?
#     ## can be accessed only inside the function
#     print(f"from inside the function -----> {course}")
#     print('--- hello world----')
# test()
# print(course)

#########
# course = 'python'  # global scope --->
# def test():
#     course = 'django'
#     print(f"from inside the function -----> {course}")
#     print('--- hello world----')
#     return course
#
# course=test()
# print(course)

#####################################################################

""" function inside  a function """

# def outerfunction():
#     course = 'python'
#
#     def innerfunction():
#
#         print(f"---- course from inner function {course}")
#
#     innerfunction()
#     print(f"---- course from outer function {course}")
#
#
# outerfunction()
##################################
# def outerfunction():
#     course = 'python'
#
#     def innerfunction():
#         course='django' # new local variable for the innerfunction
#         print(f"---- course from inner function {course}")
#
#     innerfunction()
#     print(f"---- course from outer function {course}")
#
#
# outerfunction()
##########################
# def outerfunction():
#     course = 'python'
#
#     def innerfunction():
#         nonlocal course
#         course='django' # new local variable for the innerfunction
#         print(f"---- course from inner function {course}")
#
#     innerfunction()
#     print(f"---- course from outer function {course}")

# outerfunction()


###########################################33

def test():
    name = 'Ali'
    def abc():
        nonlocal name
        name = 'Ahmed'
        def mm():
            nonlocal name
            name = 'Radwa'
        mm()
        print(name)
    abc()
    print(name)

test()
###############################


#
# def test():
#     def abc():
#         def mm():
#             global name
#             name = 'Ahmed'
#         mm()
#     abc()
#     print(name)
#
# test()
# print(name)
#
# def askforinput(option):
#
#     def test():
#         print("-------------------test")
#     def hello():
#         print("----------------------hello")
#
#     if option=="test":
#         test()
#     elif option=='hello':
#         hello()
#         test()
#     else:
#         print(option)



# askforinput("hello")



















