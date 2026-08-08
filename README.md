# Password Security Toolkit

A Python-based cybersecurity toolkit that audits passwords from an attacker's perspective by combining password strength analysis, entropy calculation, pattern recognition, and crack-time estimation.

Unlike traditional password strength checkers, this toolkit explains **why** a password is weak and provides practical recommendations based on modern password security principles.

This project is being developed incrementally to learn authentication security, password attacks, and secure software engineering.

---

## ✨ Features

### Password Audit

- Password Strength Scoring
- Password Complexity Analysis
- Dictionary Word Detection
- Common Password Detection
- Sequential Number Detection
- Repeated Block Detection
- Keyboard Walk Detection
- Alphabetical Sequence Detection
- Password Entropy Calculation
- Offline Password Crack Time Estimation
- Risk Assessment Engine
- NIST-inspired Security Guidance
- Password Improvement Recommendations

### Password Generation

- Cryptographically Secure Password Generation
- Automatic Password Audit
- Guaranteed Character Diversity

---

## 📂 Project Structure

```
Password-Security-Toolkit/
│
├── main.py
├── password_audit.py
├── password_generation.py
├── data/
│   ├── common_passwords.txt
│   └── keyboard_walks.txt
└── README.md
```

---

## 🛠 Technologies Used

- Python 3.14+
- secrets (Cryptographically Secure Random Number Generator)
- math
- pathlib
- subprocess
- String Processing
- Pattern Recognition Algorithms
- Modular Programming

---

## Cybersecurity Concepts Covered

This project is designed as a learning journey through modern password security concepts, including:

- Password Composition
- Dictionary Attacks
- Password Spraying
- Rule-Based Attacks
- Hybrid Attacks
- Pattern Recognition
- Keyboard Walks
- Authentication Security

---

## 🎯 Learning Goals

The purpose of this project is not only to build a password analyser but also to understand:

- How attackers create password candidates
- Why human-created passwords are predictable
- How password policies improve authentication security
- How to design modular cybersecurity software

---

## How to install

Step 1: Clone the Repository

```
$ git clone https://github.com/arshshukla99/Password_Security_Toolkit
```

Step 2: Navigate to the Folder

```
$ cd Password_Security_Toolkit
```

Step 3: Run the script

```
$ python3 main.py
```

---
### You should see main menu like this
```
=== Password Security Toolkit v1.0 ===

Welcome to Password Security Toolkit!
A Strong Password can be a reason why your account will not be hijacked in Future...

Choose what tool to continue with :
1) Password Audit
2) Password Generation
3) Exit

Your Choice :
```

## Example Output for option 1) Password Audit
```
┌──(kali㉿kali)-[~/Documents/Projects/Password_Security_Toolkit]
└─$ python3 main.py

=== Password Security Toolkit v0.7 ===

Welcome to Password Security Toolkit!
A Strong Password can be a reason why your account will not be hijacked in Future...

Choose what tool to continue with :
1) Password Audit
2) Password Generation
3) Exit

Your Choice : 1
Enter Your Password Here for an Audit: Superman@0381

======================================================================================================================================================
                                                            PASSWORD AUDIT REPORT
======================================================================================================================================================

Password length        : 13 Characters
Password Score         : 5 / 5
Theoretical Entropy    : 85.21
Entropy Rating         : Very Strong

----------------------------------------------------------------------------------------------------
Attack Pattern Analysis

Dictionary Word             : Found --> 'superman'
Sequential Numbers          : Not Found
Repeated Blocks             : Not Found
Keyboard Walks              : Not Found
Alphabetical Sequence       : Not Found

Estimated Crack time : 71341903.0 years
(This estimation is according to number of guesses mordern GPUs can make per seconds (i.e. 100 billion) if an attacker trys to crack password offline.)

----------------------------------------------------------------------------------------------------
Risk Assessment

This password is consistent with the modern password guidance but still contains limitations that does not align with the NIST Password Guidance.
Consider Resolving the limitations by mitigations mentioned below.

---------------------------------------------------------------------------
NIST Password Guidance

• Use passwords of at least 12–16 characters.
• Prefer randomly generated passwords.
• Use a unique password for every account.
• Avoid dictionary words and predictable patterns.

----------------------------------------------------------------------------------------------------
Recommendations

None

======================================================================================================================================================


Do you want to Audit Another Password ?
Enter your Choice (Y/N) : n

Choose what tool to continue with :
1) Password Audit
2) Password Generation
3) Exit

Your Choice : 3
Exiting...

```

---

## Example Output for Option 2) Password Generation

```
┌──(kali㉿kali)-[~/Documents/Projects/Password_Security_Toolkit]
└─$ python3 main.py

=== Password Security Toolkit v0.7 ===

Welcome to Password Security Toolkit!
A Strong Password can be a reason why your account will not be hijacked in Future...

Choose what tool to continue with :
1) Password Audit
2) Password Generation
3) Exit

Your Choice : 2

======================================================================================================================================================
                                                            PASSWORD GENERATION TOOL
======================================================================================================================================================

Input the No. of characters of the password : 13

--------------------------------------------------

Here is You Secure Password : g8IxBn.7ad4\O 

--------------------------------------------------

======================================================================================================================================================

Choose what tool to continue with :
1) Password Audit
2) Password Generation
3) Exit

Your Choice : 3
Exiting...
```
---

## 🚀 Future Plans

- Password Policy Auditor (NIST SP 800-63B)
- Export Reports (PDF / HTML)
- Password History Comparison
- GUI Version
- Unit Testing
