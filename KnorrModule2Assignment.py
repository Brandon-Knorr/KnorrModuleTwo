# Patrick Gerber
# Mod 2 Assignment 
# Groundhog Day

# BUDGET CALCULATOR
class BudgetManager:
    def __init__(self):
        print('=== Budget Calculator ===')
        self.pay_periods = int(input('How many times are you paid each month: '))
        self.pay_amount = float(input('How much is each paycheck (post-tax): $'))
        self.monthly_income = self.pay_periods * self.pay_amount

    def get_cost(self, cost_name):
        users_answer = input(f'\nDo you pay for {cost_name} (y/n): ').lower()

        if users_answer == 'y':
            amount = float(input(f'How much is/are {cost_name} per month: $'))
            return amount
        else:
            return 0.0

    def print_report(self, monthly_income, monthly_costs):
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



if __name__ == '__main__':

    manager = BudgetManager()

    categories = ['rent', 'groceries', 'a car']
    total_monthly_costs = 0

    for item in categories:
        total_monthly_costs += manager.get_cost(item)

    manager.print_report(manager.monthly_income, total_monthly_costs)

