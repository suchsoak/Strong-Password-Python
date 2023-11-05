# Strong Password With Python
[![Update](https://github.com/suchsoak/Strong-Password-Python/actions/workflows/main.yml/badge.svg)](https://github.com/suchsoak/Strong-Password-Python/actions/workflows/main.yml)

The strong random password with python.

When running the script, you will have the option to choose the letter count and even whether it will be a weak or strong password.

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
  **You will choose [1] Strong or [2] Weak**

<p align="center">
  <img src="https://github.com/suchsoak/Strong-Password-Python/blob/main/passwordpy.png" alt="passwordpy.png">
</p>

```sh
 Strong or Weak Passwords:
```

You will choose the number of words

```sh
 __________                                                ___
\______   \____    ______ _______  _  __ ____ _______  __| _/
 |     ___/__  \  /  ___//  ___/ \/ \/ // __ \_  __ \/ __ | 
 |    |    / __ \_\___ \ \___ \ \     /(  \_\ )|  | \/ /_/ | 
 |____|   (____  /____  \____  \ \/\_/  \____/ |__|  \____ | 
               \/     \/     \/                           \/ 
BY: suchsoak
Github: https://github.com/suchsoak                          
v.1.0.1

[1] Strong
[2] Weak

Strong or Weak Passwords: 1

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
v.1.0.1

[1] Strong
[2] Weak

Strong or Weak Passwords: 1

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

### So that's it, take advantage of your strong passwords. Goodbye.

<br>

| Libraries |  Links |
| ------ | ------ |
| random | https://docs.python.org/3/library/random.html 
| string| https://docs.python.org/3/library/string.html 
| time | https://docs.python.org/3/library/time.html
| zxcvn | https://pypi.org/project/zxcvbn
| Json | https://docs.python.org/3/library/json.html
| colorama | https://pypi.org/project/colorama/)https://pypi.org/project/colorama/
