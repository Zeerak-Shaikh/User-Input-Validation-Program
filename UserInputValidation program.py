# User input validation Program
username= input("Enter your Username: ")
if len(username) > 12:
     print("Your Username can not be longer than 12 letters.")
elif not username.find(" ")==-1:
    print("Your username can not contain spaces.")
elif  not  username.isalpha():
    print("Your Username can not contain digits.")
else:
    print(f"Welcome {username}")
