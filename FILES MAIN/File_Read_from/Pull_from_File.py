

print('\n We have to specify why we are opening this file. Read, write, appending, or both R/W')
print(' You include a comma, then:  r   or   w   or   a   or   r+    in quotes. ')
#   Just to read the file
f = open('test.txt', 'r')

print('\n We just opened the file, and are printing the name of the file. ')
print('\t', f.name)


print('\n We can print the mode that we just opened the file for = ')
print(f.mode)


print('\n Note: You always have to close a file.')
f.close()






print('\n=====================================================')
print(' The open that we did above, is simple but can lead to problems. Another way below.')

print(' This with way, will auto close after we are done to prevent leaks. ')
print(' Open the file to read, set full contents to variable. Print variable')
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print('\n f_contents = \n', f_contents)

print(' Note: This is fine for a small file, but is not good for a large one.')



print('\n\n=====================================================')
print(' We can read line by line. It looks strange ')
print(' Reads each line, and places each as a new element in list.')
with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)



print('\n\n=====================================================')
print(' We can read individual line.    ')
print(' Reads each line, and places each as a new element in list.')
with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)

    f_contents = f.readline()
    print(f_contents)
print(' This auto includes a line. To prevent, use end=''')

with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents, end='')



print('\n\n=====================================================')
print(' This is efficient. Read a line, print it out. Repeat.')
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')



print('\n\n=====================================================')
print(' This read the first 100 characters in and prints them out. ')
with open('test.txt', 'r') as f:
    f_contents = f.read(100)
    print(f_contents, end='')



print('\n\n=====================================================')
print('This will be an iterative loop. Grab the first 100 chars. Include a while loop.')
print(' The while loop checks if the contents is greater than 0, if so it prints. Gets the next')
print(' Because we get the next in the loop, it will stop if the next is not > 0')
print(' This will go until the end of the file.')

with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)




print('\n\n=====================================================')
print(' This is the same as above, but you can see that our read of 10 chars is noted.')
print(' After we get through 10 chars, it prints a *')
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)




print('\n\n=====================================================')
print('     Step 1 -> read 10 char')
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

print('\n=====')
print('     Step 2 -> read 10 char twice i.e. 20')
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

print('\n=====')
print('     Step 3 -> read 10 char twice i.e. 20')
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)
    print('\t This shows that we can read 10 chars twice, but read from anywhere.')
    print('\t Here we used f.seek(0) in between to start from the beginning AGAIN.')
print('\n\n=====================================================')

print('\n\n=====================================================')

print('\n\n=====================================================')

print('\n\n=====================================================')






print('\n\nConfirm the file is close? = \t', f.closed)