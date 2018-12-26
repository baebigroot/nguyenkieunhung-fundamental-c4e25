from random import randint
weather = randint(1, 100)
print(weather)
if 1 < weather <= 30:
    print("Rainy")
elif weather <= 60:
    print("Cloudy")
else:
    print("Sunny")
