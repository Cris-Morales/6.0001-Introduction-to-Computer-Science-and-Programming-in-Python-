"""
Created Saturday March 28, 2020

@author: Cris Morales
"""
# Part B: Saving, with a raise

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the portion of salary to be saved, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

# Loop variables
months_needed = 0
current_savings = 0
r = 0.04    # Return on investment
portion_down_payment = 0.25 # Down payment percentage
down_payment = portion_down_payment*total_cost  # Down payment up front

while current_savings < down_payment:
    return_inv = current_savings*r/12   # Return on investment
    monthly_saved_sal = portion_saved*annual_salary/12  # Monthly salary saved
    current_savings += return_inv + monthly_saved_sal   # Savings added in the loop
    months_needed += 1  # Month Counter
    if months_needed%6 == 0:
        annual_salary += annual_salary*semi_annual_raise
else:
    print('Number of Months: ', months_needed)  # Output