# Read

lookup = {
    "conviction": "strong belief",
    "advent": "arrival",
    "constitute": "be considered as",
}

for i in lookup:
    print(i, end = "   ")

print()
x = input("Your search: ").lower()
if x in lookup:
    print("Translation:", lookup[x])
else:
    cont = input("Word does not exist. Do you want to contribute (Y/N)?").upper()
    if cont == "Y":
        # ans = input("Enter translation")
        # lookup[x] = ans
        lookup[x] = input("Enter translation: ") #x: key/ cont: value
        
print(lookup)




# # U
# op = input("Do you want to update the translation? (Y/N)").upper()
# if op =="Y":
#     upd = input("Update which word? ").lower()
#     lookup[upd] = input("Enter new translation: ")

# print(lookup)