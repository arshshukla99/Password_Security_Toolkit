import string
import secrets

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
unichar = string.punctuation

allchar = upper + lower + digit + unichar

while True:

    choice = int(input("Input the no. of characters of the password you want : "))

    if choice < 8 or choice > 16:
        print("The Password should be in between 8 to 16 characters :/ \n")

    elif choice >= 8 or choice <= 16:
        password = ''
        
        for i in range(choice):
            random = secrets.choice(allchar)
            password += random  

        print(password)
        break
