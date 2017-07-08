
print('\n\n Import the built in OS module')
import os


# -----------------------------------------------------------------------------------
print('\n Print the functions in the OS module. \n ================')
print(dir(os))

# -----------------------------------------------------------------------------------
print('\n Print the current folder pathway:     os.getcwd()')
print(' We will get:\t', os.getcwd())

# -----------------------------------------------------------------------------------
print('\n We can change that working folder from here, with os.chdir()')
os.chdir('/Users/Tracksta6/Dropbox/Python/OS_Module/ForChange')
print(' Now we have:\t', os.getcwd())

# -----------------------------------------------------------------------------------
print('\n We can view a list of the current files in the directory we just changed with:    os.listdir()')
print('\t', os.listdir())

# -----------------------------------------------------------------------------------
print('\n To create a new folder in the directory. There are 2 methods')
os.mkdir('OS-Demo-2')
os.makedirs('OS-Demo-3/Sub-Dir-1')
print(' We just created two new folders in our current directory.')
print(' The difference between mkdir and makedirs  is that mkdir only creates')
print(' one folder, but makedirs can create a pathway as in, a folder within a folder.')

os.makedirs('OS-Demo-4/Sub-Dir-2')
print('\n We just created 3 main folders, and a sub folder in two of them.')
print(' Note we may get an error if we run this again. It cant overwrite a folder')
print('\t', os.listdir())



# -----------------------------------------------------------------------------------
print('\n We just created 3 folder sets, now lets remove 3.')
os.rmdir('OS-Demo-2')
os.removedirs('OS-Demo-3/Sub-Dir-1')
os.removedirs('OS-Demo-4/Sub-Dir-2')
print('\t', os.listdir())
print(' Hashtag one of the removes, to see what the folder will be. We deleted everything created above.')



# -----------------------------------------------------------------------------------
print('\n We want to rename then remove a file or folder.')
print(' Note, This rename wont work if you dont have the file by name. ')
print('\t', os.listdir())
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
print(' Created a copy of a file')
print('\t', os.listdir())

print('\n Now we will rename that file.')
os.rename('test_copy.txt', 'test_copy_CHANGED.txt')
print('\t', os.listdir())

print('\n Now and will remove that copy file.')
os.remove('test_copy_CHANGED.txt')
print('\t', os.listdir())



# -----------------------------------------------------------------------------------
print('\n\n We want to print out the STATS on a file or folder using:     os.stat('')')
print('\t', os.stat('test.txt'))
print(' What you see is not easy to read. You can target them specifically.')
print(' The file is:\t', os.stat('test.txt').st_size, 'bytes')
print(' The file was last modified:\t', os.stat('test.txt').st_mtime)

print(' This is not human time, it is a timestamp, we need to import from the datetime library. Do below')

# -----------------------------------------------------------------------------------
from datetime import datetime
# Create a var for the time
mod_time = os.stat('test.txt').st_mtime
print('\n\t', datetime.fromtimestamp(mod_time))



# -----------------------------------------------------------------------------------
print('\n\n How to view all the folders and files starting from a directory.')
for dirpath, dirnames, filenames in os.walk('/Users/Tracksta6/Desktop/AdStick'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()


# -----------------------------------------------------------------------------------
print('\n\n View home directory. Use:   os.environ.get(q Home q)')
print('\t', os.environ.get('HOME'))



# -----------------------------------------------------------------------------------
print('\n\n We can move an existing file to another directory.')
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)



# -----------------------------------------------------------------------------------
print('\n\n Note: This is a fake path.')
print(' Basename = \t', os.path.basename('/tmp/test.txt'))
print(' Directory = \t', os.path.dirname('/tmp/test.txt'))
print(' Both = \t', os.path.split('/tmp/test.txt'))
print(' Does the path for   (tmp/test.txt)   even exist? = \t', os.path.exists('/tmp/test.txt'))
print(' Does the path for   (Users/Tracksta6/Dropbox/Python/OS_Module/ForChange)   even exist? = \t', os.path.exists('/Users/Tracksta6/Dropbox/Python/OS_Module/ForChange'))

print('\n Check if  ( /Users/Tracksta6/Desktop/AdStick )  is a Directory: \t', os.path.isdir('/Users/Tracksta6/Desktop/AdStick'))
print(' Check if   ( /Users/Tracksta6/Desktop/AdStick/SANY0410.JPG )   is a file: \t', os.path.isfile('/Users/Tracksta6/Desktop/AdStick/SANY0410.JPG'))



# -----------------------------------------------------------------------------------
print('\n\n To get the filename without the extension')
print('\t', os.path.splitext('/Users/Tracksta6/Desktop/AdStick/SANY0410.JPG'))



# -----------------------------------------------------------------------------------
print('\n\n View everything in the os.path')
print(dir(os.path))

# -----------------------------------------------------------------------------------