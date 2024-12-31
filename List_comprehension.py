#Given a list of numbers, remove all odd numbers from the list:
numbers = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]

result = [i for i in numbers if i % 2 != 0]
print(f"odd numbers in the list {result}")

print("********************************")
#Given a list of numbers, remove floats (numbers with decimals)
original_list = [2, 3.75, .04, 59.354, 6, 7.7777, 8, 9]
only_int = [i for i in original_list if type(i) == int]
print(f"only integers in the list {only_int}")

print("********************************")
#Find all of the numbers from 1-1000 that are divisible by 7
num_Divible_by_100 = [i for i in range(1, 1000) if i % 7 == 0]
print(f"numbers divisible by 7 are {num_Divible_by_100}")

print("********************************")
#Find all of the numbers from 1-1000 that have a 3 in them
num_3 = [i for i in range(1, 1000) if '3' in str(i)]
print(num_3)

print("********************************")
#Count the number of spaces in a string
sen = "hello how are you doing?"
spaces = [i for i in sen if i == ' ']
print(f"count of spaces in the string is : {len(spaces)}")

print("********************************")
#Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
sen = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [i for i in sen if i not in vowels and i != ' ']
print(consonants)

print("********************************")
#Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)

items = ['hi', 4, 8.99, 'apple', ('t', 'b', 'n')]
index_value = [i for i in enumerate(items)]
print(index_value)

for i in range(0, len(items)):
    print((i, items[i]))

print("********************************")
#Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

list_c = [i for i in list_a if i in list_b]
print(list_c)

print("********************************")
#Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
sentence = "In 1984 there were 13 instances of a protest with over 1000 people attending"
numbers = [i for i in sentence.split() if i.isdigit()]
print(numbers)

print("********************************")
#Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’

numbers = ['even' if i % 2 == 0 else 'odd' for i in range(20)]
print(numbers)

print("********************************")
#Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]
list_c = [(i, i) for i in list_a if i in list_b]
print(list_c)

print("********************************")
#Find all of the words in a string that are less than 4 letters

sentence = 'Find all of the words in a string that are less than 4 letters'
sen = [i for i in sentence.split() if len(i) < 4]
print(sen)

print("********************************")
#Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)

digit = range(2, 10)
numbers = range(1,1000)
div = [(num,d) for num in numbers for d in digit if num%d == 0]

print(div)
