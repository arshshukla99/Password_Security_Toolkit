import sys
import subprocess
from pathlib import Path

print("\n=== Password Security Toolkit v0.8 ===\n")
print("Welcome to Password Security Toolkit!")
print("A Strong Password can be a reason why your account will not be hijacked in Future...")

choice = 0

while True:
    try:
        choice = int(input("\nChoose what tool to continue with :\n1) Password Audit\n2) Password Generation\n3) Exit\n\nYour Choice : "))
    except:
        print("Invalid Choice!! Enter Numbers Only!\n")
        continue
        
    if choice == 1:
        subprocess.run([sys.executable, Path(__file__).parent / "password_audit.py"])
        
    elif choice == 2:
        subprocess.run([sys.executable, Path(__file__).parent / "password_generation.py"])
        
    elif choice == 3:
        print("Exiting...")
        sys.exit()
    
    else:
        print("\nPlease Enter a Valid Choice !\n")
        
