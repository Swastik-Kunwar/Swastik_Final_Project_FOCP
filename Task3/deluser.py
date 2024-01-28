import main_template
# Deletes the user

content = main_template.read()

username_list = main_template.username_list()
username = main_template.username_input()
password = main_template.password_input()
encoded = main_template.encoded_password(password)

for line in content:
    row = line.strip().split(":")
    username_row = row[0]
    password_row = row[2]
    if username == username_row and encoded == password_row:
        index = username_list.index(username)
        del content[index] 
             
        main_template.write(content)
        print("User Deleted")
        break
else:
    print("User or Password not in file or incorrect")


      
    