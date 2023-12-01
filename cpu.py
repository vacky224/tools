import psutil
import os
def print_cpu_info():
    # Get CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")

processes = []
for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
       		 processes.append({
		'pid': process.info['pid'],
		'name': process.info['name'],
		'cpu_percent': process.info['cpu_percent']
        			})
print("\nRunning Processes:")
print("{:<10} {:<20} {:<15}".format('PID', 'Name', 'CPU Percent'))
print("=" * 45)
for process in processes:
        print("{:<10} {:<20} {:<15}".format(process['pid'], process['name'], process['cpu_percent']))
memory = psutil.virtual_memory()
BOLD = "\033[1m"
RESET = "\033[0m"
text_to_print = "Let us look at the Statistics"
result = os.popen("hostname -f").read().strip()
print(BOLD + result + RESET)
print("The hostname of this machine is:", result, BOLD + RESET)
print(BOLD + text_to_print + RESET)
print("=" * 45)
print("Now let us find the Memory Space too")
print(f"Total Memory: {memory.total} bytes")
print(f"Used Memory: {memory.used} bytes")
print(f"Free Memory: {memory.free} bytes")

print("=" * 45)
print("Now let us find the Hard Disk Space too")
disk_usage = psutil.disk_usage('/')

print(f"Total Disk Space: {disk_usage.total} bytes")
print(f"Used Disk Space: {disk_usage.used} bytes")
print(f"Free Disk Space: {disk_usage.free} bytes")
print(f"Disk Space Usage Percentage: {disk_usage.percent}%")
print("=" * 45)

if __name__ == "__main__":
    print_cpu_info()
