# Brandon Knorr
# Mod 2 Lab 2 
# 1 / 28 

def calculate_change_from_input():

    amount = float(input('Enter an amount: $'))


    # 2.98

    amount = int(amount * 100)

    dollars = amount // 100
    amount = amount % 100 

    quarters = amount // 25
    amount = amount % 25 

    dimes = amount // 10
    amount = amount % 10 

    nickles = amount // 5
    amount = amount % 5 

    pennies = amount // 1
    amount = amount % 1

    if dollars > 0:
        print(f'Dollars: {dollars}')

    if quarters > 0:
        print(f'Quarters: {quarters}')

    if dimes > 0:
        print(f'Dimes: {dimes}')

    if nickles > 0:
        print(f'Nickles: {nickles}')

    if pennies > 0:
        print(f'Pennies: {pennies}')

calculate_change_from_input()













