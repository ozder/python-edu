import hashlib
import getpass
import tomllib

password_manager = {}


def create_account():
    username = input("enter desired name")
    password = getpass.getpass("enter desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print('created success')


def login():
    username = input("enter username")
    password = getpass.getpass("enter desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print(password_manager)
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print('login success')
    else:
        print('invalid username or password')


def main():
    while True:
        choice = input("enter 1 to create an account, 2 to login, or 0 to exit")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("invalid choise")


if __name__ == "__main__":
    main()
