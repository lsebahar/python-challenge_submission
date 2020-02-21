#importing relevant modules to open csv
import os
import csv

csvpath = os.path.join("budget_data.csv")

#opening csv to read contents
with open(csvpath) as csvfile:

    #separating data separated by commas
    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader)

    #iterating past header
    csv_header = next(csvreader)

    # print header if desired... not relevant here
    # print(f"CSV Header: {csv_header}")

    #creating lists for both columns & output needed (change in profits)
    months = []
    profits = []
    profit_changes = []

    #iterating through rows in file
    for a,b in csvreader:
        
        # calculating change in profits by comparing monthly profits to that of previous months
        # adding profit change to list
        if len(profits) ==0:
            pass
        else:
            profit_change = int(b) - profits[-1]
            profit_changes.append(profit_change)

        months.append(a)
        profits.append(int(b))

    # creating / converting results into variables for later reference
    total_months = str(len(months))
    total_profits = str(sum(profits))
    avg_change = str(round((sum(profit_changes) / len(profit_changes)),2))
    max_increase = str(max(profit_changes))
    max_increase_month = months[profit_changes.index(max(profit_changes)) + 1 ]
    max_decrease = str(min(profit_changes))
    max_decrease_month = months[profit_changes.index(min(profit_changes)) + 1 ]

    # storing desired output as variable for quicker writing/reference
    message = 'Financial Analysis'
    message += '\n'
    message += "______________________"
    message += '\n'
    message += "Total Months: " + total_months
    message += '\n'
    message += "Total: $" + total_profits
    message += '\n'
    message += "Average Change: " + avg_change
    message += '\n'
    message += "Greatest Increase in Profits: " + max_increase_month + " ($" + max_increase+')'
    message += '\n'
    message += "Greatest Decrease in Profits: " + max_decrease_month+ " ($" + max_decrease+ ')'
    
    # printing message in terminal
    print(message)


# writing message to text file
f = open('budget_fin_analysis.txt', 'w+')

f.write(message)

f.close()
