import random
import string
import time
import json
import colorama
from colorama import Fore, Style
from zxcvbn import zxcvbn

colorama.init()
print(Fore.RED)

password1 ='''
__________                                                ___
\______   \____    ______ _______  _  __ ____ _______  __| _/
 |     ___/__  \  /  ___//  ___/ \/ \/ // __ \\_  __ \/ __ | 
 |    |    / __ \_\___ \ \___ \ \     /(  \_\ )|  | \/ /_/ | 
 |____|   (____  /____  \____  \ \/\_/  \____/ |__|  \____ | 
               \/     \/     \/                           \/ 
BY: suchsoak
Github: https://github.com/suchsoak                          

[1] Strong
[2] Weak

'''

print(password1)
print(Style.RESET_ALL)

class password():
    try:
        colorama.init()
        print(Fore.RED)
        Type = input('Strong or Weak Passwords: ')
        print(Style.RESET_ALL)
        print(Style.RESET_ALL)
        if Type == "1":
            print('--------------')
            print('[!] Strong')
            print('--------------')
            print('\n')
            words = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
            Quantity = input('Quantity: ')
            time.sleep(0.2)
            Password = "".join(random.choices(words, k=int(Quantity)))
            print('\n')
            print('-----------------')
            print('[!] Your STRONG password: ', Password)
            print('-----------------')
            print('\n')
            print("[*] Your Password is saven in: password.txt")
            with open("password.txt", 'w') as file:
              file.write("[*] Your STRONG Password: \t" + Password)
            colorama.init()
            print(Fore.RED)
            time.sleep(2)
            print("\n")
            print("[*] Information about your password:")
            print("\t")
            results = zxcvbn(Password, user_inputs=['John', 'Smith'])
            time.sleep(1)
            formatted_results = json.dumps(results, indent=4, sort_keys=True, default=str)
            time.sleep(1)
            print(formatted_results)
        elif Type == "2":
                            print('--------------')
                            print('[!] Weak')
                            print('--------------')
                            print('\n')
                            words = string.ascii_lowercase + string.ascii_uppercase
                            Quantity = input('Quantity: ')
                            Password = "".join(random.choices(words, k=int(Quantity)))
                            print('\n')
                            print('-----------------')
                            print('[!] your weak password: ',Password)
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
                            time.sleep(2)
                            results = zxcvbn(Password, user_inputs=['John', 'Smith'])
                            time.sleep(1)
                            formatted_results = json.dumps(results, indent=4, sort_keys=True, default=str)
                            time.sleep(1)
                            print(formatted_results)
                            print()
        else:
              colorama.init()
              print(Fore.RED)
              print("You need chosse 1 or 2")
              print(Style.RESET_ALL)
              print()
    except KeyboardInterrupt:
        print('program stopped')
    except Exception as error:
         print(error)
        
