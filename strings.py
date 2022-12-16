
name = 'Noha'

""" string is treated like an array ?
 => access string parts using index ---. index start from 0
 
 string is immutable datatype ----> cannot change part of it 
 """

# print(name[2])
#
# print(name[-1])
#
#
# # name[1]= 'b'
# name = 'mmmmm'

# work="Information Technology Institute"
# print(work[2:8]) ## start 2 to 7
# # print(work[100])
# "get len of the string "
# print(len(work))
# "count number of occurance for a char in the word"
# print(work.count("t"))
#
# """ string concatenation ---> between string only """
# firstname = 'Noha '
# midname = 'AbdelHady '
# lastname = 'Shehab '
#
# # fullname = firstname + midname + midname + lastname
# # print(fullname)
#
# fullname = firstname + midname*2 + lastname
# print(fullname.upper())
#
# # mm = 'abc' +str(10)
#
# # name = 'noha'
# # name = name.capitalize()
# # print(name)
#
# name = 'noha'
# name = name.upper()
# print(name)
# #
# name = name.lower()
# print(name)
# print(name.islower())
# print(name.isupper())
########################################################
# mystr = 'My name is Noha , I works at iti.'
#
# ss = mystr.replace("a", '@')
# print(ss)
#
# mm = mystr.replace("i", "I")
# print(mm)

#################################
""" string functions =--> check value in the string  """
# mystr = '100mmm'
# if mystr.isdigit():  # 1, 2,3,4,5,6,7,8,9
#     print("----- digit----")
#     mystr = int(mystr)
# else:
#     print('not a digit')

# mystr = 'abcmmm'
# if mystr.isalpha():  # check if the string ---> content only alphas a--->z only
#     print("----- alphas----")
# else:
#     print('not alphas')
#
# year = '2022'
# print(year.isnumeric())
# mynum  ="3.14"
# print(mynum.isdigit())

#################### string strip
# name = '    My name is Noha               '
# print(name)
# name = name.strip()  # remove spaces from the beginning and the end of the string only
# print(name)

# name = '    My name is Noha               '
# print(name)
# name = name.lstrip()  # remove spaces from the beginning -left of the string-
# print(name)

###########3
# name = '    My name is Noha               '
# print(name)
# name = name.rstrip()  # remove spaces from the beginning -left of the string-
# print(name)

############## strip char or set of chars from the string

# name = '@    aMy name is Noha               @'
# name = name.strip("@a")
# print(name)

# name = '@    aMy name is Noha               @'
# name = name.lstrip("@a ")
# print(name)
# name = '@    aMy name is Noha               @'
# name = name.rstrip("@a ")
# print(name)

###################### format string

# temp = "My name is {0} , I works at {1}"
#
# mystring = temp.format( 'ITI', "Noha")
# print(mystring)
#
# mystring = temp.format("Zahraa", 'DEVOPS')
# print(mystring)

##########################################

# temp = "My name is {username} , I works at {userwork}"
#
# mystring = temp.format(username='Noha', userwork='ITI')
# print(mystring)
#
# mystring = temp.format(userwork='DEVOPS', username='Zahraa')
# print(mystring)

""" f- format string -----"""
# name='Ahmed'
# work= 'VOIS'
# mytemp = f'Myname is {name}, I works at {work}'
# print(mytemp)


# name = input("please enter name: ")  # return with string
# work = input("please enter work")# return with string
# mytemp = f'Myname is {name}, I works at {work}'
# print(mytemp)

# age = input("please enter age : ")
# if age.isdigit():
#     age = int(age)

"""----- NEVER TRUST USER INPUT -----"""
age = int(input("please enter age : "))







