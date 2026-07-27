import sys
import subprocess

print("\n=== Password Security Toolkit v0.7 ===\n")
print("Welcome to Password Security Toolkit!")
print("A Strong Password can be a reason why your account will not be hijacked in Future...\n")

choice = int(input("Choose what tool to continue with :\n1) Password Audit\n2) Password Generation\n3) Exit\n\nYour Choice : "))

if choice == 1:
    subprocess.run([sys.executable,"password_audit.py"])

elif choice == 2:
    subprocess.run([sys.executable,"password_generation.py"])

elif choice == 3:
    print("Exiting...")
    sys.exit()

else:
    print("Please Enter a Valid Choice !")
    sys.exit()
