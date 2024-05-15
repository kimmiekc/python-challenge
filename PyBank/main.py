import os

#allow read of .csv file
import csv

# initializing variables / creating change/profitloss/month lists
totalmonths = 0
total = 0
change = []
profits_losses = []
months = []

csvpath = os.path.join("Resources", "budget_data.csv")

# open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read and store header, but start at next line
    csvheader = next(csvreader)

    # read through rows after header
    for row in csvreader:

        # increase the month counter by one each time
        totalmonths += 1
        
        # add profits and losses from current row to total
        total+=int(row[1])
        
        # append the month to the new months list
        months.append(row[0])

        # append profits and losses to new profits_losses list
        profits_losses.append(int(row[1]))
        
        # calculate and append the changes in profits_losses to the change list
        change.append(profits_losses[totalmonths -1] - profits_losses[totalmonths -2])
        
    # sum of all changes in profits_losses
    totalchange = sum(change)

    # calculate average change in profits_losses + round to 2nd decimal place: .00
    averagechange = round(totalchange / (len(change) -1), 2)
    
    # find greatest increase, get the index corresponding to month
    increaseprofit = max(change)
    greatestincrease = change.index(increaseprofit)

    # find greatest decrease, get the index of corresponding to month
    decreaseprofit = min(change)
    greatestdecrease = change.index(decreaseprofit)


# write to a new file in the analysis folder, with the "w" write mode
with open("Analysis/budget_analysis.txt", "w") as file:

    #write each line on the output file, along with printing into the terminal. 
    file.write("Financial Analysis\n") #budget_analysis.txt
    print("Financial Analysis") #terminal
    file.write("----------------------------\n") #budget_analysis.txt
    print("----------------------------") #terminal
    file.write(f"Total Months: {totalmonths}\n") #budget_analysis.txt
    print(f"Total Months: {totalmonths}") #terminal
    file.write(f"Total: ${total}\n") #budget_analysis.txt
    print(f"Total: ${total}") #terminal
    file.write(f"Average Change: ${averagechange}\n") #budget_analysis.txt
    print(f"Average Change: ${averagechange}") #terminal
    file.write(f"Greatest Increase in Profits: {months[greatestincrease]} (${increaseprofit})\n") #budget_analysis.txt
    print(f"Greatest Increase in Profits: {months[greatestincrease]} (${increaseprofit})") #terminal
    file.write(f"Greatest Decrease in Profits: {months[greatestdecrease]} (${decreaseprofit})") #budget_analysis.txt
    print(f"Greatest Decrease in Profits: {months[greatestdecrease]} (${decreaseprofit})") #terminal
