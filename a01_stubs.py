######################################################################
# Author: Jose Zapata
# Username: zapatamezaj
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
my_input = input('Please enter the year you were born: ')

# TODO Check the year using if conditionals, and print the correct animal for that year.
if my_input == '1999':
    print('Do you like carrots? You are a Rabbit!')
elif my_input == '1998':
    print('ROAR! You are a tiger!')
elif my_input == '1997':
    print('Do not have a cardi YAK attack, you are an ox!')
elif my_input == '1996':
    print('Careful around cats, you are a rat!')
elif my_input == '1995':
    print("OINK OINK! You are a pig")
elif my_input == '1994':
    print('WOOF! You are a dog!')
elif my_input == '1993':
    print('Cock-A-Doodle-Do! You are a rooster!')
elif my_input == '1992':
    print('Do you like bananas? Because you are a monkey!')
elif my_input == '1991':
    print("Don't eat this code! You're a goat!")
elif my_input == '1990':
    print('Hello neigh-bor! You are a horse!')
elif my_input == '1989':
    print('HISS! You are a snake!')
elif my_input == '1988':
    print('You like castles! You are a dragon!')
else:
    print('Try another year!')

######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
my_input_friend = input('Please enter the year your friend was born: ')

# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year
if my_input_friend == '1999':
    print('Do you like carrots? You are a Rabbit!')
elif my_input_friend == '1998':
    print('ROAR! You are a tiger!')
elif my_input_friend == '1997':
    print('Do not have a cardi YAK attack, you are an ox!')
elif my_input_friend == '1996':
    print('Careful around cats, you are a rat!')
elif my_input_friend == '1995':
    print("OINK OINK! You are a pig")
elif my_input_friend == '1994':
    print('WOOF! You are a dog!')
elif my_input_friend == '1993':
    print('Cock-A-Doodle-Do! You are a rooster!')
elif my_input_friend == '1992':
    print('Do you like bananas? Because you are a monkey!')
elif my_input_friend == '1991':
    print("Don't eat this code! You're a goat!")
elif my_input_friend == '1990':
    print('Hello neigh-bor! You are a horse!')
elif my_input_friend == '1989':
    print('HISS! You are a snake!')
elif my_input_friend == '1988':
    print('You are COOL and OLD! You are a dragon')
else:
    print('Try another year!')

######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
