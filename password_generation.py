import string
import secrets
from password_audit import pass_audit

print('\n'+"="*150)
print(" "*60 +"PASSWORD GENERATION TOOL")
print("="*150 + '\n')

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
unichar = string.punctuation
f_lower = False
f_upper = False
f_digit = False
f_unichar = False

allchar = upper + lower + digit + unichar
choice = 0

while True:
    try:
        choice = int(input("Input the No. of characters of the password Starting from 8 to 16 : "))
        
        if choice < 8 or choice > 16:
            print("\nThe Password should be in between 8 to 16 characters :/\n")

        else:
            password = ""
        
            for i in range(choice):
                random = secrets.choice(allchar)
                password += random

            for i in lower:
                if i in password:
                    f_lower = True
            for j in upper:
                if j in password:
                    f_upper = True
            for k in digit:
                if k in password:
                    f_digit = True
            for l in unichar:
                if l in password:
                    f_unichar = True

            if f_lower and f_upper and f_digit and f_unichar:
                print('\n'+ '-'*50+'\n')
                print("Here is You Secure Password :",password,'\n')
                print('-'*50 +'\n')
                pass_audit(password)
                break

            else:
                continue
    except:
        print("\nError : Enter Numbers Only!\n")
