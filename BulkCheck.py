import os
import time

from pynput.keyboard import Key, Controller
#Runs CMD Command to go to given url in chrome.exe
os.system('cmd /c start chrome https://mxtoolbox.com/SuperTool.aspx')
time.sleep(3)
keyboard = Controller()
#CHANGE FILE PATH PROPER TO YOUR SYSTEM BEFORE START
listOfDomains = open(r"C:\Users\mabus\Desktop\list.txt", 'r').read().split('\n')

for l_num, line in enumerate(listOfDomains):
    domain = line
    # Clears the searchbox before sending input
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    time.sleep(1)
    keyboard.press(Key.backspace)
    time.sleep(1)
    # Types spf: + given domain name into the searchbar and hits enter
    keyboard.type("spf:")
    time.sleep(1)
    keyboard.type(domain)
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(12)
    # Saves the html page in .txt format
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release('s')
    keyboard.release(Key.ctrl)
    time.sleep(1)
    keyboard.type(domain + ".txt")
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(10)
    # CHANGE FILE PATH PROPER TO YOUR SYSTEM BEFORE START
    # Searches file for any SPF Record
    # file1 = open(r"C:\Users\mabus\Desktop\spfrecords" + "\\" + f'{domain}.txt')
    downloadedSPF = open(r"C:\Users\mabus\Desktop\spfrecords" + "\\" + domain + ".txt", 'r')
    for l_no, line in enumerate(downloadedSPF):
        if "No SPF Record" in line:
            print("No SPF Record for domain", domain, "at line", l_no)
            # CHANGE FILE PATH PROPER TO YOUR SYSTEM BEFORE START
            with open(r"C:\Users\mabus\Desktop\NoSPF.txt", 'a') as noSPF:
                noSPF.write(domain + "\n")
            break
        elif "More than one" in line:
            print("More than one SPF record found for domain", domain, "at line", l_no)
            # CHANGE FILE PATH PROPER TO YOUR SYSTEM BEFORE START
            with open(r"C:\Users\mabus\Desktop\MultipleSPFs.txt", 'a') as multipleSPF:
                multipleSPF.write(domain + "\n")
            break
        elif "SPF Record Published" in line:
            print("SPF Record found for", domain, "at line", l_no)
            # CHANGE FILE PATH PROPER TO YOUR SYSTEM BEFORE START
            with open(r"C:\Users\mabus\Desktop\SPFfound.txt", 'a') as validSPF:
                validSPF.write(domain + "\n")
            break