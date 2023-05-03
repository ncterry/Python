##################################################
#Disk usage:
#You can use the shutil module from the Python standard library to monitor disk usage.
#Example:
#    Total space: 457 GB
#    Used space: 310 GB
#    Free space: 147 GB
import shutil
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
# Define text colors
# Define ANSI escape codes for text colors
reset = "\033[0m"
red = "\033[31m"
#     print(f"{red}2. Check Disk Usage{reset}")
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
def diskUsage():
    # DISKUSAGE IS THE REAL FUNCTION BUT ALL IT DOES IS RETURN THE VALUES.
    total, used, free = shutil.disk_usage("C:\\")

    return total, used, free
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------
def run_disk_usage_script():
    print(f"{red}2. Check Disk Usage{reset}")
    # DISKUSAGE() IS THE REAL FUNCTION
    # THIS FUNCTION ACTUALLY PRINTS PRETTY

    total, used, free = diskUsage()
    # --------------------------------------
    print(f"Total space: {total // (2 ** 30)} GB")
    print(f"Used space: {used // (2 ** 30)} GB")
    print(f"Free space: {free // (2 ** 30)} GB")
    # --------------------------------------
    print("********************************************\nPress Enter to continue")
    # INPUT JUST WAITS FOR ENTER. ALLOWS FOR A PAUSE
    input()
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------