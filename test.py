from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'ab') as key_file:
        key_file.write(key)

def load_key():
    file = open ("key.key", "rb")
    key = file.read()
    file.close()
    return key

def m_pass():
    '''master_pwd = input("What is master Password? ")''' '''master pass is not needed/important'''
    key = load_key(); '''+ master_pwd.encode()'''
    fer = Fernet(key)
    return fer

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = (line)
            user, passe = data.split("|")
            print("User: ", user, ", " + "Password: ", fer.decrypt(passe.encode()).decode());     '''Decrypting the password'''


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n");     '''Encrypting while entering the password'''


write_key();                     '''system generating the key'''
fer = m_pass();                  '''this fer use for load key for encrypt or decrypt'''
while True:
    mode = input("would you like to add a new password or view existing ones (view, add)? Press q to quite: ").lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode...!!!")
        continue
