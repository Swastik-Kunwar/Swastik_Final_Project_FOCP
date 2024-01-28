import main_template
from getpass import getpass
#Changes the password.

content = main_template.read()
username_list = main_template.username_list()
password_list = main_template.password_list()

username = main_template.username_input()
if username in username_list:
    current_password = getpass("Current Password: ").lower()
    encoded = main_template.encoded_password(current_password)

    if encoded in password_list:
        new_password = getpass("New Password: ").lower()
        confirm = getpass("confirm: ").lower()

        if new_password == confirm:
            new_encoded_password = main_template.encoded_password(confirm)
            new_content = []
            for line in content:
                row = line.strip().split(":")
                if username in row:
                    row[-1] = new_encoded_password
                new_content.append(":".join(row) + "\n")
            main_template.write(new_content)

        else:
            print("Password is different")

    else:
        print("Incorrect Password ")

else:
    print("Incorrect Username")
