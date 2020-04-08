"""
Created Saturday March 28, 2020

@author: Cris Morales
"""
# Part A: House Hunting

annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the portion of salary to be saved, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))

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
else:
    print('Number of Months: ', months_needed)  # Output
    print('Number of Years in Decimal: ', months_needed/12)   # My Addition


"""
Lessons Learned:
+= only needs what's added
could have used float inputs rather than int inputs
"""