"""
Start date: March, 11th, 2020
Autor: Tomas Elbert
This is a simple utility to show system's specs.
"""
import platform
import psutil
print("PySystem Info Utility v1.0")
print("Hello, here is some of your system's specs")
print("====================")
# System info
system_name= platform.system() # OS Name
system_release= platform.release() # Current version installed
system_version= platform.version()
system_processor= platform.processor() # Basic platform info
system_architecture= platform.architecture() # System's architecture
system_machine= platform.machine() # System type
print("OS installed: ",system_name)
print("Current version installed: ",system_release)
print(system_version)
print("Processor basic info: ",system_processor)
print("OS Architecture: ",system_architecture)
print("System Type: ",system_machine)
print("====================")
# CPU Info
# Por cada tipo de dato que deseamos recabar uso una variable diferente
print("Specific info about processor and cores:")
cpu_freq = psutil.cpu_freq() # Max, min and current frequency
cpu_count = psutil.cpu_count() # Number of cores
cpu_percent = psutil.cpu_percent() # General CPU usage percentage
cpu_stats = psutil.cpu_stats() # Advanced info about processor
print("Max CPU Frequency: ",cpu_freq.max, "Mhz")
print("Min CPU Frequency: ",cpu_freq.min, "Mhz")
print("Current CPU Frequency: ",cpu_freq.current, "Mhz")
print("Total physical cores: ", psutil.cpu_count(logical=False)) # logical=False especifica que solo se tomen en cuenta los núcleos físicos
print("Total logical cores: ", psutil.cpu_count(logical=True)) # logical=True especifica que se tomen en cuenta tambien los núcleos lógicos
print("Advanced Info:")
print("CPU usage percentage: ", cpu_percent,"%")
print("CTX Switches: ", cpu_stats.ctx_switches)
print("Interruptions: ", cpu_stats.interrupts)
print("Soft Interruptions: ", cpu_stats.soft_interrupts)
print("System calls: ", cpu_stats.syscalls)
print("====================")
# Memory & Swap Stats
print("RAM and swap info")
virtual_memory= psutil.virtual_memory() # Total RAM, used RAM and free RAM
swap_memory= psutil.swap_memory() # Total swap, and used swap
print("Total RAM: ",virtual_memory.total/1048576, "MB")
print("Free RAM: ", virtual_memory.available/1048576, "MB")
print("Used RAM: ", virtual_memory.used/1048576, "MB")
print("Total swap: ", swap_memory.total/1048576, "MB")
print("Used swap: ", swap_memory.used/1048576, "MB")
print("====================")
# Storage Info
print("Storage Info")
disks= psutil.disk_partitions(all=False) # Only system's partitions
disks_usage= psutil.disk_usage('/') # Total, used and free space
print("Total storage: ", disks_usage.total/1048576, "MB")
print("Used storage: ", disks_usage.used/1048576,"MB")
print("Free storage: ", (float(disks_usage.total))-(float(disks_usage.used)), "MB")
