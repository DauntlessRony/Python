
# Underweight = less than 18.5
# Normal = more or equal to 18.5 and less than 25
# Overweight = more or equal to 25 and less than 30
# Obesity = 30 or more

# Sample Input
v_weight = float(input())
v_height = float(input())
# Sample Output = Normal
v_result = 0
v_height_s = (v_height*v_height)
v_result = v_weight/v_height_s
if v_result < 18.5:
    print('Underweight')
elif v_result >= 18.5 and v_result < 25:
    print('Normal')
elif v_result >= 25 and v_result < 30:
    print('Overweight')
else:
    print('Obesity')