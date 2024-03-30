with open("my_file.txt", "w") as file:
    file.write("Hello, this is a new file.\n")
    file.write("It contains three lines of text.\n")
    file.write("0, 5, 15\n")

with open("my_file.txt", "r") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", "a") as file:
    file.write("This is a new line appended to the file.\n")
