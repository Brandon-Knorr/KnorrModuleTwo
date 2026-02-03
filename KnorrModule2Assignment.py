# Patrick Gerber
# Mod 2 Assignment 
# Groundhog Day

# BUDGET CALCULATOR

# the assignment calls for 2 functions and a decision tree 
# from my prior programming knowledge I know I would like to eventually encapsulate these into a class to manage the logic. This will make the code more reuseable 
# 
#   

# first i like to list out the requirements and create a solution then refactor from there. 

# - get pay periods from user
# - get amount of pay per period from user

print('=== Budget Calculator ===')

pay_periods = int(input('How many times are you paid each month: '))
pay_amount = float(input('How much is each paycheck (post-tax): $'))
monthly_income = pay_periods * pay_amount

