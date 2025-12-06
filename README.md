# 🔐 Strong Password With Python
[![Update](https://github.com/suchsoak/Strong-Password-Python/actions/workflows/main.yml/badge.svg)](https://github.com/suchsoak/Strong-Password-Python/actions/workflows/main.yml)

Generate strong random passwords with Python easily.

```sh
__________                                                ___
\______   \____    ______ _______  _  __ ____ _______  __| _/
 |     ___/__  \  /  ___//  ___/ \/ \/ // __ \\_  __ \/ __ | 
 |    |    / __ \_\___ \ \___ \ \     /(  \_\ )|  | \/ /_/ | 
 |____|   (____  /____  \____  \ \/\_/  \____/ |__|  \____ | 
               \/     \/     \/                           \/ 
```

**Choose the password length and strength level, then check if it's been compromised on Have I Been Pwned.**

>[!NOTE]
>✅ Your password is automatically saved to `password.txt` so you won't forget it.

## 📥 Installation

```sh
git clone https://github.com/suchsoak/Strong-Password-Python.git
pip install -r requirements.txt  
```

## 🚀 Usage

```sh
python3 Password.py
```

>[!IMPORTANT]
>⚠️ You need `hashlib` and `requests` installed to run this script.

### Menu Options
Choose one of the following:
- **[1]** Strong Password
- **[2]** Weak Password
- **[3]** Email Check (API)
- **[4]** Email Hash Check
- **[5]** Company Breach Check
- **[6]** Have I Been Pwned

## 📊 zxcvbn Information

| Field | Description |
|-------|-------------|
| `score` | Password strength (0-4) |
| `guesses` | Estimated guesses to crack |
| `crack_times_display` | Human-readable crack times |
| `feedback` | Improvement suggestions |

## 📧 Email Tools

### 🔍 Email API Check
Verify if your email was leaked (requires API key from haveibeenpwned.com)

### 🔗 Email Hash Check
Check without API key using SHA1 hash method

## 🏢 Company Breach Check
Search if a company's data was breached (e.g., Sony, Adobe)

## 📋 License & Libraries

**MIT License** © 2025 ~#M?x

| Library | Purpose |
|---------|---------|
| `random`, `string` | Password generation |
| `hashlib`, `requests` | Encryption & API calls |
| `zxcvbn` | Password strength analysis |
| `colorama` | Terminal colors |

