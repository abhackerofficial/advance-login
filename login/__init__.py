#!/bin/python3

from time import sleep
import sys

lines = ["Login your credentials."]

filename = "user.json"
__version__= 1.0

def slow():
    for line in lines:          # for each line of text (or each message)
        for c in line:          # for each character in each line
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.02)          # wait a little to make the effect look good.
        print('')

from alive_progress import alive_bar
import time

def compute():
    for i in range(100):
        time.sleep(0.005) # process items as usual.
        yield  # insert this :)

import pwinput, hashlib, getpass, atexit, os, json

for arg in sys.argv:
    if arg == "--create":
        current_dir = os.getcwd()

        def hash_password(password):
            return hashlib.md5(password.encode()).hexdigest()
        def save_credentials(username, password):
            hashed_password = hash_password(password)
            credentials = {
                "username": username,
                "password_hash": hashed_password
            }

            with open("user.json", "w") as file:
                json.dump(credentials, file)
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        epasswd = pwinput.pwinput(prompt='Confirm Passwd: ', mask='*')
        if password == epasswd:
            save_credentials(username, password)
            # Open a file for writing
            with open("startup.sh", "w") as file:
                file.write(f"cd {current_dir} && python3 -m login")

            print("Credentials has been saved to config file: \33[92muser.json\33[0m")
            exit()
        else:
            print("Password doesn't match.")
            exit()
    elif arg == "--remove":
        if os.path.exists(filename):
            with open("startup.sh", "w") as file:
                file.write(f"exec")
                os.remove("user.json")
                print("Login config file has been removed.")
                exit()
        elif not os.path.exists(filename):
            print("Credentials file not found.\nCreate config file using\33[92m python3 -m login --create\33[0m")
            exit()

if not os.path.exists(filename):
    print("Credentials file not found.\nCreate config file using\33[92m python3 login --create\33[0m")
    exit()
elif os.path.exists(filename):
    with open("user.json","r") as json_string:
        parsed_dict = json.load(json_string)
        username = parsed_dict["username"]
        passwd = parsed_dict["password_hash"]

#passwd_hash=hashlib.md5(f"{passwd}".encode('utf-8')).hexdigest()

#passwd_hash="76a2173be6393254e72ffa4d6df1030a"
#username="root"

bypass=1

os.system("clear")

slow()

while True:
    try:
        if bypass == 0:
            break
        else:
            while True:
                if True:
                    os.system("stty eof ^X")
                    atexit.register(lambda: os.system("stty eof ^D"))
                    myuser = input('Username: ')
                    if username == myuser:
                        break
                    else:
                        print("\33[91mAccess Denied.\33[0m")

        while True:
#            myinput = getpass.getpass('Password: ')
            myinput = pwinput.pwinput(prompt='Password: ', mask='*')
            input_hash=hashlib.md5(f"{myinput}".encode('utf-8')).hexdigest()
            if passwd == input_hash:
                with alive_bar(100) as bar:
                    for i in compute():
                        bar()
                print(f"\33[92mAccess Granted. : Hello, {username}\33[0m")
                bypass=0
                break
            else:
                print("\33[91mAccess Denied.\33[0m")

    except KeyboardInterrupt:
        print("CTRL+C DETECTED")


