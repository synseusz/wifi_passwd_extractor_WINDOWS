import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').replace("\r", "").split('\n')
print(data[7])
print(data[8])
wifis = [line.split(':') for line in data if "All User Profile" in line]
wifi = [wifi[1] for wifi in wifis]
print(wifi)
