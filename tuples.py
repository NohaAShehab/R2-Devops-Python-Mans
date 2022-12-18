"""
    tuple  --- > immutable datatype ---> cannot be changed
    --? access elements using index
"""
# t = tuple()
# t = tuple([5, 6, 7, "iti", "python"])
# print(t[4])

t2 = ("iti", "3DFX", "python", "databases")
# t2[0]='updated'

for item in t2:
    print(item)

"tuple concatenation"
t1= ("item", "abc", "test")
t2 = ("Ahmed", "Ali", "Omar", "test")
t3  = t1 + t2
print(t3)

print(min(t1))
print(max(t2))

""" cast tuple to a list"""
t2 = ("Ahmed", "Ali", "Omar", "test")
print(t2)
t2 = list(t2)
print(t2)
t2.append("ali")
print(t2)
t2 = tuple(t2)
print(t2)

"""tuple of one item """
t = ("item01",)