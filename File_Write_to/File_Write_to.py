
print(' We have the file open, but it is read mode with  r. Cant write.')
print(' The Two lines below, will not work together. ')
# with open('test.txt', 'r') as f:
#    f.write('Test')


print('\n\n We just created and wrote   Test   To a new txt file.')
with open('test2.txt', 'w') as f:
    f.write('Test')
    f.write('Test')
print('\t We just wrote   Test back to back.  TestTest')



print('\n\n We wrote Test twice but used seek to start after char 2. = ')
with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(2)
    f.write('Test')
# Next 2 lines are just to write the line we just wrote in the file.
with open('test2.txt', 'r') as f:
    f_contents = f.readline()
    print('\t', f_contents)

# =================================================================
'''We are going to read from one file and write it to another. A simple copy
We open the original test.txt file in the read format.
We then open/create a new write file to copy to.
For each line we read in from the rf
We copy and paste onto the wf.'''

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
print('\n\n We just created a copy line for line of the test.txt file. ')


# =================================================================
'''We can copy a jpg file, just like the txt file above, but with some changes.
Note we cannot use  r  or   w   as they are for ascii. We have to change
the picture files to binary. Use:    rb   and    wb'''
with open('SFP.jpg', 'rb') as pr:
    with open('SFP_copy.jpg', 'wb') as pw:
        for line in pr:
            pw.write(line)
print('\n\n We just copied a picture file line by line. ')



# =================================================================
'''We may want more control. The picture copy above was line by line. Now we will
grab a chunk by chunk, in a loop until we don't have any more to grab.'''
with open('SFP.jpg', 'rb') as pr:
    with open('SFP_chunk_copy.jpg', 'wb') as pw:
        chunk_size = 4096
        pr_chunk = pr.read(chunk_size)
        while len(pr_chunk) > 0:
            pw.write(pr_chunk)
            pr_chunk = pr.read(chunk_size)

print('\n\n We just copied a picture file, using chunks. ')



# =================================================================
'''Now we just did one chunk grab and copy.
We grabbed the first 50000 binary digits and pasted them'''
with open('SFP.jpg', 'rb') as pr:
    with open('SFP_chunk_piece.jpg', 'wb') as pw:
        chunk_size = 50000
        pr_chunk = pr.read(chunk_size)
        pw.write(pr_chunk)
print('\n\n We just copied a picture file, using a chunk piece. ')