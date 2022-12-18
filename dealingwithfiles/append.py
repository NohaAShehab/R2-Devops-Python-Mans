""" append file
    when you open file with a mode, if the file
    not exists --> python will try to create it.
"""
try:
    fileobj = open("info.txt" , "a")
    # when you open file with mode a --> if file doesn't exists 0--> will create it
    # if the file exists ---> will keep its content
except Exception as e:
    print(e)
else:
    # fileobj.write("Hello world\n")
    # fileobj.write("Good morning")

    ### write from byte 10 in the file
    # fileobj.write("Hello world\n")
    # fileobj.write("Good morning")
    # fileobj.close()
    ######## writelines

    fileobj.writelines(["Ali\n", "Ahmed\n", "Mohamed\n"])
    fileobj.close()