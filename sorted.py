numbers = [6, 9, 3, 1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  

my_dict = {6: 3, 5: 4, 1: 6}
print(sorted(my_dict))  

tup = (3, 6, 8, 2, 78, 1, 23, 45, 9)
sorted_tup = sorted(tup)
print(sorted_tup)  


words = ["apple", "banana", "cherry"]
words.sort(key=lambda word: word[-1])
print(words)  
