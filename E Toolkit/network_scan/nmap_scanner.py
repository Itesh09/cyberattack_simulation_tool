# network_scan/nmap_scanner.py
import os

def run_nmap_scanner():
    print("\n=== Nmap Network Scanner ===")
    print("1. Normal Scan")
    print("2. Stealth Scan")
    print("3. Full Scan")
    choice = input("Select a scan type (1-3): ")

    target = input("Enter target IP or hostname: ")

    if choice == "1":
        os.system(f"nmap {target}")
    elif choice == "2":
        os.system(f"nmap -sS {target}")
    elif choice == "3":
        os.system(f"nmap -A -T4 {target}")
    else:
        print("Invalid choice.")
