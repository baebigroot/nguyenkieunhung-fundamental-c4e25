count = 0
loop = True
while loop:
    print("Answer the following algebra question:")
    print("If x = 8, then what is the value of 4(x + 3)?")
    ans_1 = [35,36,40,44]
    for index, num in enumerate(ans_1):
        print(index+1,num,sep=". ")
    a = input("Your choice: ")   
    if a == "3":
        print("Bingo")
        count += 1
        loop = False
    else:
        print(":(")
        loop = True
    print("Estimate this answer (exact calculation not need):")
    print("Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?")
    ans_2 = ["About 55", "About 65", "About 75", "About 85"]
    for index, num in enumerate(ans_2):
        print(index+1,num,sep=". ")
    b = input("Your choice: ")
    if b == "2":
        print("Bingo")
        count += 1
        loop = False
    else:
        print(":(")
        loop = False
print("You correctly answer",count,"out of 2 question") 