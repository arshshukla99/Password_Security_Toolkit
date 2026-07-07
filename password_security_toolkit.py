print("\n=== Password Security Toolkit ===\n")
print("Welcome to Password Security Toolkit!")
print("A Strong Password can be a reason why your account will not be Hijacked in Future...\n")
password = input('Enter Your Password Here for an Audit: ')
print()

score = 0

def pass_check(password, score):
    length = 0
    upper = 0
    digit = 0
    special = 0
    
    lower = 0   #Not included in passwords normally so just counting but not going to used.
    space = 0   #Not included in passwords normally so just counting but not going to used.

    if len(password) >= 8 :
        score += 1
        if len(password) >= 12:
            score += 1

    for i in password:
        length += 1
        if i.isupper():
            upper += 1
        elif i.isdigit():
            digit += 1
        elif i.isspace():
             space += 1   #Counting so that it is not counted in special.
        elif i.islower():
            lower += 1   #Counting so that it is not counted in special.
        else:
            special += 1

    if upper >= 1:
        score += 1
    if special >= 1:
        score += 1
    if digit >= 1:
        score += 1
        
    if space == 0:
        if score == 0 :
            print("• Your Password Must contain Atleast 8 Characters.\n• Should be a mix of Uppercase, Lowercase, Digits or Spacial characters.\n")
        
        elif score == 1 :
            if length < 8:
                print("• Your Password Must contain Atleast 8 Characters.")
            else:
                print(f"Pretty Bad password choice. Your Password Score Overall {score}/5 in terms of Security.\n")
                if length < 12:
                    print("• Try to increase length of your password upto 12 Characters.")
                if upper == 0:
                    print("• Try Adding some Uppercase Letters into your password also.")
                if digit == 0 :
                    print("• Try Adding some Integer Digits to your password also.")
                if special == 0 :
                    print("• Try Adding some Special Characters to your password as they can improve your Password Security.")
        
        elif score == 2:
            if length < 8:
                print("• Your Password Must contain Atleast 8 Characters.")
            else:
                print(f"That is not a Good Password Honestly.\nYour Password Scored Overall {score}/5 in terms of Security.\n")
                if length < 12:
                    print("• Try to increase length of your password upto 12 Characters.")
                if upper == 0:
                   print("• Try Adding some Uppercase Letters into your password also.")
                if digit == 0 :
                    print("• Try Adding some Integer Digits to your password also.")
                if special == 0 :
                    print("• Try Adding some Special Characters to your password as they can improve your Password Security.")

        elif score == 3 :
            if length < 8:
                print("• Your Password Must contain Atleast 8 Characters.")
            else:
                print(f"It is a decent one but still needs improvements.\nYour Password Scored Overall {score}/5 in terms of Security.\n")
                if length < 12:
                    print("• Try to increase length of your password upto 12 Characters.")
                if upper == 0:
                    print("• Try Adding some Uppercase Letters into your password also.")
                if digit == 0 :
                    print("• Try Adding some Integer Digits to your password also.")
                if special == 0 :
                    print("• Try Adding some Special Characters to your password as they can improve your Password Security.")
                
        elif score == 4:
            print(f"This is a Good One. But Still can be Better. Your Password Scored Overall {score}/5 in terms of Security.\n")
        
            if length < 12:
                print("• Try to increase length of your password upto 12 Characters.")
            if upper == 0:
                print("• Try Adding some Uppercase Letters into your password also.")
            if digit == 0 :
                print("• Try Adding some Integer Digits to your password also.")
            if special == 0 :
                print("• Try Adding some Special Characters to your password as they can improve your Password Security.")

        elif score == 5:
            print(f"Now This is what we called a Great Password! Your Password Scored {score}/5 in terms of Security.\n")
    else:
        print("Your password should NOT contain Blank Spaces. Try Again...")
        
pass_check(password, score)

while True:
    if len(password) == 12:
        break
    else:
        retry_pass = input("\nNo Worries. Try with another one : ")
        print()
        password = retry_pass
        pass_check(password, score)
