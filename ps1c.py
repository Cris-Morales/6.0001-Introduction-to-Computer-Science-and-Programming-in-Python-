"""
Created Saturday March 28, 2020

@author: Cris Morales

Thank you to @sturrion and @jeremiahflaga, for posting helpful solutions!
"""

# Input
starting_salary = float(input('Enter your annual salary: '))

# Knowns:
total_cost = 1000000
semi_annual_raise = 0.07
r = 0.04    # Return on investment
portion_down_payment = 0.25     # Down payment percentage
down_payment = portion_down_payment*total_cost  # Down payment up front
months = 36

# bisection search:
epsilon = 100
bisection_steps = 0
max_portion_saved = 10000   # Max = 100% as an integer
min_portion_saved = 0       # Min = 0% as integer
best_portion_saved = max_portion_saved  # Initial Guess
found = False

while found is False:
    bisection_steps += 1
    annual_salary = starting_salary
    current_savings = 0
    for i in range(1, months+1):
        return_inv = current_savings*r/12   # Return on investment
        monthly_saved_sal = (best_portion_saved/10000)*annual_salary/12     # Monthly salary saved
        current_savings += return_inv + monthly_saved_sal
        if i % 6 == 0:
            annual_salary += annual_salary*semi_annual_raise
#    print(bisection_steps)     # Error Check
#    print(current_savings)     # Error Check
    if best_portion_saved == 10000 and current_savings < down_payment:
        break
    elif abs(current_savings - down_payment) <= epsilon:
        found = True
        break
    if current_savings < down_payment:
        min_portion_saved = best_portion_saved
    else:
        max_portion_saved = best_portion_saved

    best_portion_saved = (max_portion_saved+min_portion_saved)/2


if found:
    print('Best savings rate:', best_portion_saved / 10000)
    print('Steps in bisection search:', bisection_steps)
else:
    print('Is is not possible to pay the down payment in three years')