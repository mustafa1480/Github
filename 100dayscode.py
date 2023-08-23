 Write your code below this line 👇
print("Welcome to the band name generator")
City_name = input("In which city you grew in? \n")
pet_name = input("What is the name of your pet? \n")
print("your band name is :" + City_name + " " + pet_name)

Number = input("Enter the Two Digit number: ")
x = int(Number[0])
y = int(Number[1])
print(x + y)

Num = int(input("Enter the Two Digit number: "))
# ================================================================
print(Num[0] + Num[1])


Num = input("Enter the Two Digit Number: \n")


x = int(Num[0])
y = int(Num[1])
print(x + y)
========================================================

weight = int(input("Enter your weight: \n"))
height = int(input("Enter your height \n"))

BMI = weight // (height**2)


print(f"Your BMI is: {BMI}")
=============================================================
                        DAYS-2

age = int(input("What is your current age?: \n"))

years_remaining = 90 - age
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

messege = f"you have {years_remaining}years, {months_remaining} months, {weeks_remaining},and {days_remaining}days left"
print(messege)
=================================================================
                     Tip Calculator
bill = float(input("What was the total bill? \n"))

tip = float(input("What percentage tip would you like to give? 10, 12, 15 \n"))
persons = float(input("How many people to spilt the bill? \n"))


tip_percentage = (tip/100)*bill + bill
contri = (tip_percentage / persons)
Final_amount = "{:.2f}".format(contri)
print(f"Each person should pay {Final_amount}")
========================================================================
                        Odd/Even
number = int(input("enter any number: "))

if number % 2 ==0:
  print("this number is even")
else:
  print("this number is odd")
================================================================
                OOP coffie machine
from menu import MenuItem, Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

while is_on:
  options = menu.get_items()
  choice = input(f"What would u like?({options}) \n")
  if choice == "off":
    is_on = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)

    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):

       coffee_maker.make_coffee(drink)
# ======================================================================
#                 BMI using If/else
height = float(input("Enter your height in m \n"))
weight = float(input("Enter your weight in kg \n"))

BMI = weight / height**2

if BMI <=18.5:
  print(f"your bmi is {BMI}you are underweight")
elif BMI < 25:
  print(f"your bmi is {BMI}you are normalweight")
elif BMI < 30:
  print(f"your bmi is {BMI}you are Overweight")
elif BMI <35:
  print(f"your bmi is {BMI}you are obese")
else:
  print(f"your bmi is {BMI}you are clinically obese")
======================================================================
                 Leap year
year = int(input("Enter any year \n"))

if year % 4 == 0 & year % 400 == 0 :
  if year % 100 == 0:
    print("not leap year")
  else:
    print("a leap year")
else:
  print("not a leap year")

OR
year = int(input("Enter a year \n "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0 :
      print("leap year")
    else:
      print("not a leap year")
  else:
    print(" leap year")
else:
  print("not leap year")
====================================================================
              Rollercoaster

print("welcome to the rollercoaster")
height = int(input("Enter your height \n"))
bill = 0
if height >= 120:
  print("you can ride the rolercoaster ")
  age = int(input("Enter your age \n"))
  if age < 12:
    bill = 5
    print("child ticket is $5")
  elif age <= 18:
    bill = 7
    print("youth ticket is $7")
  elif age>=45 and age<= 55:
    print("no ticket for you")
  else:
    print("adult ticket is $12")
    bill = 12
  want_photo = input("Do u need a photo, say Y or N \n")
  if want_photo == "Y":
    bill +=3
  print(f"Total bill is ${bill}")
else:
  print("sorry. you have to grow before you ride ")

=====================================================================
                     pizza order
print("Welcome to pizza corner")
size = input("what size of pizza you want? S, M, L \n")
add_pepperoni = input("Do u want pepperoni? Y or N \n")
extra_cheez = input("Do u want extra cheez? Y or N \n")

bill = 0

if size == "S":
  bill+=15
elif size =="M":
  bill+=20
elif size == "L":
  bill+=25
else:
  print("Enter the correct size")

if add_pepperoni == "Y":
  if size == "S":
    bill+=2
  else:
    bill+=3
if extra_cheez == "Y":
  bill+=1

print(f"Final bill is ${bill}")
====================================================================
                     Love calculator

print("welcome to the lovev calculator \n")
name1 = input("enter 1st name \n")
name2 = input("enter 2nd name \n ")

combined_names = name1 + name2
lowered_name = combined_names.lower()
t = lowered_name.count("t")
r = lowered_name.count("r")
u = lowered_name.count("u")
e = lowered_name.count("e")

true = t + r + u + e

l = lowered_name.count("l")
o = lowered_name.count("o")
v = lowered_name.count("v")
e = lowered_name.count("e")

love = l + o + v + e

trueloves_score = int(str(true) + str(love))

if (trueloves_score<10) and (trueloves_score>90):
  print(f"your score is {trueloves_score}, excellent")
elif (trueloves_score>=40 and trueloves_score<=50):
  print(f"your score is {trueloves_score},very good")
else:
  print(f"your score is {trueloves_score}, good")

================================================================
             Trasure Game
print("Welcome to the treasure island, your mission is to find the treasure \n")
step1 = input("do u wanna take left or right? L or R \n")
if step1 == "L":
  print("you can go ahead \n")
  step2 = input("do u wanna swim or wait? S or W \n")
  if step2 == "W":
    print("you can go ahead \n")
    door = input("which door do u wanna go? R or B or Y")
    if door == "Y":
      print("you win!!!!")
    else:
      print("you lose")
  else:
    print("game over")
else:
  print("game over")

=============================================================
                  random
import random

names_string = input("Enter the names seperated by comma.\n")
names = names_string.split(",")
name_len = len(names)
random_choice = random.randint(0,name_len-1)
print(random_choice)
print(names[random_choice])

or

import random
names_string = input("Enter the names seperated by comma.\n")
names = names_string.split(",")

name_choice = random.choice(names)

print(name_choice)

==========================================================
                    List
list = ["sal","zee", "mat", "ridd", "aff", "sheb"]
# # # print(list)
# # # #           #To extract a name
# # # print(list[1])
# # #           #To add a name in a list
# # list.append("bollu")
# # #           #To add a list in a list
# # # list.extend(["sam", "james", "don"])
# # print(list)
lenght_of_list = len(list)
print(lenght_of_list)
# print(list[5])

print(list[lenght_of_list -1)

========================================
              Rock, paper, scissor Game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Write your code below this line 👇
import random
list = [rock, paper, scissors]
my = int(input("Enter rock=0, paper=1, scissors=2 \n"))
print(list[my])
if my<0 or my>=3:
  print("you have typed an invalid number")
else:
  comp = random.randint(0, 2)
  comp_choice = list[comp]
  print(comp)
  print(list[comp])

  if my<0 or my>=3:
    print("you have typed an invalid number")
  elif my == 0 and comp == 2:
    print("you win!")
  elif my == 2 and comp == 0:
    print("you lose")
  elif my > comp:
    print("you win!")
  elif my == 0 and comp == 1:
    print("you lose!")
  elif my == 1 and comp == 2:
    print("you lose!")
  elif my == comp:
    print("Its a draw")
========================================
                        nested list

fruits = ["apple", "banana", "orange", "watermelon"]
vegetables = ["tomato", "potato", "brinjal", "cucumber"]

list_all = [fruits,vegetables]

print(list_all[1][2])

===========================================================


row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where u want to put x \n")
horizontal_pos = int(position[0])
vertical_pos = int(position[1])

map[vertical_pos - 1][horizontal_pos -1] = "X"

print(f"{row1}\n{row2}\n{row3}")
===========================================================
                Loop

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
  print(fruit)
  print(fruit + "pie")
print(fruits)
==============================================================
              To find the average height using FOR LOOP
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(student_heights)


heights = sum(student_heights)
num = len(student_heights)

print(heights, num)
                  OR
students_heights = input("input a list of heights \n").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

#For LEN of students
num_of_students = 0
for num_of_students in students_heights:
    num_of_students+=1
print(num_of_students)

#For SUM od students
total_height = 0
for student in students_heights:
    total_height+=student
print(total_height)

print(total_height / num_of_students)

===============================================================================================
 #                   checking highest score
student_score = input("input the score \n").split()

for n in range(0, len(student_score)):
  student_score[n] = int(student_score[n])
print(student_score)

highest_score = 0
for score in student_score:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is ({highest_score})" )
====================================================================================================
   MOST asked question in an interview
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
====================================================================================================
#                   Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []
for letter in range(0, nr_letters):
  random_let = random.choice(letters)
  password +=random_let     #OR password.append(random_let)
for symb in range(0, nr_symbols):
  random_symb = random.choice(symbols)
  password += random_symb
for num in range(0, nr_numbers):
   random_num = random.choice(numbers)
   password += random_num
random.shuffle(password)   #To shuffle a list

real_password = ""
for char in password:
  real_password += char
print(real_password)
====================================================================================================
                      Functions
def greet_with(name, location):
  print(f"what's your name: {name}")
  print(f"what's  your loaction:{location}")

greet_with("salman","hyd")                            <== Positional Argument
greet_with(location = "hyd", name = "salman")         <== keyword Argument

====================================================================================================
                    Prime Number
def prime_num(number):
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False

    if is_prime:
        print("It is a prime number")
    else:
        print("Not a prime number")


num = int(input("Enter a number \n"))
prime_num(number=num)
====================================================================================================

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":

    def encrypt(plane_text, shift_amount):
        cipher_text = ""
        for letter in plane_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter

        print(f"The encoded text is {cipher_text}")


    encrypt(plane_text=text, shift_amount=shift)
elif direction == "decode":

    def decrypt(cipher_text, shift_amount):
        actual_word = ""
        for letter in alphabet:
            new_position = alphabet.index(letter)
            old_position = position - new_position
            old_letter = alphabet[old_position]
            actual_word += old_letter

        print(f"The decoded text is {actual_word}")


    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Enter the word correctly")

OR
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

print(logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

====================================================================================================

                                       Hangman Game

import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo

print(logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages

    print(stages[lives])
====================================================================================================
##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

######################################

#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
==================================================================================================
student_scores = {
    "Harry": 81,
    "salman": 71,
    "zeeshan": 63,
    "mat": 52
}
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceed expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
===> Project==============================================================
Adding new entries in the list
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["paris", "Lili", "Di jon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["berlin", "Hamburg", "stuttgrat"]
    }
]
country_name = str(input("Enter a country \n"))
visits_num = int(input("Enter the number of visits \n"))
cities_name = []
cities_name.append(str(input("Enter the city name \n")))


def add_new_county(country, visits, cities):
    new_log = {}
    new_log["county_name"] = country
    new_log["visits_num"] = visits
    new_log["cities_name"] = cities
    travel_log.append(new_log)


add_new_county(country=country_name, visits=visits_num, cities=cities_name)

print(travel_log)
==================================================================================================
                                        Bidding Game
from replit import clear
from art import logo
print(logo)

def find_highest_bidder(bid_record):
  highest_bid = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with the bid amount ${highest_bid}")

bidding_started = True
bid = {}
while bidding_started:
  name = input("Enter your name \n ")
  price = int(input("Enter your bid \n"))
  bid[name] = price
  ask_person = input("who wants to bid yes or no? \n")
  if ask_person == "yes":
    clear()
  else:
    bidding_started = False
    find_highest_bidder(bid)
==================================================================================================
                                      Calculator
def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1  = int(input("what's the first number \n"))
for symbol in operations:
  print(symbol)
operation_symbol = input("Select an operator \n")
num2 = int(input("what's the second number \n"))

calculation_function = operations[operation_symbol]

answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

================================================================================================================
                                        CAPSTONE PROJECT
# ==============================================================================================================
import random

from replit import clear()
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take the list of cards and return the score Calculate from the cards """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    if computer_score == 0:
        return "Lose, opponent has Blackjack"
    if user_score == 0:
        return "Win with a blackjack"
    if user_score > 21:
        return "You went over, you lose"
    if computer_score > 21:
        return "You win"
    if user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_cards = []
    computer_cards = []
    is_gameover = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_gameover:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your card: {user_cards}, current score {user_score}")
        print(f"computer card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_gameover = True
        else:
            user_should_deal = input("Type 'y' to get another card and 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_gameover = True

    while computer_score != 0 and computer_score > 17:
        computer_cards.append(deal_card())
        computer_score.calculate_score(computer_cards)
    print(f" Your final hand {user_cards}, final score {user_score}")
    print(f" computer cards {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you wanna play? 'y' for yess and 'n' for no"):
    clear()
    play_game()
==================================================================================================
              # Number Guessing Game Objectives:
import random
random_number = random.randint(1,100)
# print(random_number)       # For checking
attempts_easy = 10
attempts_hard = 5

difficulty = input("Choose a difficulty, 'easy' or 'hard' \n" ).lower()

end_game = False

while not end_game:

  if difficulty == "easy":
    guess = int(input("Take a guess:  "))
    if guess > random_number:
      print("Too high")
    elif guess < random_number:
      print("too low")
    attempts_easy -=1
    print(f"You have {attempts_easy} attempts left ")
    if guess == random_number:
      print("You Won!")
      end_game = True
  if attempts_easy == 0:
    print("You lose!")
    end_game = True
  elif difficulty == "hard":
    guess = int(input("Take a guess:  "))
    if guess > random_number:
      print("Too high")
    elif guess < random_number:
      print("too low")
    attempts_hard -=1
    if attempts_hard == 0:
      print("You lose!")
      end_game = True
    print(f"You have {attempts_hard} attempts left \n")
    if guess == random_number:
      print("You Won!")
      end_game = True
===============================================================================================================
                                      Higher Lower
import random
from game_data import data
from art import logo, vs
from replit import clear


# functions
def account_detail(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
game_continue = True
account_b = random.choice(data)
score = 0

while game_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {account_detail(account_a)}.")
    print(vs)
    print(f"Against B: {account_detail(account_b)}. \n")

    guess = input("Who has more followers, Type A or B  ").lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1

        clear()
        print(logo)
        print(f"You're right!, Current score {score}")
#
#     else:
#         game_continue = False
#         print(f"Sorry that's wrong!,final score {score}")
