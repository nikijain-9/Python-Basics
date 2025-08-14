# =========================
# A) DICTIONARY
# =========================

'''
I. Accessing Values in a Dictionary

(Square Bracket Notation)

1. Create a dictionary of countries and capitals. Print the capital of "France".
2. Given a dictionary of fruits and their prices, access and print the price of "Mango".
3. Create a dictionary mapping employee IDs to names. Access and print the name for a specific ID.

(Using get() method)

4. Given a dictionary of students and grades, use get() to retrieve the grade of "Ravi".
5. Use get() to try to access a non-existing key and print a default message if it’s not found.
6. Store product names and quantities in stock. Use get() to check availability of "Laptop".

'''

#Task 1
countries = {"France": "Paris", "India": "New Delhi", "Japan": "Tokyo"}
print(f"Capital of France is {countries['France']}")

#Task 2
fruits = {"Apple": 50, "Mango": 70, "Banana": 20}
print(f"Price of Mango is {fruits['Mango']}")

#Task 3
employees = {101: "Alice", 102: "Bob", 103: "Charlie"}
print(f"ID 102 belongs to {employees[102]}")

#Task 4
students = {"Ravi": 85, "Meera": 90}
print(f"Grades of Ravi is: {students.get("Ravi")}")

#Task 5
products = {"Mobile": 10, "Headphones": 25}
print(products.get("Laptop", "Laptop Not in stock"))  # 6

'''
II. Adding New Key-Value Pairs

1. Start with an empty dictionary and add three books with their authors.
2. Given a dictionary of movie titles and release years, add a new movie.
3. Add a new key "Total Students" to a dictionary of classes and student counts.

'''

#Task 1

books = {}
books["Harry Potter"] = "J.K Rowling"
books["The Subtle art"] = "Mark Mansion"
books["The Alchemist"] = "Paulo Coelho"
print(books)

#Task 2
movies = {"Inception": 2010, "Interstellar": 2014}
movies["Jurassic Park"] = 1993
print(movies)

classes = {"Class A": 30, "Class B": 25}
classes["Total Students"] = 55
print(classes)

'''
III. Removing Key-Value Pairs

1. Create a dictionary of colors and hex codes. Remove the key "Red".
2. Given a dictionary of cities and populations, remove a city using pop().
3. Use popitem() to remove the last inserted key-value pair from a dictionary.
'''

#Task 1
colors = {"Red": "#FF0000", "Blue": "#0000FF", "Green": "#008000"}
del colors["Red"]
print(colors)

#Task 2
cities = {"Mumbai": 20000000, "Delhi": 18000000, "Pune": 6000000}
cities.pop("Mumbai")
print(cities)

#Task 3
sample_dict = {"a": 1, "b": 2, "c": 3}
sample_dict.popitem()
print(sample_dict)


'''
IV. Looping Through a Dictionary

1. Print all keys in a dictionary of programming languages and their creators.
2. Print all key-value pairs of a dictionary containing country names and their populations.
3. Print each student name and their marks from a dictionary.
'''

#Task 1
languages = {"Python": "Guido van Rossum", "Java": "James Gosling"}
for language in languages:
    print(language)

#Task 2
populations = {"India": 1.4, "USA": 0.33, "China": 1.42}
for country, population in populations.items():
    print(f"{country} : {population}")


#Task 3
marks = {"Anu": 88, "Ravi": 92, "Meera": 79}
for student, total_marks in marks.items():
    print(f"{student} : {total_marks}")


'''
V. Looping Through All Values

1. Create a dictionary of mobile brands and models. Print only the models.
2. Given a dictionary of subjects and marks, print all marks.
3. Create a dictionary of items and prices, and print only prices above 50.
'''

#Task 1
mobiles = {"Samsung": "Galaxy S23", "Apple": "iPhone 15"}
for model in mobiles.values():
    print(model)

#Task 2
subjects = {"Math": 95, "Science": 88, "History": 76}
for marks in subjects.values():
    print(marks)

#Task 3
items = {"Pen": 10, "Notebook": 60, "Bag": 120}
for price in items.values():
    print(price)


# =========================
# A) DICTIONARY Comprehension
# =========================

'''
VI. Transform a Dictionary

1. Given a dictionary of names and ages, create a new dictionary with names as keys and ages doubled.
2. Given a dictionary of temperatures in Celsius, create a new dictionary converting them to Fahrenheit.
3. Create a dictionary where each key is a number from 1–5 and value is its square.
'''

#Task 1
ages = {"Alice": 25, "Bob": 30}
doubled_ages = {name: age * 2 for name, age in ages.items()}
print(doubled_ages)

#Task 2
temps_c = {"Delhi": 30, "Mumbai": 28}
temps_f = {city: (temp * (9/5) + 32) for city, temp in temps_c.items()}
print(temps_f)

#Task 3
sqr_dict = {n: n ** 2 for n in range(1,6)}
print(sqr_dict)


'''
VI. Filter a Dictionary

1. Given a dictionary of students and marks, create a new dictionary with only students scoring above 75.
2. From a dictionary of items and prices, keep only items costing less than 100.
3. From a dictionary of words and their lengths, filter out words shorter than 5 letters.
'''

#Task 1
students_marks = {"Aman": 80, "Rita": 65, "Raj": 90}
top_students = {student: marks for student, marks in students_marks.items() if marks > 70}
top_students = {student: marks for student, marks in students_marks.items() if marks > 70}
print(top_students)

#Task 2
prices = {"Pen": 10, "Notebook": 60, "Bag": 120}
cheap_items = {pen: price for pen, price in prices.items() if price < 100}
print(cheap_items)

#Task 3
word_lengths = {"apple": 5, "hi": 2, "banana": 6}
short_words = {word: letter_count for word, letter_count in word_lengths.items() if letter_count < 5}
print(short_words)