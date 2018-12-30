#2.1
size = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Hiep and these are my sheep sizes: ")
print(size)
print()

#2.2
print("Now my biggest sheep has size", max(size), "let's shear it.")
print()

m = size.index(max(size)) 
size[m] = 8

#2.3
print("After shearing, here is my flock: ")
print(size)
print()

#2.4
size = [x + 50 for x in size]

#2.5
print("MONTH 1: ")
print("One month has passed, now here is my flock")
print(size)

print("Now my biggest sheep has size", max(size), "let's shear it.")

m = size.index(max(size)) 
size[m] = 8

print("After shearing, here is my flock: ")
print(size)
print()

size = [x+50 for x in size]

print("MONTH 2: ")
print("One month has passed, now here is my flock")
print(size)

print("Now my biggest sheep has size", max(size), "let's shear it.")

m = size.index(max(size)) 
size[m] = 8

print("After shearing, here is my flock: ")
print(size)
print("")

size = [x+50 for x in size]

print("MONTH 3: ")
print("One month has passed, now here is my flock")
print(size)
print()

#2.6
print("My flock has size in total:", sum(size))
print("I would get", sum(size), "* 2$ =", sum(size)*2, "$")