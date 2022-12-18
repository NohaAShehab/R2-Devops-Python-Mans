


"1- generate set of values "
# num =  input("please enter number: ") # string
# allnumbers= []
# if num.isdigit():
#     num = int(num)
#     for i in range(num):
#         newl=[]
#         for j in range(i+1):
#             # print(j)
#             newl.append((j+1)*(i+1))
#         allnumbers.append(newl)
#
#     print(allnumbers)

#############################
"""
    set of values  ---> iteration ---> loop 
"""

l = [4,5,67,"iti", "python"]  # iterable
# print(l[0])
# print(l[1])
# for item in l:
#     print(item)
#
"get index of the element? "
# index = 0
# for item in l:  # loop will work until the len of the list completed
#     print(f"{index}==>{item}")
#     index +=1
#
#     print("==================")


# elements = []
# for i in range(5):
#     # print(i)
#     item = input(f"please enter element {i}: ")
#     if item.isdigit():  # check if the value in the string contains only digits 0 --- 9
#         item = int(item)
#         elements.append(item)


# print(elements)
# elements.sort() # modify the list
# print(elements)
# elements.sort(reverse=True)
# print(elements)

"""
    
"""
# l =['-10', '-100', '-20', '-33']
# l.sort(reverse=True)
# print(l)
#
# num  = input("please enter number : ")
# if num[0]=='-':
#     num=num.strip("-")
#     print(num)
#     if num.isdigit():
#         num = int(num)*-1



elements = []
for i in range(5):
    # print(i)
    item = input(f"please enter element {i}: ")
    if item.isdigit():  # check if the value in the string contains only digits 0 --- 9
        item = int(item)
        elements.append(item)
    elif item[0] == '-':
        item = item.strip("-")
        print(item)
        if item.isdigit():
            item = int(item) * -1
            elements.append(item)

print(elements)
