h_cm = int(input("Enter your height in cm: "))
m_kg = int(input("Enter your weight in kg: "))

h_m = h_cm / 100
bmi = m_kg / (h_m * h_m)
print("BMI:",bmi)

if bmi < 16:
    print("Severely underweight.")
elif 16 <= bmi < 18.5:
    print("Underweight.")
elif 18.5 <= bmi < 25:
    print("Normal.")
elif 25 <= bmi < 30:
    print("Overweight.")
else:
    print("Obese.")
