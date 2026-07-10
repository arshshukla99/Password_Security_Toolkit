print("\n=== Password Security Toolkit v0.3===\n")
print("Welcome to Password Security Toolkit!")
print("A Strong Password can be a reason why your account will not be Hijacked in Future...\n")
password = input('Enter Your Password Here for an Audit: ')
print()

MIN_LENGTH = 8
MAX_LENGTH = 12
MAX_SCORE = 5

#pass_check() function that checks the password and scores it according to its Length and what characters are involved in it.
def pass_check(password):
    upper = 0
    digit = 0
    special = 0
    score = 0
    lower = 0   #Not included in passwords normally, so just counting but not going to be used.
    space = 0   #Not included in passwords normally, so just counting but not going to be used.

    if len(password) >= MIN_LENGTH :
        score += 1
        if len(password) >= MAX_LENGTH :
            score += 1

    for i in password:
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
    
    return upper, digit, special, score, space

#dict_check() check is the password or a particular word in the password is in the wordlist or not and yields True/False accordingly.
dict_word_found = False
dict_pass_found = False
word_found = ""

def dict_check(password):
    temp_word_found = False
    temp_pass_found = False
    temp_word = ''
    
    with open("common_passwords.txt", "r",encoding='utf-8',errors='ignore') as f:
        wordlist = f.read().rstrip("\n").splitlines()
        for i in wordlist:
            if len(i) >= 3 and i in password.lower():
                temp_word_found = True
                temp_word = i
                break
            if len(i) >=3 and i == password.lower():
                temp_pass_found = True
                break
        return temp_word_found, temp_word, temp_pass_found
        
def pattern_recognition(password):
    sequential_found = False
    sequential = ''

    for i in password:
        if i.isdigit():
            if password[i] == password[i-1] and password[i+1] == password[i-2] and password[i+2] == password[i-3] :
                sequential_found = True
                sequential = password[i] + password[i+1] + password[i+2] + password[i+3] 
            else:
                continue

#suggestions() function that takes the password and it characteristics and gives suggestions to improve the password.
def suggestions(password, upper, digit, special, score, space):
    if space == 0:
        if score == 0 :
            print(f"• Your Password Must contain Atleast {MIN_LENGTH} Characters.")
            if upper == 0 or digit == 0 or special == 0 :
                print("• Should be a mix of Uppercase, Lowercase, Digits or Spacial characters.\n")

        elif score == 1 :
            if len(password) < MIN_LENGTH:
                print(f"• Your Password Must contain Atleast {MIN_LENGTH} Characters.")
            else:
                print(f"Pretty Bad password choice. Your Password Score Overall {score}/{MAX_SCORE} in terms of Security.\n")
                if len(password) < MAX_LENGTH:
                    print(f"• Try to increase length of your password upto {MAX_LENGTH} Characters.")
                if upper == 0:
                    print("• Try Adding some Uppercase Letters into your password also.")
                if digit == 0 :
                    print("• Try Adding some Integer Digits to your password also.")
                if special == 0 :
                    print("• Try Adding some Special Characters to your password as they can improve your Password Security.")

        elif score == 2:
            if len(password) < MIN_LENGTH:
                print(f"• Your Password Must contain Atleast {MIN_LENGTH} Characters.")
            else:
                print(f"That is not a Good Password Honestly.\nYour Password Scored Overall {score}/{MAX_SCORE} in terms of Security.\n")
                if len(password) < MAX_LENGTH:
                    print(f"• Try to increase length of your password upto {MAX_LENGTH} Characters.")
                if upper == 0:
                   print("• Try Adding some Uppercase Letters into your password also.")
                if digit == 0 :
                    print("• Try Adding some Integer Digits to your password also.")
                if special == 0 :
                    print("• Try Adding some Special Characters to your password as they can improve your Password Security.")

        elif score == 3 :
            if len(password) < MIN_LENGTH:
                print(f"• Your Password Must contain Atleast {MIN_LENGTH} Characters.")
            else:
                print(f"It is a decent one but still needs improvements.\nYour Password Scored Overall {score}/{MAX_SCORE} in terms of Security.\n")
                if len(password) < MAX_LENGTH:
                    print(f"• Try to increase length of your password upto {MAX_LENGTH} Characters.")
                if upper == 0:
                    print("• Try Adding some Uppercase Letters into your password also.")
                if digit == 0 :
                    print("• Try Adding some Integer Digits to your password also.")
                if special == 0 :
                    print("• Try Adding some Special Characters to your password as they can improve your Password Security.")

        elif score == 4:
            print(f"This is a Good One. But Still can be Better. Your Password Scored Overall {score}/{MAX_SCORE} in terms of Security.\n")

            if len(password) < MAX_LENGTH:
                print(f"• Try to increase length of your password upto {MAX_LENGTH} Characters.")
            if upper == 0:
                print("• Try Adding some Uppercase Letters into your password also.")
            if digit == 0 :
                print("• Try Adding some Integer Digits to your password also.")
            if special == 0 :
                print("• Try Adding some Special Characters to your password as they can improve your Password Security.")

        elif score == MAX_SCORE:
            print(f"Now This is what we called a Great Password! Your Password Scored {score}/{MAX_SCORE} in terms of Security.")
    else:
        print("Your password should NOT contain Blank Spaces. Try Again...")

# takes the arguments returned from the function pass_check() and store it in variable
upper, digit, special, score, space = pass_check(password)

#the variables unpack the ouput of dict_check()
dict_word_found, word_found, dict_pass_found = dict_check(password)

#Checks if the password or particular word in the password found or not 
if dict_pass_found == False:
    if dict_word_found == True:
        suggestions(password, upper, digit, special, score, space)

        print("\n⚠ Dictionary Word Detected!\n")
        print(f"Found word : '{word_found}' in Common Attack Dictionary\n")
        print(f"It is recommended not to use common words in your password which can be found in Common Attack Dictionaries...")
    else:
        upper, digit, special, score, space = pass_check(password)
        suggestions(password, upper, digit, special, score, space)
else:
    print(f"Your Password is too Common!\nFound in Common Attack Dictionary.\n\nYour Password Scored 0/{MAX_SCORE} in terms of Security.")

#Choice for the User if he wants continuation on the password Audit
while True:
    choice = input("\nDo you want to Audit Another Password ?\nEnter your Choice (Y/N) : ")

    if choice.lower() == "y":
        retry_pass = input("\nEnter Another Password : ")
        print()
        password = retry_pass
        upper, digit, special, score, space = pass_check(password)

        dict_word_found, word_found, dict_pass_found = dict_check(password)
        
        if dict_pass_found == False:
            if dict_word_found == True:
                suggestions(password, upper, digit, special, score, space)
                    
                print("\n⚠ Dictionary Word Detected!\n")
                print(f"Found word : '{word_found}' in Common Attack Dictionary\n")
                print(f"It is recommended not to use common words in your password which can be found in Common Attack Dictionaries...")
            else:
                upper, digit, special, score, space = pass_check(password)
                suggestions(password, upper, digit, special, score, space)
        else:
           print(f"Your Password is too Common!\nFound in Common Attack Dictionary.\n\nYour Password Scored 0/{MAX_SCORE} in terms of Security.")
                
    elif choice.lower() == 'n':
        break

    else:
        print("Invalid Choice! Give Choice inputting single characters like 'y' or 'Y' or 'n' or 'N' ")
