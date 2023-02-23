total = 0
while True:
    try:
        age = int(input('enter the age:'))
        # 18 24 2 5 42 = 400
        # 20 32 2 1 2 = 200
    except:
        break
    if age>2:
        print("The age of the customer is greater than 3. So, Charge the bill.")
        total += 100
        continue
    # else:
    #     continue
print(total)
