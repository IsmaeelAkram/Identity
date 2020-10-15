import os, sys

def clear():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

clear()
print("===== IDENTITY MENU =====")
print("1) Start in release mode")
print("2) Start in development mode")
print("3) Exit")
choice = input("> ")

print("Any boot args? ")
bootargs = input("> ")

clear()

if(choice == '1'):
    os.system(f"python3 identity.py {bootargs}")
elif(choice == '2'):
    os.system(f"nodemon --exec python3 identity.py {bootargs}")
else:
    sys.exit()