from getpass import getpass
import codecs

def read():
    """Reads the file in a list."""
    file_name = "passwd.txt"
    with open(file_name) as file:
        content = file.readlines()
        return content

def append(lines):
    """Appends the string to the file."""
    file_name = "passwd.txt"
    with open(file_name,"a") as file:
        file.write(lines)
        

def write(lines):
    """Writes the strings to the file."""
    file_name = "passwd.txt"
    with open(file_name,"w") as file:
        for line in lines:
            file.write(line)

def password_input():
    """User input Passowrd."""
    password = getpass("Enter Password: ").lower()
    return password

def encoded_password(password):
    """Encodes the password to rot-13."""
    encoded = codecs.encode(password, 'rot-13').lower()
    return encoded

def username_input():
    """Username input."""
    username = input("Enter Username: ").lower()
    return username

def username_list():
    """Creates a list of username in the file."""

    content = read()
    username_list = []

    for line in content:
        row = line.strip().split(":")
        username_list.append(row[0])
    return username_list


def password_list():
    """Creates a list of password in the file."""
    content = read()
    password_list = []

    for line in content:
        row = line.strip().split(":")
        password_list.append(row[2])
    return password_list
    
    