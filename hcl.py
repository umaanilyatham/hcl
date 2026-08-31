

with open("file.txt","r") as file:
    content = file.read()
    print("File content:")
    print(content)

with open("file1.txt","x") as file1:

    file1.write(content)

    print("copy the content successfully.")
