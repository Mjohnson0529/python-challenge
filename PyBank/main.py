# Dependencies 
import os
import csv

# Relative path to csv file
budget_csv = os.path.join('Resources', 'budget_data.csv')

# counter for months
total_months = 0

# counter for net total of p and l
net_total = 0

# variable to hold the value of change between rows
chg = 0

# variable to hold the profit or loss value in the row
total = 0

# list to hold dates
dates = []

# list to hold profits
profits = []

# read csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # read header row
    csv_header = next(csvreader)
    
    # move to first row
    start_row = next(csvreader)
    print(start_row)
    # count the first month
    total_months += 1

    # get value of p or l for first month
    net_total += int(start_row[1])

    # get value of p or l for first month to determine change
    total = int(start_row[1])

    # read each row of data after the header
    for row in csvreader:
        # count the total amount of months
        total_months += 1
        
        # determine the net total amount of p/l of the entire period
        net_total = net_total + int(row[1])
        
        # add dates to date list
        dates.append(row[0])
        
        # record changes in profit 
        chg = int(row[1]) - total
       
        # add the change in profits to the profits list
        profits.append(chg)
        
        # update next profit value
        total = int(row[1])

        # determine the average change over the period
        avg = round((sum(profits)/len(profits)), 2)
# Return the greatest increase in profits
grt_inc = max(profits)

# Return the greatest decrease in profits
grt_dec = min(profits)

# print to terminal
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {total_months}')
print(f'Average Change: ${avg}')
print(f'Greatest Increase in Profits: {dates[profits.index(grt_inc)]} (${grt_inc})')
print(f'Greatest Increase in Profits: {dates[profits.index(grt_dec)]} (${grt_dec })')

# print to text file
output = os.path.join("Analysis", "pybank.txt")

# write in file


pybank = open(output, 'w')
pybank.write(('Financial Analysis\n'))
pybank.write(('----------------------------\n'))
pybank.write(f'Total Months: {total_months}\n')
pybank.write(f'Average Change: ${avg}\n')
pybank.write(f'Greatest Increase in Profits: {dates[profits.index(grt_inc)]} (${grt_inc})\n'),
pybank.write(f'Greatest Increase in Profits: {dates[profits.index(grt_dec)]} (${grt_dec })\n')
   