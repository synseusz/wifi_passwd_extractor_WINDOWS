import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').replace("\r", "").split('\n')
print(data[7])
print(data[8])
wifis = []
for line in data:
    if "All User Profile" in line:
        name = line.split(':')[1]
        wifis.append(name[1:len(name)])


for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', '%s'%(wifi), 'key=clear']).decode('utf-8').replace("\r", "").split('\n')
    passwords_list = [line.split(':')[1] for line in results if "Key Content" in line]
    try:
        print(wifi, " - ", passwords_list[0])
    except:
        print(wifi, " - ", "No password assigned!")

