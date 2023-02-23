squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

# start and end
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

# step
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

# backward index
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

# Given a string as input, output its reverse.
# Sample Input: hello world
# Sample Output: dlrow olleh
# v_forward_text = input('enter your text to reverse it: ')
v_forward_text = 'hello world'
print(v_forward_text[::-1])

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])
# index 7 = 49, index 5 = 25; So = 25(end index), 36, 49(start index)
# Rearrange = 49(start index), 36, 25(end index)
# exclude last index; So, result will be 49, 36

for i in range(10):
    v1 = i
    print('v1=' + str(i))
    if not i % 2 == 0:
        v2 = i
        print('not enter in if=' + str(i))
        print('all=' + str(i+1))

for i in range(10):
  if not i % 2 == 0:
    print(i+1)

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

x = [2, 4]
x += [6, 8]
print(x[2]//x[0])

print(5 // 2)
print( 7%2 )
print( 7%(5 // 2) )

print("42" + '5')

if (1 == 1) and (2 + 2 > 3):
  print("true")
else:
  print("false")

x = 'amistu'
print(x[0:3])

x = [6, 4, 2, 9]
x = x[::-1]
print(x)
print(x[0]+x[2])