

# info = ("Noha", "iti", "Engineering")

"""
    dictionary ---> no index but key:value
"""
# d = {}
# print(d)
#
# info = {"name": "Noha", "email": "nshehab@iti.gov.eg", "name":"Noha Shehab"}
# print(info)
#
# print(info["name"])
#
# info["name"]= "Ahmed"
# print(info)
# info["city"]= "Cairo"
# print(info)
#
# print(len(info))

""""""

# mystring = "Ahmed"
# print(len(mystring))
# l = [2,4,5,6,55, "kd"]
# print(len(l))

# t = ('gg',22,4,5,6,55, "kd")
# print(len(t))

info = {"name": "Noha", "email": "nshehab@iti.gov.eg", "age":30, "city":"Mansoura"}
print(len(info))

# keys = info.keys()
# print(keys)
# for k in keys:
#     print(k)
#
# keys= list(keys)
# print(keys)

# values = info.values()
# print(values)
# for v in values:
#     print(v)
#
# values= list(values)
# print(values)
##############################3
userinfo= {
    "fname":"",
    "lname":"",
    "age":"",
    "country":""
}
# print(userinfo)
# ### loop over the keys
# for key in userinfo.keys():
#     userinfo[key]=input(f"please enter value for {key}: ")
#
# print(userinfo)
#
# items = info.items()
# print(items)
# items = list(items)
# print(items)

# info = {"name": "Noha", "email": "nshehab@iti.gov.eg"}
# d2 = {"work": "iti", "course": "python", "name": "noha dddd"}
# info.update(d2)


info = {"name": "Noha", "email": "nshehab@iti.gov.eg",
        "courses":{"c1":"python", "c2":"django"}
        }

# print(info["courses"]["c1"])

# for i in info:
#     print(f"{i}, {info[i]}")
#
# print("Noha" in info)  # check if the key exists --
# print("Noha" in info.values())  # check if the key exists --

# info.clear()

# for m in range(5):  # generate range of values from 0 to 4
#     print(m)

# m = range(5)
# print(m)  # start =0, step=1 , stop=5
# m = list(m)
# print(m)

# m = range(1,5)
# print(m)  # start =0, step=1 , stop=5
# m = list(m)
# print(m)



# m = range(1,10, 2)
# print(m)  # start =0, step=1 , stop=5
# m = list(m)
# print(m)


# m = range(10,1, -2)
# print(m)  # start =0, step=1 , stop=5
# m = list(m)
# print(m)

""" --- predefined number of iterations ----"""
# for char in 'noha':  # 4
#     print(char)
#
#
# for c in [3,4,5,6,6]:  # 5
#     print(c)


    # name = input("please enter name :  ")
    # if name.isalpha():
    #     print("name valid ")

# name = input("please enter name :  ")
# while not name.isalpha():
#     name = input("please enter name :  ")

# count = 0
#
# while count < 5:
#     print("----- iti ------")
#     count +=1


# name = input("please enter name :  ")
# while not name.isalpha():
#     name = input("please enter name :  ")

#
# for i in range(10):
#     if i == 4:
#         break  # stop the loop
#     print(i)

# while True:
#     name = input("please enter name :  ")
#     if name.isalpha():
#         break

######################
# for i in range(10):
#     if i == 4:
#         break  # stop the loop
#     print(i)
# else:
#     print("------------ loop ended ----------------- ")
"""
    if(name =='Ahmed'){}
    
"""
# name = 'Ahmed'
# if name =='Ahmed':
#     pass
#
# x = 10
#
# for i in range(5):
#     pass

#
# for i in range(5):
#     if i==3:
#         pass
#     print(i)