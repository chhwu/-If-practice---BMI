height = float(input('Please enter you height(m):'))
weight = float(input('Please enter your weight(kg): '))
bmi = weight / (height ** 2)
if bmi >= 35:
    print('Extreme obesity.')
elif 30 <= bmi < 35:
    print('Middle obesity.')
elif 27 <= bmi < 30:
    print('Slight obesity.')
elif 24 <= bmi < 27:
    print('Overweight.')
elif 18.5 <= bmi < 24:
    print('Normal weight.')
else:
    print('Underweight.')