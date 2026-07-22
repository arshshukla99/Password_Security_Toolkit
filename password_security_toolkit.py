import math

print("\n=== Password Security Toolkit v0.6 ===\n")
print("Welcome to Password Security Toolkit!")
print("A Strong Password can be a reason why your account will not be hijacked in Future...\n")

password = input('Enter Your Password Here for an Audit: ')
print()

MIN_LENGTH = 8
MAX_LENGTH = 12
MAX_SCORE = 5

#pass_score() function that checks the password and scores it according to its Length and what characters are involved in it.
def pass_score(password):
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
    
    return upper, lower, digit, special, score, space

#dict_check() check is the password or a particular word in the password is in the wordlist or not.

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
    return temp_pass_found, temp_word_found, temp_word

#pattern_recognition_sequential() Checks for Sequential Number Pattern in the password.
sequential_found = False

def pattern_recognition_sequential(password):
    temp_seq_found = False
    seq_num = ''
    temp_num = ''
    
    for i in password:
        if i.isdigit():
            temp_num += i
            
    for j in range(len(temp_num)):
            if j==0:
                seq_num += temp_num[j]
                
            elif j!=0 and int(temp_num[j-1]) + 1 == int(temp_num[j]):
                seq_num += temp_num[j]
                
    if len(seq_num) >= 3:
        temp_seq_found = True
        
    return temp_seq_found, seq_num

#pattern_recognition_block() function check weather there are repeating blocks in a password
def pattern_recognition_block(password):
    temp_block_found = False
    temp_block = ''
    
    for block_size in range(2, len(password)//2 + 1):   #Sets a block size of 2, 3, 4 ... till the half length of password
        for start_index in range(0, len(password) - block_size + 1):   # Sets the starting index from which the block is decided and subtracted by the block size
            temp_block = password[start_index : start_index + block_size] # if block 'ab' starting index is 2 then it takes till 2 + blocksize to compare the block repeat after that block

            index = start_index + len(temp_block)

            if temp_block == password[index : index + len(temp_block)]:
                temp_block_found = True
                break
        if temp_block_found == True:
            break
    return temp_block_found, temp_block

#pattern_recognition_keyboard_walks() function check weather the password contains keyboard walks in the password.
def pattern_recognition_keyboard_walks(password):
    temp_walk_found = False
    temp_walk = ''
    with open("keyboard_walks.txt","r",encoding='utf-8',errors='ignore') as f:
        walks = f.read().splitlines()
        
        for walk in walks:
            if walk[:4] in password.lower() :
                temp_walk_found = True
                temp_walk = walk[:4]
                break
            if walk[4:] in password.lower() :
                temp_walk_found = True
                temp_walk = walk[4:]
                break
    return temp_walk_found, temp_walk

#pattern_recognition_alphabet_sequence() function checks whether the password contains alphabetical sequence in the password.
def pattern_recognition_alphabet_sequence(password):
    temp_alpha_found = False
    temp_alpha_store = ''
    temp_alpha = ''
    
    for i in password:
        if i.isalpha():
            temp_alpha_store += i
            
    for j in range(len(temp_alpha_store)):
        if j == 0:
            temp_alpha += temp_alpha_store[j]
            
        elif j != 0 and ord(temp_alpha_store[j-1].lower()) + 1 == ord(temp_alpha_store[j].lower()):
            temp_alpha += temp_alpha_store[j]
    
    if len(temp_alpha) > 3:
        temp_alpha_found = True
    
    return temp_alpha_found, temp_alpha

def entropy_check(upper, lower, digit, special):
    total = 94
    if lower == 0:
        total -= 26
    if upper == 0:
        total -= 26
    if digit == 0:
        total -= 10
    if special == 0:
        total -= 32
    
    temp_entropy = (upper + lower + digit + special) * math.log2(total)
    entropy_risk_points = 0
    
    if temp_entropy < 30:
        temp_final_entropy = "Very Weak"
        entropy_risk_points += 5
    elif temp_entropy >= 30 and temp_entropy < 40:
        temp_final_entropy = "Weak"
        entropy_risk_points += 3
    elif temp_entropy >= 40 and temp_entropy < 50:
        temp_final_entropy = "Medium"
        entropy_risk_points += 2
    elif temp_entropy >= 50 and temp_entropy < 70:
        temp_final_entropy = "Strong"
        entropy_risk_points += 1
    elif temp_entropy >= 70:
        temp_final_entropy = "Very Strong"
    
    return temp_entropy, temp_final_entropy, entropy_risk_points

#recommendations() function that takes the password and it characteristics and gives suggestions to improve the password.
def recommendations(password, upper, digit, special, score, space):
    if space == 0:
        if score == 0 :
            print(f"• Your Password Must contain Atleast {MIN_LENGTH} Characters.")
            if upper == 0 or digit == 0 or special == 0 :
                print("• Should be a mix of Uppercase, Lowercase, Digits or Spacial characters.\n")

        elif score == 1 :
            if len(password) < MIN_LENGTH:
                print(f"• Your Password Must contain Atleast {MIN_LENGTH} Characters.")
            else:
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
                if len(password) < MAX_LENGTH:
                    print(f"• Try to increase length of your password upto {MAX_LENGTH} Characters.")
                if upper == 0:
                    print("• Try Adding some Uppercase Letters into your password also.")
                if digit == 0 :
                    print("• Try Adding some Integer Digits to your password also.")
                if special == 0 :
                    print("• Try Adding some Special Characters to your password as they can improve your Password Security.")

        elif score == 4:

            if len(password) < MAX_LENGTH:
                print(f"• Try to increase length of your password upto {MAX_LENGTH} Characters.")
            if upper == 0:
                print("• Try Adding some Uppercase Letters into your password also.")
            if digit == 0 :
                print("• Try Adding some Integer Digits to your password also.")
            if special == 0 :
                print("• Try Adding some Special Characters to your password as they can improve your Password Security.")

        elif score == MAX_SCORE:
            print("None")
    else:
        print("Your password should NOT contain Blank Spaces. Try Again...")

#risk_assessment() function shows risk assessment according to risk points gained by the password.
def risk_assessment(final_entropy_report, risk_points):
    if risk_points == 0:
        print("Low Security risks, \nThis password is Consistent with the modern password guidance and NIST guidelines.\n")

    elif risk_points > 0 and risk_points < 3:
        print("This password is consistent with the modern password guidance.\n")
        print('-'*75 + '')
        print("NIST Password Guidance\n\n• Use passwords of at least 12–16 characters.\n• Prefer randomly generated passwords.\n• Use a unique password for every account.\n• Avoid dictionary words and predictable patterns.\n")

    elif risk_points >= 3 and risk_points < 5:
        print(f"Although the password has {final_entropy_report} theoretical entropy but it contains \npredictable human pattern which will reduce it resistance against \nmodern Password Cracking methods.\n")
        print('-'*75 + '')
        print("NIST Password Guidance\n\n• Use passwords of at least 12–16 characters.\n• Prefer randomly generated passwords.\n• Use a unique password for every account.\n• Avoid dictionary words and predictable patterns.\n")

    elif risk_points >= 5 and risk_points < 8 :
        print(f"This password has {final_entropy_report} theoretical entropy. Therefore, It has \nenrtropy score under the safe criteria as well as it \ncontains predictable human patterns which will highly reduce \nits resistance against modern Password Cracking methods.\n")

    elif risk_points >= 8 :
        print("This password will have very weak resistance against modern Password Cracking methods and can be easily exploited. Consider Changing it as soon as possible.\n")

#crack_time() function checks the cracking time of password from the attacker perspective if he trys offline password cracking with modern GPUs.
def crack_time(password, upper, lower, digit, special):
    total_characters = 0
    
    if upper != 0:
        total_characters += 26
    if lower != 0:
        total_characters += 26
    if digit != 0:
        total_characters += 10
    if special != 0:
        total_characters += 32
    
    total_combinations = total_characters ** len(password)
    
    temp_crack = total_combinations / 10000000000 #estimated 100 billion password guesses/sec
    
    return temp_crack
    
def pass_audit(password):
    print("="*100)
    print(" "*35 +"PASSWORD AUDIT REPORT")
    print("="*100 + '\n')
    
    # yielding password specifications and scoring
    upper, lower, digit, special, score, space = pass_score(password)
    
    #The Theoretical Entropy Evaluation
    entropy, final_entropy_report, risk_points = entropy_check(upper, lower, digit, special)
    print(f"Password length        : {len(password)} Characters")
    print(f"Password Score         : {score} / 5")
    print(f"Theoretical Entropy    : {round(entropy,2)}")
    print(f"Entropy Rating         : {final_entropy_report}\n")
    
    print("-"*75 + '')
    print("Attack Pattern Analysis\n" )
    
    pass_found, word_found, word = dict_check(password)
    seq_found, seq_num = pattern_recognition_sequential(password)
    block_found, block = pattern_recognition_block(password)
    walk_found, walk = pattern_recognition_keyboard_walks(password)
    alpha_found, alpha = pattern_recognition_alphabet_sequence(password)
    
    if pass_found :
        print("Dictionary Word             : Found, Whole Password")
        risk_points += 1
    else:
        if word_found:
            print(f"Dictionary Word             : Found --> '{word}'")
            risk_points += 1
        else:
            print("Dictionary Word             : Not Found")
    
    if seq_found :
        print(f"Sequential Numbers          : Found --> '{seq_num}'")
        risk_points += 1
    else:
        print("Sequential Numbers          : Not Found")
    
    if block_found:
        print(f"Repeated Blocks             : Found --> '{block}'")
        risk_points += 1
    else:
        print("Repeated Blocks             : Not Found")
    
    if walk_found :
        print(f"Keyboard Walks              : Found --> '{walk}'")
        risk_points += 1
    else:
        print("Keyboard Walks              : Not Found")
    
    if alpha_found:
        print(f"Alphabetical Sequence       : Found --> '{alpha}'\n")
        risk_points += 1
    else:
        print("Alphabetical Sequence       : Not Found\n")
    
    pass_crack_time = crack_time(password, upper, lower, digit, special)
    print(f"Estimated Crack time :\n\n{round((pass_crack_time/60), 10)} seconds\n{round((pass_crack_time/3600), 5)} hours\n{round((pass_crack_time/86400), 2)} days\n(This estimation is according to number of guesses mordern GPUs can make per seconds (i.e. 100 billion) if an attacker trys to crack password offline.)\n")
    
    #risk assessment in the output according to password quality
    print('-'*75 + '')
    print("Risk Assessment\n")
    risk_assessment(final_entropy_report,risk_points)
    
    #recommendations for the password
    print('-'*75 + '')
    print("Recommendations\n")
    
    recommendations(password, upper, digit, special, score, space)
    print('\n' + "="*100)


#Initial Function call
pass_audit(password)

#Choice for the User if the user wants continuation on the password Audit
while True:
    choice = input("\nDo you want to Audit Another Password ?\nEnter your Choice (Y/N) : ")

    if choice.lower() == "y":
        retry_pass = input("\nEnter Another Password : ")
        print()
        password = retry_pass
        
        pass_audit(password)
                
    elif choice.lower() == 'n':
        break

    else:
        print("Invalid Choice! Give a choice by inputting single characters like 'y' or 'Y' or 'n' or 'N' ")
        
