import random
import string
import time
# The simple random password with python
print("   _ \\                                                 |        ___|  |                              ")
print(" |   |  _` |   __|   __| \\ \\  \\   /   _ \\    __|   _` |      \\___ \\  __|   __|   _ \\   __ \\    _  | ")
print(" ___/  (   | \\__ \\ \\__ \\  \\ \\  \\ /   (   |  |     (   |            | |    |     (   |  |   |  (   | ")
print("_|    \\__._| ____/ ____/   \\_/\\_/   \\___/  _|    \\__._|      _____/ \\__| _|    \\___/  _|  _| \\__. | ")
print("                                                                                             |___/  ")
    
print('BY: ~#M?x')
print('GitHub:','https://github.com/suchsoak','\n')
class password():
    Type = input('Strong or Weak Passwords: ')
    try:
        if Type == 'Strong' or 'strong':
            words = string.ascii_lowercase + string.digits + string.punctuation
            Quantity = input('Quantity: ')
            time.sleep(0.2)
            Password = "".join(random.choices(words, k=int(Quantity)))
            print('-----------------')
            print('Your Password: ', Password)
            print('-----------------')
        elif Type == 'Weak' or 'weak':
                words = string.ascii_lowercase 
                Quantity = input('Quantity: ')
                Password = "".join(random.choices(words, k=int(Quantity)))
                print('-----------------')
                print('your password: ', Password())
                print('-----------------')
    except KeyboardInterrupt:
        print('Programa interrompido!')
    except Exception as error:
         print(error)
   

         
