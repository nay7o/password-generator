import os, platform
os_user = platform.system()
if os_user == "Windows":
    os.system('py get-pip.py')
    os.system('pip install pyperclip')
elif os_user == "Linux":
    os.system('sudo apt install python3-full')
    os.system('sudo apt install python3-pip')
    os.system('pip install pyperclip --break-system-packages')
elif os_user == "Darwin":
    os.system('python get-pip.py')
    os.system('pip3 install pyperclip')
else:
    input("error: the program didn't detect a valid os, press enter to quit")
    quit()