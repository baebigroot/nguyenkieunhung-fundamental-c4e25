n = int(input("Enter n: "))
for i in range (1, n+1):
    print(i)


n = int(input("Enter n: "))
for i in range (0, n+1, 2):
    print(i)


from turtle import *
shape("turtle")
for i in range (20):
    forward(i * 10)
    left(90)

print(i)


from turtle import *
shape("turtle")
d = 100
for i in range (20):
    forward(i * 10)
    left(90)
    d += 10
print(i)