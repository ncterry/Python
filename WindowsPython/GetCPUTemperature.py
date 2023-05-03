'''
Monitoring the temperature of CPU and other hardware sensors: 
You can use the py3nvml library to access NVIDIA GPU information (if available) 
or the wmi library for general hardware information. To install these libraries, 
run pip install py3nvml wmi in your terminal or command prompt.

Note: Accessing temperature information might not be supported on all systems. 
You may need to use third-party tools or libraries that are specific to your hardware.
EXAMPLE
temp_c, temp_f = cpuTemperature()
print(f"CPU temperature:", temp_c,  "°C")
print(f"CPU temperature:", temp_f,  "°F")
'''
# --------------------------------------
import wmi
def cpuTemp():
    # THIS IS THE FUNCTION
    # You need to be running in admin privs to use WMI
    w = wmi.WMI(namespace="root\\wmi")
    temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
    
    temp_c = (temperature_info.CurrentTemperature / 10 - 273.15)
    temp_f = (temperature_info.CurrentTemperature / 10 - 273.15) * (9/5) + 32

    return temp_c, temp_f
# END def cpuTemperature():
# --------------------------------------
# --------------------------------------
# --------------------------------------
# Define a function to run the CPU temperature script
def run_cpu_temperature_script():
    # THIS ALLOWS TO CALL THE FUNCTION AND PRINT IT PRETTY
    # CPUTEMP() JUST RETURNS THE VALUES
    # --------------------------------------
    # Define text colors
    # Define ANSI escape codes for text colors
    reset = "\033[0m"
    red = "\033[31m"
    # Print text in different colors
    # print(f"{red}This text is red{reset}")
    # --------------------------------------
    print(f"{red}1. Check CPU Temperature{reset}")
    # Set the path of the script to be executed
    # The script has a function. State where the script is at to import the function
    script_path = "GetCPUTemperature.py"
    temp_c, temp_f = cpuTemp()
    # --------------------------------------
    print("temp_c = ", temp_c)
    print("temp_f = ", temp_f)
    # --------------------------------------
    # Check if the script exists in the specified path
    print("********************************************\nPress Enter to continue")
    # INPUT JUST WAITS FOR ENTER. ALLOWS FOR A PAUSE
    input()
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------