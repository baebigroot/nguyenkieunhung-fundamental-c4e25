size = [ 5 ,7,300 , 90 ,24,50,75]

print("Hello , my name is hiep and these are my sheep size :")
print(size)

print(" now my biggest sheep  has size",max(size), " let's shear it")
x = size.index(max(size))
size[x]=8
print("after shearing , here is my flock")
print(size)

y=0
z = int(len(size))

for i in range(z):
    size[y]=size[i]+50
    y+=1

print("one month has pass , now here is my flock")
print(size)