# main.py
import os
import sys

def display_menu():
    print("\n=== Cyber Attack Simulation Tool ===")
    print("1. Network Scanning (Nmap)")
    print("2. Vulnerability Scanning")
    print("3. XSS Injection")
    print("4. SQL Injection")
    print("5. Packet Sniffing")
    print("6. Brute Force Scanning")
    print("7. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nSelect an option (1-7): ")

        if choice == "1":
            from network_scan.nmap_scanner import run_nmap_scanner
            run_nmap_scanner()
        elif choice == "2":
            from vulnerability_scan.vuln_scanner import run_vuln_scanner
            run_vuln_scanner()
        elif choice == "3":
            from xss_injection.xss_attacker import run_xss_attacker
            run_xss_attacker()
        elif choice == "4":
            from sql_injection.sql_attacker import run_sql_attacker
            run_sql_attacker()
        elif choice == "5":
            from packet_sniffing.packet_sniffer import run_packet_sniffer
            run_packet_sniffer()
        elif choice == "6":
            from brute_force.brute_forcer import run_brute_forcer
            run_brute_forcer()
        elif choice == "7":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()