# Password Security Toolkit

A Python-based cybersecurity project that analyses passwords from an attacker's perspective instead of relying only on traditional password strength scoring.

Unlike basic password strength checkers, this toolkit identifies common attack patterns such as dictionary words, sequential numbers, keyboard walks, and repeated blocks while providing recommendations to improve password security.

This project is being developed incrementally to learn authentication security, password attacks, and secure software engineering.

---

## ✨ Features

### Current Features (v0.7)

- Password Strength Scoring
- Password Complexity Analysis
- Dictionary Word Detection
- Common Password Detection
- Sequential Number Detection
- Repeating Block Detection
- Keyboard Walk Detection
- Alphabetical Sequence Detection
- Password Improvement Suggestions
- Password Entropy Calculation
- Risk Assessment Suggestions based on Entropy and Pattern found
- Offline Password Crack Estimation

---

## 🚀 Planned Features

- Secure Password Generator
- Password Audit Reports
- Password Policy Auditor (NIST Guidelines)

See the full development roadmap in **ROADMAP.md**.

---

## 📂 Project Structure

```
Password-Security-Toolkit/
│
├── main.py
├── common_passwords.txt
├── keyboard_walks.txt
├── ROADMAP.md
└── README.md
```

---

## 🛠 Technologies Used

- Python 3.14.6
- File Handling
- String Algorithms
- Pattern Recognition
- Modular Programming
- Math Module

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
$ python3 password_security_toolkit.py
```

---

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
