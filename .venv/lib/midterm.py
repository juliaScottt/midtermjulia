# Question 1
a = 10
a = a + 2
print(a*2)
a = 19
print(a+3)
a = a // 2

#Question 2
print((2+3)*6/2 and 18.0)

# Question 3
import datetime

a = 9
b = 3
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year


print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 4)
print(d)


#Question 4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
# Question 5
def find_patterns(text):
   count = 0

   for i in range(len(text)):
      if text[i] == 'C':

         for j in range(i + 2, len(text) - 7 ):

            if text[j:j + 6] == 'jeb':
               count += 1
               break

   return count


text_example = "Cabcjeb is a test string with C123jeb patterns and one without end Cnope."
pattern_count = find_patterns(text_example)
print("Found patterns:", pattern_count)

# question 6
original_string = "Hello"

try:
   original_string[0] = "k"
except TypeError as e:
   print(f"Error: {e}")

new_string = original_string + ", World!"
print(new_string)

print(original_string)

my_list = [8, 4, 9]
print(f"Original list: {my_list}")

my_list[0] = 10
print(f"Modified list: {my_list}")

my_list.append(8)
print(f"List after adding an element: {my_list}")

my_list.remove(6)
print(f"List after removing an element: {my_list}")




# Example usage
text = "Cabcjeb is a pattern, and so is Cdefghijeb, but not Cjebalone."


def find_pattern_occurrences(text):
    pass


print(find_pattern_occurrences(text))

# Question 7
import random

random_numbers = []
for i in range(10):
   random_numbers.append(random.randint(1, 100))

for i in range(len(random_numbers)):
   if random_numbers[i] > 70:
       random_numbers[i] = -random_numbers[i]

print(random_numbers)

import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here
# removing number greater than 50
import random

# Generating random numbers
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Removing numbers greater than 50 and replacing others with "XX"
final_numbers = ["XX" if number <= 50 else None for number in random_numbers]
final_numbers = [number for number in final_numbers if number is not None]

# Printing the final list
print(final_numbers)

# Question 8

def is_valid_url(url):
   # Check if it starts with http:// or https://
   if not (url.startswith("http://") or url.startswith("https://")):
      return False

   # Check if the URL contains a dot
   if '.' not in url:
      return False

   # Check if the URL contains spaces
   if ' ' in url:
      return False

   return True



# Question 9

from datetime import datetime


def days_passed_since_birthday(birthday_str):
    # Parsing the given birthday
    birthday = datetime.strptime(birthday_str, "%d-%m-%Y")

    # Getting today's date
    today = datetime.now()

    # Calculating age in years
    age_years = today.year - birthday.year

    # Adjust for if today's date is before the birthday in the current year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age_years -= 1

    # Assuming an average year length of 365.25 days to account for leap years
    days_passed = age_years * 365

    return int(days_passed)


# Using the specific birthday you provided: "11-08-2002"
print(days_passed_since_birthday("11-08-2002"))

# Question 10 --> upload to github

# birthyear question:

print(is_valid_url("https://www.juliaschott.com"))  # True
print(is_valid_url("www.juliaschott.com"))  # False


# Question 9
def calculate_days_since_birthday(birthday):
   current_year = 2024


   birth_year = int(birthday.split("/")[2])




   full_years_passed = current_year - 1 - birth_year




   days_passed = full_years_passed * 365




   leap_years = 0
   for year in range(birth_year + 1,
                     current_year):
       if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
           leap_years += 1




   days_passed += leap_years


   return days_passed




birthday_julia = "11/08/2002"
days_passed_julia = calculate_days_since_birthday(birthday_julia)
print(f"Days passed since Julia's birthday (excluding birth year and current year): {days_passed_julia}")