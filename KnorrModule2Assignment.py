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

# Create a function called print_report
#   -This function should accept two parameters: monthly_income and monthly_costs
#   -This function should output the monthly income and costs
#   -This function should look if the budget is a surplus, breaks even, or is a deficit, and output a corresponding message
#   -No return value is needed

def print_report(monthly_income, monthly_costs):
    print('-' * 30)
    print(f'Monthly Income: ${monthly_income:,.2f}')
    print(f'Monthly Costs: ${monthly_costs:,.2f}')
    print('-' * 30)

    difference = monthly_income - monthly_costs

    if difference > 0:
        print(f'You have a surplus of: ${difference:,.2f}')
    elif difference < 0:
        print(f'You are running a deficit of: ${abs(difference):,.2f}')
    else:
        print('You are breaking even!')


# create a variable to track the total cost
total_costs = 0

# call the get cost function 3 different times with 3 different arguments 
total_costs += get_cost('rent')
total_costs += get_cost('groceries')
total_costs += get_cost('a car')

# call the print report function with the 2 arguments 
print_report(monthly_income, total_costs)

