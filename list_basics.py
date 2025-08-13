'''
1. List
(Introduce you to the list type and how to manipulate list elements effectively)

Create a list of 5 favorite movies. Add two more movies at the end and print the updated list.

Replace the 3rd movie in the list with a new movie name.

Remove the last movie from the list and print the remaining movies.
'''

#Task 1
movies = ['Toy Story', 'WallE', 'Insidious']

movies.append('Matrix')
movies.append('Avatar')
print(movies)

#Task 2
movies[2] = 'Big Hero 6'
print(movies)

#Taks 3
movies.pop()
print(movies)

'''
2. Tuple
(List that doesn’t change throughout the program)

Create a tuple of 5 country names and print each country on a separate line.

Check if "India" is present in the tuple, and print an appropriate message.

Convert the tuple into a list, add one new country, and convert it back to a tuple.
'''

countries = ('Russia', 'Japan', 'China', 'India', 'America')

#Task 1
print("Countries below")
for index, country in enumerate(countries):
    print(f"{index}: {country}")

#Task 2
country = 'Nepal'

if country in countries:
    index_of_country = countries.index(country)
    print(f"{country} exists in the list at {index_of_country}")
else:
    print(f"{country} doesn't exist in Countries list")

#Task 3
tuple_to_list = list(countries)
print(tuple_to_list)

tuple_to_list.append('Yemen')
list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)

'''
3. Sort a List in Place (sort())
(Use sort() method to sort a list in place)

Given the list [34, 2, 56, 7, 23], sort it in ascending order and print it.

Sort the same list in descending order.

Sort a list of words ["banana", "apple", "cherry"] alphabetically.
'''
numbers = [34, 2, 56, 7, 23]

#Task 1
numbers.sort()
print(numbers)

#Task 2
numbers.sort(reverse=True)
print(numbers)

#Task3
fruits = ["banana", "apple", "cherry"]
fruits.sort()
print(fruits)

'''
4. Sort a List (sorted())
(Return a new sorted list without changing the original)

Given [10, 3, 45, 7], create a new sorted list without altering the original list.

Sort the list ["pear", "apple", "banana"] into alphabetical order and store it in a new list.

Sort [5, 9, 1, 2] in descending order without modifying the original list.
'''

#Task 1
numerics = [10, 3, 45, 7]
sorted_numerics = sorted(numerics)
print(sorted_numerics)

#Task 2
fruits_new = ["pear", "apple", "banana"]
sorted_fruits = sorted(fruits_new)
print(sorted_fruits)

#Task 3
numbers_new = [5, 9, 1, 2]
sorted_numbers = sorted(numbers_new, reverse = True)
print(sorted_numbers)

'''
5. Slice a List
(Use slicing technique to manipulate lists)

From the list [1, 2, 3, 4, 5, 6, 7], extract elements from index 2 to 5.

Get every second element from the list [10, 20, 30, 40, 50].

Reverse the list [1, 2, 3, 4, 5] using slicing.
'''

#Task 1
numbers01 = [1, 2, 3, 4, 5, 6, 7]
ext_list = numbers01[2:6]
print(ext_list)

#Task 2
numbers02 = [10, 20, 30, 40, 50]
sliced_nums = numbers02[::2]
print(sliced_nums)

#Task 3
numbers03 = [1, 2, 3, 4, 5]
reversed_list = numbers03[::-1]
print(reversed_list)

'''
6. Unpack a List
(Assign list elements to multiple variables)

Unpack [1, 2, 3] into three separate variables a, b, c and print them.

Unpack [1, 2, 3, 4, 5] into first, second, and a list of remaining numbers.

Swap two variables x = 10 and y = 20 using list unpacking.
'''

#Task 1

numbers04 = [1,2,3]
a, b, c = numbers04
print(f"a: {a}, b: {b}, c: {c}")

#Task 2
numbers05 = [1, 2, 3, 4, 5]
first, second, *others = numbers05
print(f"first: {first}, seond: {second}, others: {others}")

#Task 3
x = 10
y = 20
x, y = y, x
print(f"x: {x}, y: {y}")

'''
7. Iterate over a List
(Use a for loop to iterate)

Print each element of [2, 4, 6, 8] multiplied by 2.

Iterate over ["dog", "cat", "rabbit"] and print the length of each string.

Iterate over [5, 10, 15] and calculate the sum of all numbers.
'''

#Task 1
numbers06 = [2, 4, 6, 8]
doubled_list = []

for num in numbers06:
    doubled_list.append(num * 2)

print("doubled_list", doubled_list)

#Task 2
animals = ["dog", "cat", "rabbit"]
for char in animals:
    print(f"{char}: {len(char)}")

#Task 3
nums07 = [5, 10, 15]
sum_of_nums = 0
for num in nums07:
    sum_of_nums += num

print(sum_of_nums)


'''
8. Find the Index of an Element
(Find index of the first occurrence)

Find the index of 7 in [3, 7, 2, 7, 5].

Find the index of "apple" in ["banana", "apple", "cherry"].

Check if "mango" exists in the list; if yes, print its index, otherwise print "Not Found".
'''
#Task 1
nums08 = [3, 7, 2, 7, 5]
print(nums08.index(7))

#Task 2
fruits01 = ["banana", "apple", "cherry", "mango"]
print(fruits01.index('apple'))

#Task 3
if 'mango' in fruits01:
    print(f"Index of Mango is {fruits01.index('mango')}")
else:
    print("mango does not exist in the list")


'''
9. Transform List Elements with map()
(Use map() to transform list elements)

Convert a list of strings ["1", "2", "3"] into integers.

Given [2, 4, 6], create a new list where each element is squared.

Convert ["apple", "banana", "cherry"] into uppercase strings.
'''

#Task 1
nums09 = ["1", "2", "3"]
conv_list= list(map(lambda n: int(n), nums09))
print(conv_list)
print(type(conv_list[1]))

#Task 2
nums10 = [2, 4, 6]
sqrd_list = list(map(lambda n: n ** 2, nums10))
print(sqrd_list)

#Task 3
fruits03 = ["apple", "banana", "cherry"]
cap_fruits = list(map(lambda fr: fr.upper(), fruits03))
print(cap_fruits)


'''
10. Filter List Elements with filter()
(Use filter() to filter list elements)

From [1, 2, 3, 4, 5], filter out only even numbers.

From ["apple", "bat", "cat", "door"], filter words with length greater than 3.

From [10, 15, 20, 25], filter numbers divisible by 5.
'''

#Task 1
nums11 = [1, 2, 3, 4, 5]
even_nums = list(filter(lambda n: n % 2 == 0, nums11))
print(even_nums)

#Task 2
fruits04 = ["apple", "bat", "cat", "door"]
big_name_fruits = list(filter(lambda fr: len(fr) > 3, fruits04))
print(big_name_fruits)

#Task 3
nums12 = [10, 15, 20, 25, 14]
div_by_five = list(filter(lambda n: n % 5 == 0, nums12))
print(div_by_five)

'''
11. List Comprehensions
(Create a new list based on an existing list)

From [1, 2, 3, 4], create a list where each element is squared.

From [1, 2, 3, 4, 5, 6], create a list containing only even numbers.

Create a list of all characters from the string "hello".]
'''
#Task 1
nums13 = [1, 2, 3, 4]
squared_nums = [num ** 2 for num in nums13]
print(squared_nums)

#Task 2
nums14 = [1, 2, 3, 4, 5, 6]
even_num_list = [num for num in nums14 if num % 2 == 0]
print(even_num_list)

#Task 3
greet = "hello"
string_char_list = [char for char in greet]
print(string_char_list)


