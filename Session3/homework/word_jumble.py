words = ["fitz", "coulson", "daisy",]

import random
ques = random.choice(words)
correct = ques
jumble = ""

while ques:
    position = random.randrange(len(ques))
    jumble += ques[position]
    ques = (ques[:position] + ques[(position+1):])

print("The jumble is: ", end = "")
print(*jumble, sep=" ")
guess = input("Your answer? ")

while guess != correct:
    print("That's not it :<. Please try again: ", end = "")
    guess = input("")
print("Huray! You got it :D")