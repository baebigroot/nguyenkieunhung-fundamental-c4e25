person = {
    "name": "Quan",
    "age": 25,
    "location": "Hanoi",
}

#DEBUG: quet qua toan bo du lieu ben trong
# for k in person.key():
#     print(k, person[k]) #person[k]: value

# for v in person.values():
#     print(v)

for k, v in person.items():
    print(k, v, sep = ": ")
