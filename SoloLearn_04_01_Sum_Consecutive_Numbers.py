# Take a number N as input and output the sum of all numbers from 1 to N (including N).
# Sample Input = 100
# Sample Output = 5050
# Explanation: The sum of all numbers from 1 to 100 is equal to 5050.

# v_input = 10
# v_number = v_input+1
# r_input = range(v_number)
# print(r_input)
# sum = 0
# for i in r_input:
#     print(i)
#     print(type(i))
#     sum+=i
# print(sum)



v_input = int(input())
v_number = v_input+1
r_input = range(v_number)
print(r_input)
sum = 0
for i in r_input:
    print(i)
    sum+=i
print(sum)