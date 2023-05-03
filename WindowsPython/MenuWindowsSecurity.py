## Import the required libraries
import os
import subprocess
#^^^ Python Libraries
#vvv NCT Functions
from GetCPUTemperature import run_cpu_temperature_script
from GetDiskUsage import run_disk_usage_script
# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------
# Define text colors
# Define ANSI escape codes for text colors
reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
# Print text in different colors
# print(f"{red}This text is red{reset}")
# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------
# Execute the function
# --------------------------------------------------------
# Define a function to print the menu options
def print_menu():
    print(f"{blue}|-----------------------------------------------------|{reset}")
    print(f"{yellow}|-----------------Windows Python Menu-----------------|{reset}")
    print(f"{blue}|-----------------------------------------------------|{reset}")
    print("| 1. Check CPU Temperature")
    print("| 2. Check Disk Usage")

    print("| q. Quit")
# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------
# Define the main function
def main():
    # Run the menu in a loop until the user decides to quit
    while True:
        # Display the menu options
        print_menu()
        # --------------------------------------------------------
        # Get the user's choice as input
        user_input = input("Please enter your choice or 'q' to quit: ")
        print("--------------------------------------------------------\n")
        # --------------------------------------------------------
        # If the user chooses option 1, run the CPU temperature script
        if user_input == '1':
            run_cpu_temperature_script()
        # END 1--------------------------------------------------------
        if user_input == '2':
            run_disk_usage_script()
        # END 2--------------------------------------------------------
        if user_input == '3':
            break
        # END 3--------------------------------------------------------
        if user_input == '4':
            break
        # END 4--------------------------------------------------------
        if user_input == '5':
            break
        # END 5--------------------------------------------------------
        if user_input == '6':
            break
        # END 6--------------------------------------------------------
        # --------------------------------------------------------
        # If the user enters 'q', exit the loop and end the script
        elif user_input.lower() == 'q':
            print("Goodbye!")
            break
        # If the user enters an invalid choice, display an error message
        else:
            print("Invalid choice, please try again.")
# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------
# If the script is being run directly (not imported as a module), call the main function
if __name__ == "__main__":
    main()
# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------
