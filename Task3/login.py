import main_template
# Checks if the password and username match.
username = main_template.username_input()
password = main_template.password_input()
encoded = main_template.encoded_password(password)

for line in main_template.read():
    row = line.strip().split(":")
    username_row = row[0]
    password_row = row[2]
    if username == username_row and encoded == password_row:
        print("Access Granted")
        break
else:  
    print("Access Denied.")
        
        
    
    
            


