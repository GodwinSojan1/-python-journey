def calculate_BMI(weight,height):
    result =  weight / (height * height)
    return result

def check_category(result):
    if result < 18.5:
        a = 'underweight'
        return a
    elif result > 25:
        b = 'overweight'
        return b
    else:
        c= 'normal'
        return c
       
weight = float(input('enter ur weight'))
height = float(input('enter ur height'))


bmi = calculate_BMI(weight, height)
category = check_category(bmi)

print(f"Your BMI is {bmi:.2f}")
print(f"You are {category}")