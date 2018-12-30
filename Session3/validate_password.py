loop = True
while loop:
    p = input("Enter your password: ")
    loop = False
    if len(p) < 8:
        print("Password length must be greater than 8.")
        loop = True
    if p.isalnum():
        print("Password must not contain special characters.")
        loop = True
    if p.isdigit():
        print("Password must contain letter.")
        loop = True
    if p.isalpha():
        print("Password must contain digit.")
        loop = True
    
print("Password OK")

 