password = str(input("Enter the value of password"))
if len(password) < 6:
    print("Password is too weak")
elif len(password) <= 10:
    print("Password is medium")
else:
    print("password is Strong")

