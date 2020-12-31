#!/bin/python3

import os
from colorama import Fore

print(Fore.RED)
print("""╭━━━╮          
         ┃╭━╮┃          
         ┃┃╱┃┣╮╭┳━━┳━━╮ 
         ┃┃╱┃┃╰╯┃╭╮┃╭╮┃ 
         ┃╰━╯┃┃┃┃╭╮┃╰╯┃ 
         ╰━━╮┣┻┻┻╯╰┫╭━╯ 
         ╱╱╱╰╯╱╱╱╱╱┃┃   
         ╱╱╱╱╱╱╱╱╱╱╰╯   """)
print("/Speed//up your nmap")

def menu():
    print(Fore.CYAN)
    print()
    print("Type [1] for local-network scan")
    print("Type [2] for webpage scan")
    print("Type [3] to scan a single host")
    print()
    print("Type [4] to exit")
    print()
    choice = input()

    if choice == '1':
        menu1()
    
    if choice == '2':
        menu2()

    if choice == '3':
        menu3()

    if choice == '4':
        exit()

def menu1():
    print(Fore.CYAN)
    print("Type [1] For:")
    print("Quick scan all divices on local 192.168.0.0/24")
    print()
    print("Type [2] For:")
    print("Quick scan all divices on local 10.0.0.0/24")
    print()
    print("Type [3] to go back")
    print()
    choice1 = input()

    if choice1 == '1':
        print()
        print(Fore.CYAN)
        print("[Scanning local-network]")
        attack1 = os.system("nmap -sn 192.168.0.0/24")

    if choice1 == '2':
        print()
        print(Fore.CYAN)
        print("[Scanning local-network]")
        attack1 = os.system("nmap -sn 10.0.0.0/24")

    if choice1 == '3':
        menu()
    
    menu1()

def menu2():
    print()
    print(Fore.CYAN)
    print("Type [1] to scan webpage")
    print("Type [2] to scan webpage with Anonymity On")
    print("Type [3] to go back")
    print()
    choice2 = input()

    if choice2 == '1':
        print()
        print(Fore.CYAN)
        page = str(input("Add webpage url: "))
        print("[Scanning wbepage]")
        attack2 = os.system(f"nmap -T5 -A {page}")

    if choice2 == '2':
        print()
        print("This option takes...")
        print(Fore.CYAN)
        page = str(input("Add webpage url: "))
        print("[Scanning webpage]")
        attack2 = os.system(f"nmap -T1 -d -A {page}") 

    if choice2 == '3':
        menu()
    
    menu2()

def menu3():
    print()
    print(Fore.CYAN)
    print("Type [1] to scan single-host")
    print("Type [2] to scan single-host with Anonymity On")
    print("Type [3] to go back")
    print()
    choice3 = input()

    if choice3 == '1':
        print()
        print(Fore.CYAN)
        host = str(input("Add host ip: "))
        print("[Scanning host ip]")
        attack3 = os.system(f"nmap -T5 -A {host}")

    if choice3 == '2':
        print()
        print("This option takes longer...")
        print(Fore.CYAN)
        host = str(input("Add host ip: "))
        print("[Scanning host ip]")
        attack3 = os.system(f"nmap -T1 -d -A {host}")

    if choice3 == '3':
        menu()
    menu3()
    
menu() 
