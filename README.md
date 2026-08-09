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

### Password Breach Check

- SHA-1 Hash Conversion
- HIBP API Call using requets Module
- Proper Error Handling

---

## 📂 Project Structure

```
Password-Security-Toolkit/
│
├── main.py
├── password_audit.py
├── password_generation.py
├── password_breach_search.py
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
- HIBP API call using requests Module

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
- API Calls
- Secure Password Storing Methodologies
---

## 🎯 Learning Goals

The purpose of this project is not only to build a password analyser but also to understand:

- How attackers create password candidates
- Why human-created passwords are predictable
- How password policies improve authentication security
- How to design modular cybersecurity software
- How passwords are found can be found in Data Breaches

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
3) Password Breach Search
4) Exit

Your Choice :
```

## Example Output for option 1) Password Audit
```
┌──(kali㉿kali)-[~/Documents/Projects/Password_Security_Toolkit]
└─$ python3 main.py

=== Password Security Toolkit v1.0 ===

Welcome to Password Security Toolkit!
A Strong Password can be a reason why your account will not be hijacked in Future...

Choose what tool to continue with :
1) Password Audit
2) Password Generation
3) Password Breach Search
4) Exit

Your Choice : 1
Enter Your Password Here for an Audit: 

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
3) Password Breach Search
4) Exit

Your Choice : 4
Exiting...

```

---

## Example Output for Option 2) Password Generation

```
┌──(kali㉿kali)-[~/Documents/Projects/Password_Security_Toolkit]
└─$ python3 main.py

=== Password Security Toolkit v1.0 ===

Welcome to Password Security Toolkit!
A Strong Password can be a reason why your account will not be hijacked in Future...

Choose what tool to continue with :
1) Password Audit
2) Password Generation
3) Password Breach Search
4) Exit

Your Choice : 2

======================================================================================================================================================
                                                            PASSWORD GENERATION TOOL
======================================================================================================================================================

Input the No. of characters of the password (8-16): 12

--------------------------------------------------

Here is Your Secure Password: {~n$r6pY@pMt 

--------------------------------------------------

======================================================================================================================================================
                                                            PASSWORD AUDIT REPORT
======================================================================================================================================================

Password length        : 12 Characters
Password Score         : 5 / 5
Theoretical Entropy    : 78.66
Entropy Rating         : Very Strong

----------------------------------------------------------------------------------------------------
Attack Pattern Analysis

Dictionary Word             : Not Found
Sequential Numbers          : Not Found
Repeated Blocks             : Not Found
Keyboard Walks              : Not Found
Alphabetical Sequence       : Not Found

Estimated Crack time : 758956.0 years
(This estimation is according to number of guesses mordern GPUs can make per seconds (i.e. 100 billion) if an attacker trys to crack password offline.)

----------------------------------------------------------------------------------------------------
Risk Assessment

Low Security risks, 
This password is Consistent with the modern password guidance and NIST guidelines.

----------------------------------------------------------------------------------------------------
Recommendations

No Recommendations

======================================================================================================================================================


Choose what tool to continue with :
1) Password Audit
2) Password Generation
3) Password Breach Search
4) Exit

Your Choice : 4
Exiting...
```
---

## Example Output for Option 3) Password Breach Search

```
┌──(kali㉿kali)-[~/Documents/Projects/Password_Security_Toolkit]
└─$ python3 main.py

=== Password Security Toolkit v1.0 ===

Welcome to Password Security Toolkit!
A Strong Password can be a reason why your account will not be hijacked in Future...

Choose what tool to continue with :
1) Password Audit
2) Password Generation
3) Password Breach Search
4) Exit

Your Choice : 3
Enter your Password to check if it is present in past Data Breaches: 

Alert! This password is found 881 in previous Data Breaches. Change it Immediately!


Choose what tool to continue with :
1) Password Audit
2) Password Generation
3) Password Breach Search
4) Exit

Your Choice : 4
Exiting...
```

---

## Screenshots
### Main Menu
<img width="1365" height="719" alt="1" src="https://github.com/user-attachments/assets/3d04eba1-f757-45f3-9b1a-b03b424649f6" />
### Option 1) Password Audit Preview
<img width="1365" height="720" alt="2" src="https://github.com/user-attachments/assets/0d2b349e-95c0-4134-81bf-57318d53e395" />
### Option 2) Password Generation Preview
<img width="1365" height="719" alt="3" src="https://github.com/user-attachments/assets/7f3c7583-da8e-4bae-996c-2085a42f2944" />
### Option 3) Password Breach Check Preview
<img width="1365" height="722" alt="4" src="https://github.com/user-attachments/assets/d0cbf22a-8768-4b64-86b5-f2a674c2524e" />
