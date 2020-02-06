



newline = "\n---------------"

print("Read a file called Notes.txt")

# open("Notes.txt", "r")  # r - only want to read file
# open("Notes.txt", "w")  # w - write file
# open("Notes.txt", "a")  # a - append to file
# open("Notes.txt", "r+")  # r+ - read and write file

print(newline)
notes_file = open("Notes.txt", "r")  # r - only want to read file
print("When you are done with a file, make sure to close it also.")
notes_file.close()


print(newline)
notes_file = open("Notes.txt", "r")  # r - only want to read file
print("Check if a file is readable")
print(notes_file.readable())



print(newline)
print("Actually read/print the contents of the file.")
print(notes_file.read())
notes_file.close()


print(newline)
print("Open file, and read specific lines")
notes_file = open("Notes.txt", "r")
print("Readline remembers what line. Multiple will auto move onto next line.")
print(notes_file.readline())
print(notes_file.readline())
print(notes_file.readline())
notes_file.close()


print(newline)
notes_file = open("Notes.txt", "r")
print("Plural readlines, goes through, and places each/every line into a local array also.")
print(notes_file.readlines())
notes_file.close()
