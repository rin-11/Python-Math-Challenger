# GOAL: randomnly generate math questions for user to calculate
        # user cannot move on until the answer is correct
        # set timer

import random
import time

#variables
OPERATORS = ["+", "-",  "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    #select random operators and random intergers
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    #create expression string
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0 #variable to keep track of the number of incorrect answers
input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer): #check exptression
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("FINISHED! ALL 10 PROBLEMS WERE ANSWERED CORRECTLY IN", total_time, "SECONDS.")
