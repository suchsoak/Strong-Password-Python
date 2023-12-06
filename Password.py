import random
import string
import requests
import hashlib
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
V.1.0.2                   

[1] Strong
[2] Weak
[3] Have i been pwned

....................~~...~. .. 
........... .. .~.....  . +~   
......... ....~.~. ........~.  
...... . ......  ......... .   
......~~~~.~~~~......... .~. . 
....~~~~~~~~~..~~~~~~  ... . . 
..~~~+~~~~~.~~~~~+oooo++~.....
~~~~~~~~~.~.~~~+++ooooo++.....
..~~~~~~~.~~+~+++ooo+++~......
... . ..~~~+++++oo+++.........
.....  . .++++ooo+~. .........
........ . .~++~.. ...........
........... .~.. .............
'''

print(password1)
print(Style.RESET_ALL)

class password():
    try:
        colorama.init()
        print(Fore.RED)
        Type = input('Strong, Weak or Have i been pwned: ')
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
            print("\t")
            print("Have I Been Pwned")
            Password = Password
            hash_password = hashlib.sha1(Password.encode('utf-8')).hexdigest().upper()
            url = f"https://api.pwnedpasswords.com/range/{hash_password[:5]}"
            req = requests.get(url)
            hashes = req.text.split('\n')
            pwned = False
            for hash in hashes:
                if hash.startswith(hash_password[5:]):
                    pwned = True
                    break
            if pwned:
                print("[!] Yes, your password has been pwned.")
            else:
                print("[!] No, your password has not been pwned.")
            time.sleep(2)
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
                            print("Have I Been Pwned")
                            print("\t")
                            Password = Password
                            hash_password = hashlib.sha1(Password.encode('utf-8')).hexdigest().upper()
                            url = f"https://api.pwnedpasswords.com/range/{hash_password[:5]}"
                            req = requests.get(url)
                            hashes = req.text.split('\n')
                            pwned = False
                            for hash in hashes:
                                if hash.startswith(hash_password[5:]):
                                    pwned = True
                                    break
                            if pwned:
                                print("[!] Yes, your password has been pwned.")
                            else:
                                print("[!] No, your password has not been pwned.")
                            time.sleep(2)
                            results = zxcvbn(Password, user_inputs=['John', 'Smith'])
                            time.sleep(1)
                            formatted_results = json.dumps(results, indent=4, sort_keys=True, default=str)
                            time.sleep(1)
                            print(formatted_results)
                            print()
        elif Type == '3':
            colorama.init()
            print(Fore.BLUE)
            have = '''
            /\   /\                       __ ___                                                            ___
            /  |_|  \_____  ___  __ ____  |__|\_ |__   ____   ____   ____  ______ __  _  __ ____   ____   __| _/
            /         \__  \ \  \/ // __ \ |  | | __ \_/ __ \_/ __ \ /    \ \____ \\ \/ \/ //    \_/ __ \ / __ | 
            \    _    // __ \_\   /\  ___/_|  | | \_\ \  ___/_  ___/_   |  \|  |_\ \\     /|   |  \  ___/_ /_/ | 
            \  | |  /(____  / \_/  \___  /|__| |___  /\___  /\___  /___|  /|   ___/ \/\_/ |___|  /\___  /____ | 
            \/   \/      \/           \/          \/     \/     \/     \/ |__|                \/     \/     \/ 
            '''
            print(have)
            print(Style.RESET_ALL)
            leak = input("Put your PASSWORD:" )
            colorama.init()
            print(Fore.RED)
            print("Have I Been Pwned")
            print("\t")
            Password = leak
            hash_password = hashlib.sha1(Password.encode('utf-8')).hexdigest().upper()
            url = f"https://api.pwnedpasswords.com/range/{hash_password[:5]}"
            req = requests.get(url)
            hashes = req.text.split('\n')
            pwned = False
            for hash in hashes:
                if hash.startswith(hash_password[5:]):
                    pwned = True
                    break
            if pwned:
                print("[!] Yes, your password has been pwned.")
            else:
                print("[!] No, your password has not been pwned.")
            print(Style.RESET_ALL)
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
