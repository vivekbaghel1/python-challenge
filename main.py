# import os and cvs module
import os
import csv

# define file path 
csv_path = os.path.join('.','budget_data.csv')

# open csv file
with open(csv_path, 'r') as csvfile:
    budget_read = csv.reader(csvfile, delimiter=',')

    budget_header = next(budget_read)

    #total_month = sum(1 for rows in budget_read)

    #total_net_amount = sum(float(rows[1]) for rows in budget_read)

    total_month = 0
    total_net_amount = 0
    profit_loses = []
    rev_change =[]
    month = []
    #rev_change = 0

    for rows in budget_read:
        #print(row)
        total_month = total_month + 1
        profit_loses.append(float(rows[1]))
        total_net_amount = total_net_amount + int(rows[1])
        month.append(rows[0])
        #print(total_month)

    #print(len(total_month))
    #print(sum(total_net_amount))

    for i in range(1,total_month):
        rev_change.append(profit_loses[i] - profit_loses[i-1])

    ave_change = round(sum(rev_change) / (total_month -1),2)
    max_change = max(rev_change)
    #max_change_month 
    min_change = min(rev_change)

    #print(total_month)
    #print(total_net_amount)
    #print(ave_change)

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", total_month)
    print("Total: $", total_net_amount)
    print("Avereage Change: $", ave_change)
    print("Greatest Increase in Profits:" + "$", max_change)
    print("Greatest Decrease in Profits:" + "$", min_change)
