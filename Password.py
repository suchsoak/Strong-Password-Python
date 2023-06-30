import random
import string
import time
import colorama
from colorama import Fore, Style
# The simple random password with python
# Password = https://texteditor.com/multiline-text-art/
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
    except KeyboardInterrupt:
        print('program stopped')
    except Exception as error:
         print(error)
