# Sample Input 23
# Sample Output 5 10 15 20
v_input = int(input())
r_all_floor = range(v_input)
for i in r_all_floor:
    # print('floor number: ' + str(i))
    # print('Getting 5ht floor number: ' + str(i//5))
    if i//5 == 0:
        print('Every 5th floor: ' + str(i))