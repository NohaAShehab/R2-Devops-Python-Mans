

"""
    -simple text files-
    operations ----> read file content, write content to the file , append content to the file

    append ===> keep old content ---> and add the new content
    write ===> remove old content ---> add the new content

    -----------------------------------------------
    1- open file (opening_mode) ---> read(r), write(w), append(a)
    2- do operation (reading , writing)
    3- close file ---> close
"""

""" 1- read file content """
try:
    fileobject =open("users.txt", "r")  # textIOWrapper
except Exception as e:
    print(e)
else:
    # 1-read file content
    # data = fileobject.read()  # read all file content into one string
    # print(data)

    # # 2- read file line by line
    # for line in fileobject:
    #     print(line, end="#")

    #3- read file content into a list
    fileobject.seek(10)
    lines = fileobject.readlines()
    print(lines)


    # close file
    fileobject.close()













