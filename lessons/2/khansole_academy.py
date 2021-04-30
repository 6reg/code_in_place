"""
Prints out randomly generated addition problem 
and checks if the user answers correctly.
"""

import random 

def main():
    # Generate two random two digit numbers
    first_num = random.randint(0,99)
    second_num = random.randint(0,99)
    
    # Add the two numbers together
    res = first_num + second_num

    # Print the problem to console
    print("What is " + str(first_num) + " + " + str(second_num) + "?")

    # Get user answer
    user_ans = input("Your answer: ")

    # Check if user answer is correct
    if res == int(user_ans):
        print("Correct!")
    else:
        print("Incorrect. The expected answer is " + str(res))
