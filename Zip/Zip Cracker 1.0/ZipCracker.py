# imports
import zipfile
import os

zipName = input("[*] Zip: ")
pwdsFile = input("[*] Password File: ")

if os.path.exists(zipName):
    if os.path.exists(pwdsFile):
        with open(pwdsFile,'rb') as text:
            for entry in text.readlines():
                password = entry.strip()
                with zipfile.ZipFile(zipName,'r') as zf:
                    try:
                        zf.extractall(pwd=password)

                        print("\n[+] Password Found!")

                        data = zf.namelist()[0]
                        print("Data: " + str(data))

                        data_size = zf.getinfo(data).file_size
                        print("Data Size: " + str(data_size))

                        print("Password: " + password.decode("utf-8"))

                        break
                    except:
                        print("[-] Password Not Found! - " + password.decode("utf-8"))
                    pass
    else:
        print("[-] Password File Not Found!")
else:
    print("[-] Zip File Not Found!")