ques = {
    "Answer the following algebra question: \nIf x = 8, then what is the value of 4(x + 3) ? \n1. 35 \n2. 36 \n3. 40 \n4. 44": 4,
    "Estimate this answer (exact calculation not needed) \nJack score these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean? \n1. About 55\n2. About 65\n3. About 75\n4. About 85": 2,
    "Answer the following question: \nWho is Obama? \n1. The President of Vietnam \n2. A singer \n3. A celebrity \n4. Donald Trump's father": 3,
    "Answer the following PUN question: \nWhich country's capital has the fastest-growing population? \n1. USA (Washington, D.C) \n2. Russia (Moskva)\n3. China (Beijing)\n4. Ireland (everyday it's Dublin)": 4,
}

score = 0

for k in ques.keys():
    print(k)
    x = int(input("Your choice: "))
    if x != ques[k]:
        print(":( \nThe correct answer is", ques[k], "\n")
    else:
        print("Bingo. \n")
        score += 1

print("You correctly answer", score, "out of", len(ques), "questions.")