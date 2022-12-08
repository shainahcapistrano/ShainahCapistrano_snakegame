def copy_file(file1, file2):
    file_handle = open(file1, "r")
    contents = file_handle.read()
    print(contents)


copy_file("test.txt","copytest.txt")