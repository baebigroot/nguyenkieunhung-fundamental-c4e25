Salary_per_hour= {
    "HUY": 25 ,
    "QUAN" : 25 ,
    "DUC": 30 ,
}
Hour ={
    "HUY":  30,
    "QUAN" : 20 ,
    "DUC": 40 ,
}

total = 0

for j in Hour:
    luong=Hour[j]*Salary_per_hour[j]
    total+=luong
    print("Luong hang tuan cua",j,"la",luong)
    
print("Tong luong =",total)