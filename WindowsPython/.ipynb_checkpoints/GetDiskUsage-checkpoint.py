'''
Disk usage: 
You can use the shutil module from the Python standard library to monitor disk usage.
Example:
    Total space: 457 GB
    Used space: 310 GB
    Free space: 147 GB
'''
#-------------------------------------------------
import shutil
#Example
#total, used, free = diskUsage()
#print(f"Total space: {total // (2**30)} GB")
#print(f"Used space: {used // (2**30)} GB")
#print(f"Free space: {free // (2**30)} GB")
def diskUsage():
    total, used, free = shutil.disk_usage("C:\\")

    return total, used, free
'''

'''
#-------------------------------------------------