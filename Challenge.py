import os
# Resources\budget_data.cs/v
import csv
file_path = os.path.join("..", "Resources", "budget_data.csv")
beginning_months = 0
begin_profit_and_loss = 0
profit_and_loss_start = 0
total_profit_and_loss = []
total_profit_and_loss_change = []
date_list = []

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_months = beginning_months + 1
        beginning_months = total_months
        # Calculates total months in data set

        profit_and_loss = begin_profit_and_loss +  int(row[1]) 
        begin_profit_and_loss = profit_and_loss 
        # Calculates total profit and loss over time

        profit_and_loss_change = (int(row[1]) - profit_and_loss_start)
        profit_and_loss_start = int(row[1])
        total_profit_and_loss_change.append(int(profit_and_loss_change))
        # Calculates profit / loss per row, and appends that change to the list above
        date_list.append(row[0])
        #append the date in column 0 to the list for each loop

total_profit_and_loss_change.pop(0)
# print(total_profit_and_loss)
average_change=round((sum(total_profit_and_loss_change)/len(total_profit_and_loss_change)),2)

largest_increase = max(total_profit_and_loss_change)
#largest increase
largest_increase_index = total_profit_and_loss_change.index(largest_increase)
# #Index of largest increase
largest_increase_month = (date_list[largest_increase_index + 1])
# #Find the associated month using the index

largest_decrease = min(total_profit_and_loss_change)
#largest decrease
largest_decrease_index = total_profit_and_loss_change.index(largest_decrease)
#Index of largest decrease
largest_decrease_month = (date_list[largest_decrease_index + 1])
# Find the associated month using the index

# print("Financial Analysis")
# print("-----------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: ${profit_and_loss}")
# print(f"Average Change: ${round(average_change,2)}")
# print(f"Greatest Increase in Profits: {largest_increase_month} ${largest_increase}")
# print(f"Greatest Decrease in Profits: {largest_decrease_month} ${largest_derease}")

output =(
f'Financial Analysis\n'
f'-------------------------\n'
f'Total Months: {total_months}\n'
f'Total: ${profit_and_loss}\n'
f'Average Change: ${average_change}\n'
f'Greatest Increase in Profits: {largest_increase_month} ${largest_increase}\n'
f'Greatest Decrease in Profits: {largest_decrease_month} ${largest_decrease}\n'
)
#aggregate data for output

output_file = os.path.join("PyBank_final.txt")
with open (output_file, "w") as txtfile:
   txtfile.write(output)
#write to a file




