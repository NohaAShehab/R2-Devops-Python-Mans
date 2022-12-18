""" write file
    when you open file with w mode, if the file
    not exists --> python will try to create it.
"""
try:
    fileobj = open("mycv.txt" , "w")
    # when you open file with mode w --> if file doesn't exists 0--> will create it
    # if the file exists ---> will remove its content
except Exception as e:
    print(e)
else:
    # fileobj.write("Hello world\n")
    # fileobj.write("Good morning")

    ### write from byte 10 in the file
    # fileobj.seek(10)
    # fileobj.write("Hello world\n")
    # fileobj.write("Good morning")
    # fileobj.close()
    ######## writelines

    fileobj.writelines(["Ali\n", "Ahmed\n", "Mohamed\n"])
    fileobj.close()