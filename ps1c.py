"""
Created Saturday March 28, 2020

@author: Cris Morales

Thank you to @sturrion and @jeremiahflaga, for posting helpful solutions!
"""

# Input
starting_salary = float(input('Enter your annual salary: '))

# Knowns:
total_cost = 1000000    #Dream house cost
semi_annual_raise = 0.07    #Semi Annual Raise Rate
r = 0.04    # Return on investment
portion_down_payment = 0.25     # Down payment percentage
down_payment = portion_down_payment*total_cost  # Down payment up front
months = 36     # Desired Months tile down payments

# bisection search:
epsilon = 100   # margin of error, within 100$
bisection_steps = 0     #running bisection step counter
max_portion_saved = 10000   # Max = 100% as an integer
min_portion_saved = 0       # Min = 0% as integer
best_portion_saved = max_portion_saved  # Initial Guess is max for failure criteria
found = False   # starting conditional for the loop

while found is False:
    bisection_steps += 1    # Step Counter
    annual_salary = starting_salary     # Reset Annual Salary each step
    current_savings = 0.0   # Reset savings account each step
    for i in range(1, months+1):    
        return_inv = current_savings*r/12   # Return on investment
        monthly_saved_sal = (best_portion_saved/10000)*annual_salary/12     # Monthly salary saved
        current_savings += return_inv + monthly_saved_sal   # Current Savings Formula
        if i % 6 == 0:     # Semi Annual Raise conditional
            annual_salary += annual_salary*semi_annual_raise
#    print(bisection_steps)     # Error Check
#    print(current_savings)     # Error Check
    if best_portion_saved == 10000 and current_savings < down_payment:  # Failure Conditional
        break
    elif abs(current_savings - down_payment) <= epsilon:    # Success Conditional from margin of error -> epsilon
        found = True
        break
    if current_savings < down_payment:          # Beggining of Bisection redefines
        min_portion_saved = best_portion_saved
    else:
        max_portion_saved = best_portion_saved

    best_portion_saved = (max_portion_saved+min_portion_saved)/2    # Our next guess.


if found:   # Output if found = True
    print('Best savings rate:', best_portion_saved / 10000)
    print('Steps in bisection search:', bisection_steps)
else:       # Output if found = False
    print('Is is not possible to pay the down payment in three years')
