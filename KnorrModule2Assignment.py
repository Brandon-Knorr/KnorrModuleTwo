# Patrick Gerber
# Mod 2 Assignment 
# Groundhog Day

# BUDGET CALCULATOR

# the assignment calls for 2 functions and a decision tree 
# from my prior programming knowledge I know I would like to eventually encapsulate these into a class to manage the logic. This will make the code more reuseable 
# 
#   

# first i like to list out the requirements and create a solution then refactor from there. 

# - get pay periods from user -DONE
# - get amount of pay per period from user -DONE
print('=== Budget Calculator ===')

pay_periods = int(input('How many times are you paid each month: '))
pay_amount = float(input('How much is each paycheck (post-tax): $'))
monthly_income = pay_periods * pay_amount

# create a function called get cost that takes one parameter for the name of a cost
#   - this function should first check if the user pays for the cost 
#       - if the user DOES pay for the cost return that amount 
#       - if the user DOES NOT pay for the cost return 0 

def get_cost(cost_name):
    users_answer = input(f'\nDo you pay for {cost_name} (y/n): ').lower()

    if users_answer == 'y':
        amount = float(input(f'How much is/are {cost_name} per month: $'))
        return amount
    else:
        return 0.0

