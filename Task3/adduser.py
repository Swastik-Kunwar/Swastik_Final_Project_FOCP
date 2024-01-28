import main_template
# Creates and appends the username, name and password to the file.
username_list = main_template.username_list()

while True:        
    username = main_template.username_input()
    if username in username_list:                
        print("ALready exsits")
        continue
    else:
        name = input("Enter Name: ")
        password = input("Enter Password: ")
        encoded_password = main_template.encoded_password(password)
        lines = username + ":" + name + ":"+ encoded_password + "\n"
        
        main_template.append(lines)
        print("USER CREATED")
        break
