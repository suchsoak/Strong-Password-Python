# Strong Password With Python
[![Update](https://github.com/suchsoak/Strong-Password-Python/actions/workflows/main.yml/badge.svg)](https://github.com/suchsoak/Strong-Password-Python/actions/workflows/main.yml)

The strong random password with python.

**When you run the script, you'll have the option to choose the letter count and even whether it will be a weak or strong password and check your password on Have I Been Pwned.**

>[!NOTE]
>So you don't forget your password, I put it in a txt file "password.txt".


# How To Install

> Install with git

```sh
 git clone https://github.com/suchsoak/Strong-Password-Python.git

```
```sh
 pip install -r requirements.txt  
```

# Usage

```sh
 Python3 Password.py
```

>[!IMPORTANT]
>Keep in mind that for it to work you need to install hashlib and requests to work

#### You will choose [1] Strong, [2] Weak, [3] Email (API), [4] Email Hash, [5] Company or [6] Have i been pwned

```sh

__________                                                ___
\______   \____    ______ _______  _  __ ____ _______  __| _/
 |     ___/__  \  /  ___//  ___/ \/ \/ // __ \\_  __ \/ __ | 
 |    |    / __ \_\___ \ \___ \ \     /(  \_\ )|  | \/ /_/ | 
 |____|   (____  /____  \____  \ \/\_/  \____/ |__|  \____ | 
               \/     \/     \/                           \/ 
BY: suchsoak
Github: https://github.com/suchsoak       
V.1.0.3                   

[1] Strong
[2] Weak
[3] Email (API)
[4] Email Hash
[5] Company
[6] Have i been pwned

```
<details>
 
<summary>Password</summary>

## You will choose the number of words

```sh
 __________                                                ___
\______   \____    ______ _______  _  __ ____ _______  __| _/
 |     ___/__  \  /  ___//  ___/ \/ \/ // __ \_  __ \/ __ | 
 |    |    / __ \_\___ \ \___ \ \     /(  \_\ )|  | \/ /_/ | 
 |____|   (____  /____  \____  \ \/\_/  \____/ |__|  \____ | 
               \/     \/     \/                           \/ 
BY: suchsoak
Github: https://github.com/suchsoak                          
v.1.0.3

[1] Strong
[2] Weak
[3] Email (API)
[4] Email Hash
[5] Company
[6] Have i been pwned

Put the namber: 1

--------------
[!] Strong
--------------

Quantity: 20
```


# Information About zxcvbn 

```sh
calc_time: Time taken to calculate the password strength.
crack_times_display: Time estimates to crack the password in different scenarios.
crack_times_seconds: Time estimates to crack the password in seconds.
feedback: Feedback on the password, such as suggestions to improve it.
guesses: Number of guesses required to crack the password.
guesses_log10: Logarithm base 10 of the number of guesses required to crack the password.
password: The password that was evaluated.
score: Password score based on its strength.
sequence: A sequence of tokens (parts) of the password that were individually analyzed.
```

# Example zxcvbn

```sh
{
    'password': 'JohnSmith123',
    'score': 2,
    'guesses': 2567800,
    'guesses_log10': 6.409561194521849,
    'calc_time': datetime.timedelta(0, 0, 5204)
    'feedback': {
        'warning': '',
        'suggestions': [
            'Add another word or two. Uncommon words are better.',
            "Capitalization doesn't help very much"
        ]
    },
    'crack_times_display': {
        'offline_fast_hashing_1e10_per_second': 'less than a second'
        'offline_slow_hashing_1e4_per_second': '4 minutes',
        'online_no_throttling_10_per_second': '3 days',
        'online_throttling_100_per_hour': '3 years',
    },
    'crack_times_seconds': {
        'offline_fast_hashing_1e10_per_second': 0.00025678,
        'offline_slow_hashing_1e4_per_second': 256.78
        'online_no_throttling_10_per_second': 256780.0,
        'online_throttling_100_per_hour': 92440800.0,
    },
    'sequence': [{
        'matched_word': 'john',
        'rank': 2,
        'pattern': 'dictionary',
        'reversed': False,
        'token': 'John',
        'l33t': False,
        'uppercase_variations': 2,
        'i': 0,
        'guesses': 50,
        'l33t_variations': 1,
        'dictionary_name': 'male_names',
        'base_guesses': 2,
        'guesses_log10': 1.6989700043360185,
        'j': 3
    }, {
        'matched_word': 'smith123',
        'rank': 12789,
        'pattern': 'dictionary',
        'reversed': False,
        'token': 'Smith123',
        'l33t': False,
        'uppercase_variations': 2,
        'i': 4,
        'guesses': 25578,
        'l33t_variations': 1,
        'dictionary_name': 'passwords',
        'base_guesses': 12789,
        'guesses_log10': 4.407866583030775,
        'j': 11
    }],
}
 
```

## Example in the script

```sh
__________                                                ___
\______   \____    ______ _______  _  __ ____ _______  __| _/
 |     ___/__  \  /  ___//  ___/ \/ \/ // __ \_  __ \/ __ | 
 |    |    / __ \_\___ \ \___ \ \     /(  \_\ )|  | \/ /_/ | 
 |____|   (____  /____  \____  \ \/\_/  \____/ |__|  \____ | 
               \/     \/     \/                           \/ 
BY: suchsoak
Github: https://github.com/suchsoak                          
v.1.0.3

[1] Strong
[2] Weak
[3] Email (API)
[4] Email Hash
[5] Company
[6] Have i been pwned

Put the namber: 1

--------------
[!] Strong
--------------

Quantity: 20

-----------------
[!] Your STRONG password:  21GJu>*KrjeC{hds"~ca
-----------------

[*] Your Password is saven in: password.txt

[*] Information about your password:
	
{
    "calc_time": "0:00:00.005670",
    "crack_times_display": {
        "offline_fast_hashing_1e10_per_second": "centuries",
        "offline_slow_hashing_1e4_per_second": "centuries",
        "online_no_throttling_10_per_second": "centuries",
        "online_throttling_100_per_hour": "centuries"
    },
    "crack_times_seconds": {
        "offline_fast_hashing_1e10_per_second": "10000000000.0000000001",
        "offline_slow_hashing_1e4_per_second": "10000000000000000.0001",
        "online_no_throttling_10_per_second": "10000000000000000000.1",
        "online_throttling_100_per_hour": "3600000000000000199876.144433"
    },
    "feedback": {
        "suggestions": [],
        "warning": ""
    },
    "guesses": 100000000000000000001,
    "guesses_log10": 20.0,
    "password": "21GJu>*KrjeC{hds\"~ca",
    "score": 4,
    "sequence": [
        {
            "guesses": 100000000000000000000,
            "guesses_log10": 20.0,
            "i": 0,
            "j": 19,
            "pattern": "bruteforce",
            "token": "21GJu>*KrjeC{hds\"~ca"
        }
    ]
}
```
</details>

<details>
 
<summary>Email</summary>

# Email API

### This is a request to find out if your email has been leaked on the dark web, using the Have i Been pwned API. But for that you need the API key

#### Then, You will put the email and your API key

>You need have the API key

```sh
   Put your API key: admin@gmail.com
```
```sh
   Put your API key: 01010.00100.010.101
```

>Part of the script

```sh

 email = input("Put the email:")
                API = input("Put your API key:")
                url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
                headers = {"hibp-api-key": "{API}"}  
```

# Email Hash

#### The `Email hash` it creates a hash of the email you put in and checks if that hash has already been leaked, it's an attempt to use the API for free. But it's not 100% that it will work.

#### It's the same thing you do as option 6 sends a hash that checks whether or not it's already `been leaked`.

>Part of the code

```sh
email_1 = input("Put your Email:" )
            colorama.init()
            print(Fore.RED)
            print("\t")
            Email = email_1
            hash_password = hashlib.sha1(Email.encode('utf-8')).hexdigest().upper()
            url = f"https://api.pwnedpasswords.com/range/{hash_password[:5]}"
            req = requests.get(url)
            hashes = req.text.split('\n')
            pwned = False
            for hash in hashes:
                if hash.startswith(hash_password[5:]):
                    pwned = True
                    break
            if pwned: 
                print("[!] Yes, your email has been pwned.")
            else:
                print("[!] No, your email has not been pwned.")
```

#### If you want see more details

| API |  Link |
| ------ | ------ |
|  haveibeenpwned | https://haveibeenpwned.com/API/v3#BreachModel

</details>

<details>
 
<summary>Company</summary>

# Company

#### This option checks if any information from a company has already been leaked, such as sony.

```sh

Put the number: 5

Put the Company:sony
{"Name":"Sony","Title":"Sony","Domain":"sony.com","BreachDate":"2011-06-02","AddedDate":"2013-12-04T00:00:00Z","ModifiedDate":"2013-12-04T00:00:00Z","PwnCount":37103,"Description":"In 2011, Sony suffered breach after breach after breach &mdash; it was a <em>very</em> bad year for them. The breaches spanned various areas of the business ranging from the PlayStation network all the way through to the motion picture arm, Sony Pictures. A SQL Injection vulnerability in <a href=\"http://www.sonypictures.com\" target=\"_blank\" rel=\"noopener\">sonypictures.com</a> lead to <a href=\"http://www.troyhunt.com/2011/06/brief-sony-password-analysis.html\" target=\"_blank\" rel=\"noopener\">tens of thousands of accounts across multiple systems being exposed</a> complete with plain text passwords.","LogoPath":"https://haveibeenpwned.com/Content/Images/PwnedLogos/Sony.png","DataClasses":["Dates of birth","Email addresses","Genders","Names","Passwords","Phone numbers","Physical addresses","Usernames"],"IsVerified":true,"IsFabricated":false,"IsSensitive":false,"IsRetired":false,"IsSpamList":false,"IsMalware":false,"IsSubscriptionFree":false}
Don't have nothing about this company: sony

```

### Note that for this to work you need to get the curl tool which in turn is already standard for any operating system to get it

```sh
   s.system(f'\ncurl https://haveibeenpwned.com/api/v3/breach/{Company}\n')
```
```sh
   https://haveibeenpwned.com/api/v3/breach/sony
```
```sh
   https://haveibeenpwned.com/api/v3/breach/adobe
```
</details>

<details>
 
<summary>Have i been pwned</summary>

# Have i been pwned

```sh

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
```

### You can now put an option to verify a specific password of yours that you may or may not have already leaked on the dark web

```sh

Put the namber: 6

                                              ___
            ______ __  _  __ ____   ____   __| _/
            \____ \\ \/ \/ //    \_/ __ \ / __ | 
            |  |_\ \\     /|   |  \  ___/_ /_/ | 
            |   ___/ \/\_/ |___|  /\___  /____ | 
            |__|                \/     \/     \/ 


Put your PASSWORD:

```
</details>
	
### So that's it, take advantage of your strong passwords. Goodbye.

License & Copyright
-----------------------
MIT License Copyright (c) 2024 ~#M?x


| Libraries |  Links |
| ------ | ------ |
| random | https://docs.python.org/3/library/random.html 
| string| https://docs.python.org/3/library/string.html 
| time | https://docs.python.org/3/library/time.html
| zxcvn | https://pypi.org/project/zxcvbn
| Json | https://docs.python.org/3/library/json.html
| colorama | https://pypi.org/project/colorama/)https://pypi.org/project/colorama/
| requests | https://pypi.org/project/requests/
| hashlib  | https://docs.python.org/3/library/hashlib.html 
| OS  | https://docs.python.org/3/library/os.html
| Have I Been Pwned  | https://haveibeenpwned.com/API/Key
