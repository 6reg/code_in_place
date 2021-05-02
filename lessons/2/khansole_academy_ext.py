
"""
while total < 3
    additionProblem()
    if userAns == Ans
    total = total + 1
"""

import random



def main():
    
    count = 1

    while count < 4:
        first_num = random.randint(0,99)
        second_num = random.randint(0,99)
        res = first_num + second_num
        
        print("What is " + str(first_num) + " + " + str(second_num) + "? ")

        user_ans = input("Your anwser: ")

        
        if res == int(user_ans):
            print("Correct! You've gotten " + str(count) + " correct in a row.")
            count = count + 1
        else: 
            print("Incorrect. The expected answer is " + str(res))
            count = 1
    print("Congratulations! You mastered addition.")



