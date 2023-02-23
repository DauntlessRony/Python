# add start
def add(x):
    print(x)
    sum=0
    for i in x:
        sum+=i
    return sum

v_list = []
v_tuple = ()
while True:
    try:
        a = float(input('Enter Value: '))
    except:
        break
    if a:
        v_list.append(a)
        v_tuple=tuple(v_list)
        continue
print(v_tuple)
print(add(v_tuple))

# add end


# sub start
def sub(x):
    print(x)
    sub=0
    for i in x:
        sub=i-sub
    return sub

v_list = []
v_tuple = ()
while True:
    try:
        a = float(input('Enter Value: '))
    except:
        break
    if a:
        v_list.append(a)
        v_tuple=tuple(v_list)
        continue
print(v_tuple)
print(sub(v_tuple))

# sub end

# mul start
def mul(x):
    print(x)
    mul=1
    for i in x:
        mul*=i
    return mul

v_list = []
v_tuple = ()
while True:
    try:
        a = float(input('Enter Value: '))
    except:
        break
    if a:
        v_list.append(a)
        v_tuple=tuple(v_list)
        continue
print(v_tuple)
print(mul(v_tuple))

# mul end

# div start

def div(x,y):
    print(x,'/',y)
    if y!=0:
        return x/y
    else:
        'Invalid'

print(div(float(input('Enter Value Dividend: ')),float(input('Enter Value Divisor: '))))


# div end