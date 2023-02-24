import os
import csv
file_path = os.path.join("Resources", "budget_data.csv")
#import the csv

beginning_months = 0
begin_profit_and_loss = 0
profit_and_loss_start = 0
total_profit_and_loss = []
total_profit_and_loss_change = []
date_list = []
#sets up variables and lists

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    #opens csv

    for row in csvreader:
        total_months = beginning_months + 1
        beginning_months = total_months
        #calculates total months in data set

        profit_and_loss = begin_profit_and_loss +  int(row[1]) 
        begin_profit_and_loss = profit_and_loss 
        #calculates total profit and loss over time

        profit_and_loss_change = (int(row[1]) - profit_and_loss_start)
        profit_and_loss_start = int(row[1])
        total_profit_and_loss_change.append(int(profit_and_loss_change))
        #calculates profit / loss per row, and appends that change to the list above
        date_list.append(row[0])
        #append the date in column 0 to the list for each loop

total_profit_and_loss_change.pop(0)
average_change=round((sum(total_profit_and_loss_change)/len(total_profit_and_loss_change)),2)

largest_increase = max(total_profit_and_loss_change)
#largest increase
largest_increase_index = total_profit_and_loss_change.index(largest_increase)
#index of largest increase
largest_increase_month = (date_list[largest_increase_index + 1])
#find the associated month using the index

largest_decrease = min(total_profit_and_loss_change)
#largest decrease
largest_decrease_index = total_profit_and_loss_change.index(largest_decrease)
#index of largest decrease
largest_decrease_month = (date_list[largest_decrease_index + 1])
#find the associated month using the index


output =(
f'Financial Analysis\n'
f'-------------------------\n'
f'Total Months: {total_months}\n'
f'Total: ${profit_and_loss}\n'
f'Average Change: ${average_change}\n'
f'Greatest Increase in Profits: {largest_increase_month} (${largest_increase})\n'
f'Greatest Decrease in Profits: {largest_decrease_month} (${largest_decrease})\n'
)
#aggregate data for output

output_file = os.path.join("Analysis","PyBank_final.txt")
with open (output_file, "w") as txtfile:
   txtfile.write(output)
    #write to a file




