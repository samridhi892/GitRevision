#Create a dictionary of squares of numbers from 1 to 10
import string

d = {num: num * num for num in range(1, 10)}
print(d)
print("********************")

#2. Create a dictionary of even numbers as keys and their squares as values
d = {num: num * num for num in range(1, 11) if num % 2 == 0}
print(d)
print("********************")

#3. Create a dictionary of words and their lengths from a sentence
sent = "Create a dictionary of words and their lengths from a sentence"
d = {word: len(word) for word in sent.split()}
print(d)

print("********************")
#4. Create a dictionary of lowercase characters from a string
letters = "Create A Dictionary of lowercase characters from a string"
d = {char: char.lower() for char in letters}
print(d)

print("********************")
#5. Create a dictionary of numbers and their cubes
d = {num: num * num * num for num in range(2, 10)}
print(d)

print("********************")
#6. Create a dictionary of numbers and their squares, excluding odd numbers
d = {num: num * num for num in range(1, 11) if num % 2 == 0}
print(d)

print("********************")


#7. Create a dictionary of numbers and their prime status

def check_prime(n):
    flag = False
    if n == 0 or n == 1:
        return "0 or 1 number is not a prime number"
    for i in range(2, n):
        if n % i == 0:
            flag = True
            break
    if flag:
        return "not prime"
    else:
        return " is  prime"


d = {num: check_prime(num) for num in range(3, 12)}
print(d)

print("********************")
#8. Create a dictionary of characters and their ASCII values from a string
text = "Create a dictionary of characters and their ASCII values from a string"
d = {char: ord(char) for char in text}
print(d)

print("********************")
#9. Create a dictionary of words and their vowels from a list of strings
words = ["Create", "a", "dictionary"]
vowels = ['a', 'e', 'i', 'o', 'u']

d = {word: sum(1 for char in word if char.lower() in 'aeiou') for word in words}
print(d)

print("********************")
#10. Create a dictionary of words with the letters sorted
text = ["Create", "a", "dictionary"]
d = {word: ''.join(sorted(word)) for word in text}
print(d)

print("********************")
#Create a dictionary of words and their lengths, but only for words with more than 5 letters
sample = ['apple', 'banana', 'cherry', 'date']
d = {word: len(word) for word in sample if len(word) > 5}
print(d)

print("********************")
#12. Create a dictionary of characters and their frequency in a string
sample = "hello world"
d = {char: sample.count(char) for char in sample if char != ' '}
print(d)

print("********************")
#13. Create a dictionary of words and their reversed forms
sample = ['apple', 'banana', 'cherry']
d = {word: word[::-1] for word in sample}
print(d)

print("********************")
#14. Create a dictionary of numbers and their squares, but only for even numbers
d = {num: num * num for num in range(2, 11) if num % 2 == 0}
print(d)

print("********************")


#15. Create a dictionary of numbers and their factors
def fact(n):
    fac = []
    for i in range(1, n + 1):
        if n % i == 0:
            fac.append(i)
    return fac


d = {num: fact(num) for num in range(1, 10)}
print(d)

print("********************")
#16. Create a dictionary of words and their uppercase forms
sample = ['apple', 'banana', 'cherry']
d = {word: word.upper() for word in sample}
print(d)

print("********************")


#17. Create a dictionary of numbers and their parity (even or odd)
def check(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'


d = {num: check(num) for num in range(1, 11)}
print(d)

d = {num: 'even' if num % 2 == 0 else 'odd' for num in range(1, 6)}
print(d)

print("********************")
#18. Create a dictionary of numbers and their binary representations

d = {num: bin(num) for num in range(1, 5)}
print(d)

print("********************")


#19Create a dictionary of numbers and their factorials
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


d = {num: factorial(num) for num in range(1, 6)}
print(d)

print("********************")
#20. Create a dictionary of numbers and their squares, but only for multiples of 3
d = {num: num * num for num in range(1, 10) if num % 3 == 0}
print(d)

print("********************")
#21. Create a dictionary of numbers and their powers of 2

d = {num: 2 ** num for num in range(1, 5)}
print(d)

print("********************")
#22. Create a dictionary of words and their vowels, excluding words with no vowels
sample = ['apple', 'banana', 'cherry', 'dog', 'cat']


def check_word(word):
    v = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char in v:
            return word.count(char)


d = {word: check_word(word) for word in sample}
print(d)

print("********************")
#23. Create a dictionary of strings by replacing vowels with underscores
sample = ['apple', 'banana', 'cherry']


def check_vow(word):
    v = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char in v:
            word = word.replace(char, '_')
    return word


d = {word: check_vow(word) for word in sample}
print(d)

print("********************")
#24. Create a dictionary of words and their lengths, but only for words starting with 'a'
sample = ['apple', 'banana', 'cherry', 'date']

d = {word: len(word) for word in sample if word[0] == 'a'}
print(d)

print("********************")
#25. Create a dictionary of strings by repeating each word thrice
sample = ['apple', 'banana', 'cherry']
d = {word: 3 * word for word in sample}
print(d)

print("********************")
#26. Create a dictionary of strings with words containing 'a' and their lengths
sample = ['apple', 'banana', 'cherry', 'date']
d = {word: len(word) for word in sample if 'a' in word}
print(d)

print("********************")
#27. Create a dictionary of numbers and their squares, but only for numbers greater than 5

d = {num: num * num for num in range(1, 10) if num > 5}
print(d)

print("********************")
#28. Create a dictionary of characters and their ASCII values from a string, excluding non-alphabetic characters
sample = "Hello123"
d = {char: ord(char) for char in sample if not char.isdigit()}
print(d)

print("********************")
#29. Create a dictionary of words and their uppercase forms, excluding words with no uppercase letters
sample = ['apple', 'Banana', 'cherry', 'Date']
d = {word: word.upper() for word in sample if any(char.isupper() for char in word)}
print(d)

print("********************")
#30. Create a dictionary of strings with words containing more than 4 letters
sample = "Python is a powerful and versatile programming language"
d = {word: len(word) for word in sample.split() if len(word) > 4}
print(d)

print("********************")
#31. Create a dictionary of words and their first letter capitalized
sample = ['apple', 'banana', 'cherry']
d = {word: word.capitalize() for word in sample}
print(d)

print("********************")
#32. Create a dictionary of strings with vowels removed
sample = ['apple', 'banana', 'cherry']


def remove_vow(word):
    v = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char in v:
            word = word.replace(char, '')
    return word


d = {word: remove_vow(word) for word in sample}
print(d)

print("********************")
#33. Create a dictionary of numbers with their signs reversed
numbers = [5, -10, 15, -20, 25]
d = {num: -num for num in numbers}
print(d)

print("********************")
#34 .Create a dictionary of strings with words in reverse

text = "Python is fun"
# splitted = text.split()[::-1]
# for index in range(0,len(splitted)):
#      print(index,splitted[index])

d = {index: text.split()[::-1][index] for index in range(0, len(text.split()))}
print(d)

print("********************")


#35. Create a dictionary of numbers with their divisors

def divisor(n):
    div = []
    for i in range(1, n + 1):
        if n % i == 0:
            div.append(i)
    return div


d = {num: divisor(num) for num in range(1, 6)}
print(d)

print("********************")
#36. Create a dictionary of characters and their counts, excluding whitespace characters, from a string
sample = "hello world"
d = {char: sample.count(char) for char in sample if char != ' '}
print(d)

print("********************")
#37. Mapping lowercase letters to their ASCII values

print("********************")


#38. Numbers and their factorial from 1 to 10

def check_factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


d = {num: check_factorial(num) for num in range(1, 11)}
print(d)

print("********************")
#39. Numbers and their binary representation from 1 to 10
d = {num: bin(num) for num in range(1, 11)}
print(d)

print("********************")
#40. Pairs of distinct elements and their absolute difference from two lists
sample1 = [3, 6, 9]
sample2 = [5, 10, 15]

d = {(x, y): abs(x - y) for x in sample1 for y in sample2}
print(d)

print("********************")
#41. Pairs of distinct elements and their character position sum from two lists
input1 = ['abc', 'def', 'ghi']
input2 = ['jkl', 'mno', 'pqr']

d = {(x, y): sum(ord(char) for char in x) + sum(ord(char) for char in y) for x in input1 for y in input2}
print(d)

print("********************")
#42. Distinct words and their length, excluding those with odd lengths, in a sentence
sample = "Hello, how are you?"
d = {word: len(word) for word in sample.split() if len(word) % 2 == 0}
print(d)

print("********************")
#43. Distinct words and their length, excluding those with even lengths, in a sentence
sample = "Hello, how are you?"
d = {word: len(word) for word in sample.split() if len(word) % 2 != 0}
print(d)

print("********************")
#44. Characters and their occurrence count, excluding punctuation, in a sentence
sample = "Hello, how are you?"
d = {word: sample.count(word) for word in sample if word not in string.punctuation}
print(d)

#45. Distinct words and their length, excluding those with lengths not Fibonacci, in a sentence

print("********************")
#46. Mapping words to their frequency of containing the letter 'e'
sample = "Hello, how are you?"

d = {word: word.count('e') for word in sample.split()}
print(d)

print("********************")
#47. Mapping characters to their position in the alphabet

#48. Mapping words to their palindrome status in a sentence
sample = "madam sees the racecar"
d = {word: True if word[::-1] == word else False for word in sample.split()}
print(d)

print("********************")
#49. Mapping numbers to their binary and hexadecimal representations

#50. Mapping words to their reverse in a sentence
sample = "Hello, how are you?"

d = {word:word[::-1] for word in sample.split()}
print(d)
