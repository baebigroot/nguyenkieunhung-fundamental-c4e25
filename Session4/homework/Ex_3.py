ques = {
    "Answer the following algebra question: \n If x = 8, then what is the value of 4(x + 3) ? \n 1. 35 \n 2. 36 \n 3. 40 \n 4. 44": 4,
}

for k in ques.keys():
    print(k)
    x = int(input("Your choice: "))
    while x != ques[k]:
        print(":( \n")
        print(k)
        x = int(input("Your choice: "))
    else:
        print("Bingo")