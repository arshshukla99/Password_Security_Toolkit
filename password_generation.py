import string
import secrets

print('\n'+"="*150)
print(" "*60 +"PASSWORD GENERATION TOOL")
print("="*150 + '\n')

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
unichar = string.punctuation

allchar = upper + lower + digit + unichar
choice = 0

while True:
    try:
        choice = int(input("Input the No. of characters of the password : "))
        
        if choice < 8 or choice > 16:
            print("\nThe Password should be in between 8 to 16 characters :/\n")

        else:
            password = ''
        
            for i in range(choice):
                random = secrets.choice(allchar)
                password += random  
        
            print('\n'+ '-'*50+'\n')
            print("Here is You Secure Password :",password,'\n')
            print('-'*50 +'\n')
            print("="*150+'\n')
            break
        
    except:
        print("\nError : Enter Numbers Only!\n")
