for i in range (20):
    print("* ", end = '')
print()



n = int(input("Enter a number: "))
for i in range (n):
    print("* ", end = '')
print()



for i in range (9):
    if i % 2:
        print("* ", end = '')
    else:
        print("x ", end = '')
print()



n = int(input("Enter a number: "))
for i in range (n):
    if i % 2:
        print("* ", end = '')
    else:
        print("x ", end = '')
print()



for i in range (3):
    for i in range(7):
        print("* ", end = '')
    print()



n = int(input("Enter n: "))
m = int(input("Enter m: "))

for i in range (m):
    for i in range (n):
        print("* ", end = '')
    print()