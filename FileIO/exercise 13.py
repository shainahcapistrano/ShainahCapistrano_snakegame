def copy_file(file1, file2):
    file_handle = open(file1, "r")
    contents = file_handle.read()
    print(contents)
    file_handle.close()
    file_handle = open(file2, "w")
    file_handle.write(contents)
    file_handle.close()


copy_file("test.txt","copytest.txt")
