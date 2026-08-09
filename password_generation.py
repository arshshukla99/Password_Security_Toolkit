import string
import secrets
from password_audit import pass_audit

print('\n' + "="*150)
print(" "*60 + "PASSWORD GENERATION TOOL")
print("="*150 + '\n')

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
unichar = string.punctuation

allchar = upper + lower + digit + unichar

while True:
    try:
        choice = int(input("Input the No. of characters of the password (8-16): "))
        
        if choice < 8 or choice > 16:
            print("\nThe Password should be between 8 and 16 characters :/\n")
            continue

        while True:
            password = ""
            
            for _ in range(choice):
                random = secrets.choice(allchar)
                password += random

            f_lower = False
            for i in lower:
                if i in password:
                    f_lower = True

            f_upper = False
            for j in upper:
                if j in password:
                    f_upper = True

            f_digit = False
            for k in digit:
                if k in password:
                    f_digit = True

            f_unichar = False
            for l in unichar:
                if l in password:
                    f_unichar = True

            if f_lower and f_upper and f_digit and f_unichar:
                print('\n' + '-'*50 + '\n')
                print("Here is Your Secure Password:", password, '\n')
                print('-'*50 + '\n')
                pass_audit(password)
                break

        break

    except ValueError:
        print("\nError: Enter numbers only!\n")
