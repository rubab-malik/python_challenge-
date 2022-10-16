# First we'll import the os module
# This will allow us to create file paths across operating systems

import os

# Module for reading CSV files

import csv

# Path TO collect data from csv folder and save them as a text file

csvpath = os.path.join('..','Resources', 'budget_data.csv')
txtfile_csvpath=os.path.join('..', 'Resources', 'budget_data.txt')

# initializing the 'variables'

months_count=0
total_net_amount=0
PreValue=0
Diffrence=0
greatest_increase=0
greatest_decrease=0

# Define list
change=[]

# reading using csv module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        months=row[0]
        amount=row[1]
        row_amount=int(amount)
        Diffrence=row_amount-PreValue
        PreValue=row_amount

        change.append(Diffrence)

    # Greatest increase in profits
        if (greatest_increase < Diffrence):
            greatest_increase= Diffrence
            greatest_increase_date=months

    # Greatest decrease in profits
        if (greatest_decrease > Diffrence):
            greatest_decrease= Diffrence
            greatest_decrease_date=months
           
    # Get total amount of Financial Analysis

        months_count+=1
        total_net_amount+=int(amount)

    # Get average

average=round((sum(change[1:])/(len(change)-1)),2)

with open(txtfile_csvpath, "w") as txt_file: 

# Display Results

# Total number of months included in dataset

    total_months=(
        f"\nFinancial Analysis\n"
        f"---------------------------\n"
        f"Total Months: {months_count}")
    print(total_months)
    txt_file.write(total_months)

# The net total amount of "Profit/Losses" over the entire period

    total_amount=(f"\nTotal: ${total_net_amount}\n")
    print(total_amount)
    txt_file.write(total_amount)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

    Av=(f"Average: ${average}\n")
    print(Av)
    txt_file.write(Av)

# The greatest increase in profits (date and amount) over the entire period

    max=(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    print(max)
    txt_file.write(max)

# The greatest decrease in profits (date and amount) over the entire period

    min=(f"Greatest decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    print(min)
    txt_file.write(min)






    









