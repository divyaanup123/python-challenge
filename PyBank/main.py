import os
import csv

#csvpath='C:/personal/Divya Ut assignement/Starter_Code/PyBank/Resources/budget_data.csv'
#csvpath =os.path.join(path,'budget_data.csv')
csvpath=os.path.join("..", "Resources", "budget_data.csv")

# Create empty lists to iterate through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []
 
# Open csv in default read mode 
with open(csvpath, encoding="utf-8") as budget_data:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget_data,delimiter=",") 

    # Skip the header labels to iterate with the values
    header = next(csvreader)  

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)


max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {len(total_months)}\n")
print(f"Total: ${sum(total_profit)}\n")
print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")

# Printting  the Final analysis and exporting to a text file 
# Set path for file
csvpath = os.path.join('..', 'Resources', 'PyBank_Results.txt')
with open(csvpath, "w") as text_file:
    print('Financial Analysis', file=text_file)
    print('----------------------------', file=text_file)
    print(f'Total Months: {len(total_months)}', file=text_file)
    print(f'Total: ${sum(total_profit)}', file=text_file)
    print(f'Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}', file=text_file)
    print(f'Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})', file=text_file)
    print(f'Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})', file=text_file)

