# print("Hello world!")
# range(2, 20)
# str(12)
# range(10, 20, 3)
# range(0, 100, 5)

# nums = [1, 3, 5, 2, 4]
# print(len(nums))

# letters = ["a", "b", "c"]
# letters += ["d"]
# print(len(letters))

# nums = [1, 2, 3]
# nums.append(4)
# print(nums)

# words = ["Python", "fun"]
# index = 1
# words.insert(index, "is")
# # print(type(words))
# # print(dir(words))
# # print(dir(insert))
# print(words)

# letters = ['p', 'q', 'r', 's', 'p', 'u']
# print(letters.index('r'))
# print(letters.index('p'))
# print(letters.index('q'))

# max(list): Returns the maximum value.
# min(list): Returns the minimum value.
# list.count(item): Returns a count of how many times an item occurs in a list.
# list.remove(item): Removes an item from a list.
# list.reverse(): Reverses items in a list.

# # Complete the code to remove the smallest and largest elements
# # # from the list and output the sum of the remaining numbers.
# data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]
# print(len(data))
# print(max(data))
# print(min(data))
# data.remove((max(data)))
# data.remove((min(data)))
# print(len(data))
# sum = 0
# for i in data:
#     print(i)
#     sum += i
# print(sum)