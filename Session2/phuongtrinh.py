a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

delta = b ** 2 - 4*a*c
a2 = 2*a 
x = - b / a2

x1 = (-b + delta ** (1/2)) / a2
x2 = (-b - delta ** (1/2)) / a2

if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có 1 nghiệm: ",x)
else:
    print("Phương trình có 2 nghiệm",x1,"và",x2)