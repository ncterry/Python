'''
Monitoring the temperature of CPU and other hardware sensors: 
You can use the py3nvml library to access NVIDIA GPU information (if available) 
or the wmi library for general hardware information. To install these libraries, 
run pip install py3nvml wmi in your terminal or command prompt.

Note: Accessing temperature information might not be supported on all systems. 
You may need to use third-party tools or libraries that are specific to your hardware.
EXAMPLE
tempC, tempF = cpuTemperature()
print(f"CPU temperature:", tempC,  "°C")
print(f"CPU temperature:", tempF,  "°F")
'''
import wmi
def cpuTemp():
    w = wmi.WMI(namespace="root\\wmi")
    temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
    
    tempC = (temperature_info.CurrentTemperature / 10 - 273.15)
    tempF = (temperature_info.CurrentTemperature / 10 - 273.15) * (9/5) + 32

    return tempC, tempF
# END def cpuTemperature():
