answer = {
    "Answer the following algebra question: \nIf x = 8, then what's the value of 4(x + 3) \n 1. : 35 \n 2. : 36 \n 3. : 40 \n 4. : 44" : 4,
    "Estimate this answer (exact calculation not needed):\nJack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean? \n 1. 55 \n 2. 65 \n 3. 75 \n 4. 85" : 2
}

score = 0

for k in answer.keys():
    print(k)
    x = int(input("Your choice: "))
    if x != answer[k]:
        print(":(")
    else:
        print("Bingo.")
        score += 1

print("You correctly answer", score, "out of", len(answer), "questions.")
