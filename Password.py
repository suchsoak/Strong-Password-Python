# Copyright 2023 suchsoak

# The simple random password with python
# https://texteditor.com/multiline-text-art/

import random
import string
import time
import json
import colorama
from colorama import Fore, Style
from zxcvbn import zxcvbn

colorama.init()
print(Fore.RED)
print("   _ \\                                                |        ___|  |                              ")
print(" |   |  _` |   __|   __| \\ \\  \\   /   _ \\    __|   _` |      \\___ \\  __|   __|   _ \\   __ \\    _  | ")
print(" ___/  (   | \\__ \\ \\__ \\  \\ \\  \\ /   (   |  |     (   |            | |    |     (   |  |   |  (   | ")
print("_|    \\__._| ____/ ____/   \\_/\\_/   \\___/  _|    \\__._|      _____/ \\__| _|    \\___/  _|  _| \\__. | ")
print("                                                                                             |___/  ")
class by():    
    print('\n')
    print('\t\t\t\t\t''BY: ~#M?x')
    print('\t\t\t\t\t''GitHub:','https://github.com/suchsoak','\n')
class password():
    try:
        Type = input('Strong or Weak Passwords: ')
        print(Style.RESET_ALL)
        if Type == "Strong" or Type == "strong":
            print('--------------')
            print('[!] strong')
            print('--------------')
            print('\n')
            words = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
            Quantity = input('Quantity: ')
            time.sleep(0.2)
            Password = "".join(random.choices(words, k=int(Quantity)))
            print('\n')
            print('-----------------')
            print('[!] Your STRONG password: ', '|', Password, '|')
            print('-----------------')
            print('\n')
            print("[*] Your Password is saven in: password.txt")
            with open("password.txt", 'w') as file:
              file.write("[*] Your STRONG Password: \t" + Password)
            colorama.init()
            print(Fore.RED)
            print("\n")
            print("[*] Information about your password:")
            print("\t")
            results = zxcvbn(Password, user_inputs=['John', 'Smith'])
            formatted_results = json.dumps(results, indent=4, sort_keys=True, default=str)
            print(formatted_results)

        elif Type == "Weak" or Type == "weak":
                            print('--------------')
                            print('[!] Weak')
                            print('--------------')
                            print('\n')
                            words = string.ascii_lowercase + string.ascii_uppercase
                            Quantity = input('Quantity: ')
                            Password = "".join(random.choices(words, k=int(Quantity)))
                            print('\n')
                            print('-----------------')
                            print('[!] your weak password: ', '|', Password, '|')
                            print('-----------------')
                            print('\n')
                            print("[*] Your Password is saven in: password.txt")
                            print('\n')
                            with open("password.txt", 'w') as file:
                                file.write("[*] Your Weak Password: \t" + Password) 
                            print("\n")
                            print("[*] Information about your password:")
                            print("\t")
                            colorama.init()
                            print(Fore.RED)
                            results = zxcvbn(Password, user_inputs=['John', 'Smith'])
                            formatted_results = json.dumps(results, indent=4, sort_keys=True, default=str)
                            print(formatted_results)
                            print()
    except KeyboardInterrupt:
        print('program stopped')
    except Exception as error:
         print(error)
