with open(r"Class08_Assignment.txt", 'r') as f:
    contents = f.readlines()
    print(type(contents))
    print(contents)
    lines = len(f.readlines())
    print(type(lines))
    print(lines)
    print('Total Number of lines:', lines)

number_of_words = 0
with open(r'Class08_Assignment.txt','r') as f:
    data = f.read()
    lines = data.split()
    print(type(lines))
    print(lines)
    number_of_words += len(lines)
print(number_of_words)