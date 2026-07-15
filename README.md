# Password Security Toolkit

A Python-based cybersecurity project that analyses passwords from an attacker's perspective instead of relying only on traditional password strength scoring.

Unlike basic password strength checkers, this toolkit identifies common attack patterns such as dictionary words, sequential numbers, keyboard walks, and repeated blocks while providing recommendations to improve password security.

This project is being developed incrementally to learn authentication security, password attacks, and secure software engineering.

---

## ✨ Features

### Current Features (v0.4)

- Password Strength Scoring
- Password Complexity Analysis
- Dictionary Word Detection
- Common Password Detection
- Sequential Number Detection
- Repeating Block Detection
- Keyboard Walk Detection
- Alphabetical Sequence Detection
- Password Improvement Suggestions

---

## 🚀 Planned Features

- Password Entropy Calculator
- Password Crack Time Estimation
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

## Example Output
```
┌──(kali㉿kali)-[~]
└─$ git clone https://github.com/arshshukla99/Password_Security_Toolkit
Cloning into 'Password_Security_Toolkit'...
remote: Enumerating objects: 48, done.
remote: Counting objects: 100% (48/48), done.
remote: Compressing objects: 100% (46/46), done.
remote: Total 48 (delta 21), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (48/48), 22.89 KiB | 366.00 KiB/s, done.
Resolving deltas: 100% (21/21), done.
                                                                                                                                                                      
┌──(kali㉿kali)-[~]
└─$ cd Password_Security_Toolkit
                                                                                                                                                                      
┌──(kali㉿kali)-[~/Password_Security_Toolkit]
└─$ python3 password_security_toolkit.py

=== Password Security Toolkit v0.4 ===

Welcome to Password Security Toolkit!
A Strong Password can be a reason why your account will not be Hijacked in Future...

Enter Your Password Here for an Audit: 
```
