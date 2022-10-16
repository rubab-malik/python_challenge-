
# First we'll import the os module
# This will allow us to create file paths across operating systems

import os

# Module for reading CSV files

import csv

# Path TO collect data from csv folder and save them as a text file

csv_path=os.path.join('../Resources','election_data.csv')
txtfile_csvpath=os.path.join('..', 'Resources', 'election_data.txt')

#Initialize Total_vote counter

total_votes=0

# options of candidate (Declare a dictionary)

candidate={}
candidate_List = {}

# reading using csv module

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    header=next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # count total number of vote cast
        total_votes+=1

        #Print the candidate name of each row

        candidate_name = row[2]

         #Print the candidate vote of each row
        
        candidate_votes={}   

        # If the candidate name doesn't match any existing candidate in a list
        #for candidate_name in candidate_List:

        if candidate_name not in candidate_List:
            
            candidate_List[candidate_name]=1

        else:

            candidate_List[candidate_name]+=1

with open(txtfile_csvpath, "w") as txt_file: 

# The total number of votes cast

    results=(
        f"\nELection Results\n"
        f"-------------------\n"
        f"Total Votes: {total_votes}\n-------------------\n")
    print(results)
    txt_file.write(results)
    
    # The count of percentage and total votes won by each candidate 

    for Candidate, vote in candidate_List.items():
        b=(f"{Candidate}: {round(vote/total_votes*100,3)}% ({vote})\n")

        print(b)
        txt_file.write(b)

    # The winner of the election based on popular vote

    c=(f"-------------------\nWinner: {max(candidate_List, key=candidate_List.get)}\n-------------------")
    print(c)
    txt_file.write(c)