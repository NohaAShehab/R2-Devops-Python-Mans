""" non primitive datatypes
    list  ----> hold set of values from different datatypes

"""
"1- to define a list "
l = ["Ahmed", 33, "Python", "Ali", True, 3.14, True, "Python"]
myl = []
"2- you can access list elements using the index ---> start from 0 ?"
print(l[3])
"3- list is mutable datatype ? ---> you can change list content in the run time "
l[3] = "Updated"
print(l)
"4- get the len of the list"
print(len(l))
"5- count number of occurance for elements "
print(l.count("Python"))
"6- list can hold another list "
l1 = ["Ahmed", "Python","iti", "Devops", ["Python", 'Kubernetes', 'Microservice'], True, "Python"]

print(l1)

"7- append element to the list in the runtime ----> will add element to the end of the list"
l1.append("added_element")

"8- insert element at certain position in the list"
l1.insert(3, "inserted")

"9- pop element from the list ---> "
# popped_element= l1.pop() # remove the last element in the list

"10- pop element at index from the list"
# popped_element= l1.pop(1)

"11- remove element form the list"
# l1.remove("Python")

"12- loop over the list "
# for item in l1:
#     print(f"item = {item}")
#     if item=="Python":
#         l1.remove(item)
# print(l1)

# """ check existence """
# names = ["Ahmed", "ALi", "iti", "Mohamed", "Omar"]
#
# print("Ahmed" in names)
#
# """ sort the list  -----> list elements must form the same type (values primitive)"""
#
# names = ["Ahmed", "ALi", "iti", "Mohamed", "Omar"]
# print(names)
# # names.sort() # sort the same variable
# # print(names)  # ascending
#
# names.sort(reverse=True)
# print(names)
#
# "reverse list===="
# myl = ["Ahmed", True, 33.44, ["abc", "mm"]]
# print(myl)
# myl.reverse()
# # print(myl)
# # """ ---- list concatenation ----"""
# # l1= ["Ahmed", "Ali",True ]
# # l2 = ["python", "Scripting", "Kubernates"]
# #
# # l3 = l1 + l2
# # print(l3)
#
#
# """ ---- Extend a list  ----"""
# l1= ["Ahmed", "Ali",True ]
# l2 = ["python", "Scripting", "Kubernates"]
# l1.extend(l2)
# print(l1)
#
# """ --- min- max ----> list items should be from the same type ---"""
#
# l = [3,4,5,6,10]
# print(min(l))
# print(max(l))
#
# l2 = ["python", "Scripting", "Kubernates"]
# print(min(l2))
# l2 = ["python", "Scripting", "Kubernates"]
# print(max(l2))

"1- noha  2"

#############
l = []
for i in range(5):
    print(i)
    # l.append()

# I love iti.

# noha ====> nh

for c in "noha":
    print(c)


# 3 =====>
"""
4==> 4, 8, 12 , 16
3===> 3, 6,9
2 ===> 2 , 4
1  ===> 1
"""

# [[1], [2,4],[3,6,9], [4,8,12,16]]