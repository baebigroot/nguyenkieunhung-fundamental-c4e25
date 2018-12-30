from random import randint
x = randint(1,10)
print(x)

loop = 0
n = int(input("Guess my number: "))

while x != n and loop <3:
    if x > n:
        print("A little too small!")
    elif x < n:
        print("A little too big")
    n = int(input("Enter your guess: "))
    loop += 1

if loop < 3:
    print("Bingo")
else:
    print("You lose")