# Sample Input 23
# Sample Output 5 10 15 20
while True:
    try:
        v_input = int(input('How many floor are there in your building ? '))
    except:
        break
    if v_input:
        r_only_fifth_floor = range(5,v_input, 5)
        print(r_only_fifth_floor)
        for i in r_only_fifth_floor:
            print('Every 5th floor: ' + str(i))
        continue
