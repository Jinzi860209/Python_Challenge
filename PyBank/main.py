import os
import csv
csvpath = os.path.join('./Resources/budget_data.csv')
pathout = os.path.join('./Analysis/budget_analysis.txt')


with open(csvpath,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)

    #Create lists for variables
    total_months = []
    profit = []
    profit_change = []
    
   # Read each row of data after the header
    for row in csvreader:
         #total months
        total_months.append(row[0])
        
        #total profit
        profit.append(int(row[1]))
   
    for i in range(len(profit)-1):
        
        # Take the difference between two months
        profit_change.append(profit[i+1]-profit[i])
                      
#evaluate the max and min
increase = max(profit_change)
decrease = min(profit_change)

#using the index
month_increase = profit_change.index(max(profit_change))+1
month_decrease = profit_change.index(min(profit_change))+1

#print the result
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(total_months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {total_months[month_decrease]} (${(str(decrease))})")  
   
output=(
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {len(total_months)}\n"
    f"Total: ${sum(profit)}\n"
    f"Average Change: {round(sum(profit_change)/len(profit_change),2)}\n"
    f"Greatest Increase in Profits: {total_months[month_increase]} (${(str(increase))})\n"
    f"Greatest Decrease in Profits: {total_months[month_decrease]} (${(str(decrease))})\n"
)
print(output)

#Write to the text path
with open(pathout, "w") as txt_file:
    txt_file.write(output)
            