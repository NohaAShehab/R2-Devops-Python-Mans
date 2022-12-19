

"""

    validate email , validate url , validate ip address

"""
import re

email = input("please enter your email: ")
# print(email)

emailpattern=  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# res=re.match(emailpattern, email)  # check if part of the string follows the pattern then
# # will return with match object
# """ if the string follows the pattern ? ---> re.match --> return match object else None"""
# # print(res)
# if res:
#     print("-----Email valid")
# else:
#     print("---- email not valid ---")
########################33
# res=re.fullmatch(emailpattern, email)  # check if all the string follows the pattern then
# # will return with match object
# print(res)
##############################


res=re.search(emailpattern, email)  # check if all the string follows the pattern then
# will return with match object
print(res)

from getpass import getpass
password = getpass("please enter password : ")


