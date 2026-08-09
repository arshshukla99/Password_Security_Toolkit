import sys
import subprocess
from pathlib import Path

print("\n=== Password Security Toolkit v1.0 ===\n")
print("Welcome to Password Security Toolkit!")
print("A Strong Password can be a reason why your account will not be hijacked in Future...")

choice = 0

while True:
    try:
        choice = int(input("\nChoose what tool to continue with :\n1) Password Audit\n2) Password Generation\n3) Password Breach Search\n4) Exit\n\nYour Choice : "))
    except:
        print("Invalid Choice!! Enter Numbers Only!\n")
        continue
        
    if choice == 1:
        subprocess.run([sys.executable, Path(__file__).parent / "password_audit.py"])
        
    elif choice == 2:
        subprocess.run([sys.executable, Path(__file__).parent / "password_generation.py"])

    elif choice == 3:
        subprocess.run([sys.executable, Path(__file__).parent / "password_breach_search.py"])
        
    elif choice == 4:
        print("Exiting...")
        sys.exit()
    
    else:
        print("\nPlease Enter a Valid Choice !\n")
        
