#!/usr/bin/env python
# coding: utf-8

# import dependencies
import pandas as pd

# read in the file
original_file = "Resources/budget_data.csv"

file = pd.read_csv(original_file, encoding="UTF-8")
#file.head()

# totaling of all profit and losses of all periods
total = file["Profit/Losses"].sum()
#total

# totaling number of periods
total_months = file["Date"].count()
#total_months

# set new variable to make coding easier
profit_losses = file["Profit/Losses"]

# set new variable to make coding easier
profit_losses = file["Profit/Losses"]

# created list to store montly changes
monthly_change = []

# created for loop to actually calculate monthly changes
for i in range(0,len(profit_losses)-1):
    
    value_1 = profit_losses[i]
# incrementing i to get the next value
# note: we do not increment in for loop because of this
    i = i + 1
    value_2 = profit_losses[i]
    change = value_2 - value_1
    
# append the value to monthly change
    monthly_change.append(change)
        
# for loop to sum all monthly changes
aggregate_monthly_changes = 0
for value in monthly_change:
    aggregate_monthly_changes = aggregate_monthly_changes + value

# averaged all monthly changes
average_change = round(aggregate_monthly_changes / (total_months - 1),2)
#average_change

# found max monthly change then found corresponding index to find date in "Date" field
greatest_increase_profit = max(monthly_change)
max_month_index = monthly_change.index(greatest_increase_profit)
#greatest_increase_profit
#max_month_index

# found the corresponding date from "max_month_index" above adding plus 1 because the index is off 1 in monthly_change list
greatest_increase_date = file["Date"][(max_month_index + 1)]
#greatest_increase_date

# found greatest decrease in monthly change then found corresponding index to find date in "Date" field
greatest_decrease_profit = min(monthly_change)
greatest_decrease_index = monthly_change.index(greatest_decrease_profit)
# greatest_decrease_profit
# greatest_decrease_index

# found the corresponding date from "greatest_decrease_index" above adding plus 1 becase the index is off 1 in monthly_change list
greatest_decrease_date = file["Date"][(greatest_decrease_index + 1)]
# greatest_decrease_date

# printing table results
results_PyBank = "Financial Analysis" + '\n' + "--------------------------------" + '\n' + "Total Months: " + str(total_months) + '\n' + "Total: $" + str(total) + '\n' + "Average Change: $" + str(average_change) + '\n' + "Greatest Increase in Profits: " + greatest_increase_date + " " + "($" + str(greatest_increase_profit) + ")" + '\n' + "Greatest Decrease in Profits: " + greatest_decrease_date + " " + "($" + str(greatest_decrease_profit) + ")"
results_PyBank

# write data in a file. 
file1 = open("results_PyBank.txt","w")
file1.write(results_PyBank)
file1.close()
