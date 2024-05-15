import os

# allow read of csv file
import csv

# initialize variables / candidatevotes / totalvotes  
votespercandidate = {}
totalvotes = []
# initialize variables for each candidate
Charles_Casper = 0
Raymon_Anthony = 0
Diana_Degette = 0

csvpath = os.path.join("Resources", "election_data.csv")

# open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read and store header, start at next line
    csvheader = next(csvreader)

    # read through rows after header
    for row in csvreader:

        #append total votes to new list
        totalvotes.append(row[1])

        # assigning votes to the length of total votes
        votes = len(totalvotes)
        
            # if row 3 contains charles, add +1 to charles variable
        if row[2] == "Charles Casper Stockham":
            Charles_Casper += 1

            # elseif row 3 contains diana, add +1 to diana variable
        elif row[2] == "Diana DeGette":
            Diana_Degette += 1

            # elseif row 3 contains raymon, add +1 to raymon variable
        elif row[2] == "Raymon Anthony Doane":
            Raymon_Anthony += 1
        
    # Calculate totals for each candidate
    Cand1 = round((Charles_Casper / votes)*100,3)
    Cand2 = round((Diana_Degette / votes)*100,3)
    Cand3 = round((Raymon_Anthony / votes)*100,3)
    
    # hold number of votes per candidate in a dictionary
    votespercandidate = {"Charles Casper Stockham": Charles_Casper,
                      "Diana DeGette": Diana_Degette,
                      "Raymon Anthony Doane": Raymon_Anthony}
    
    # calculate electioner winner by max votes
    electionresult = max(votespercandidate, key = votespercandidate.get)
    
# write to a new file in the analysis folder, with the "w" write mode
with open("Analysis/election_reults.txt", "w") as file:

    # write each line in output file, and print in terminal
    file.write("Election Results\n") #election_results.txt
    print("Elesction Results") #terminal
    file.write("----------------------------\n") #election_results.txt
    print("----------------------------") #terminal
    file.write(f"Total Votes: {votes}\n") #election_results.txt
    print(f"Total Votes: {votes}") #terminal
    file.write("----------------------------\n") #election_results.txt
    print("----------------------------") #terminal
    file.write(f"Charles Casper Stockgam: {Cand1}% ({Charles_Casper})\n") #election_results.txt
    print(f"Charles Casper Stockgam: {Cand1}% ({Charles_Casper})") #terminal
    file.write(f"Diana DeGette: {Cand2}% ({Diana_Degette})\n") #election_results.txt
    print(f"Diana DeGette: {Cand2}% ({Diana_Degette})") #terminal
    file.write(f"Raymon Anthony Doane: {Cand3}% ({Raymon_Anthony})\n") #election_results.txt
    print(f"Raymon Anthony Doane: {Cand3}% ({Raymon_Anthony})") #terminal
    file.write("----------------------------\n") #election_results.txt
    print("----------------------------") #terminal
    file.write(f"Winner: {electionresult}\n") #election_results.txt
    print(f"Winner: {electionresult}")#terminal
    file.write("----------------------------\n") #election_results.txt
    print("----------------------------") #terminal

            