# C

person = {
    "Name": "Quan",
    "Age": 25,
    "Location": "Hanoi",
    "Exes": 3,
    "Status": False,
    "Friends": 125,
}

# print(person["Location"], person["Exes"], person["Status"], person["Friends"])

person["Name"] = "A.Quan" #update
person["exp"] = 2 #create

# print(person["skills"])

#kiem tra xem key co nam trong dict hay k
if  "skills" in person:
    print("Exists")
else:
    print("Not exists")

# print(person)