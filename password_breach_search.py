import requests
import hashlib
import getpass

def pass_hash(password: str):
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

def check_breach(sha1_hash):
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    found = False
    matching_hash = None
    
    try:
        response = requests.get(url, timeout=5)
        
    except requests.exceptions.ConnectionError:
        print("\nNetwork Error : No Internet Connection or Server is down.")
        return None, None

    except requests.exceptions.Timeout:
        print("\nConnection Timeout : The request took to long for respond.")
        return None, None
    
    except Exception as e:
        print("\nError Occurred :", e)
        return None, None

    if response.status_code != 200:
        raise RuntimeError("\nNot able to search the password")

    for i in response.text.splitlines():
        matching_hash = i.split(':')

        if matching_hash[0] == suffix:
            found = True
            return found, matching_hash[1]
        
    return found, None

def main():
    password = getpass.getpass("Enter your Password to check if it is in the Data Breaches: ")
    
    sha1_hash = pass_hash(password)
    match_found, matched_no = check_breach(sha1_hash)

    if match_found:
        print(f"\nAlert! This password is found {matched_no} in previous Data Breaches. Change it Immediately!\n")
    elif match_found == False:
        print(f"\nThis Password is not found in the previous breaches. You can use it\n")
    else:
        print("No Requests Succeeded.\n")

if __name__ == "__main__":
    main()
