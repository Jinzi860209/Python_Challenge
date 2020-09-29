import os
import csv
csvpath = os.path.join('./Resources/election_data.csv')
pathout = os.path.join('./Analysis/election_analysis.txt')

with open(csvpath,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    #Set variables
    Total_votes = 0 
    Khan_votes = 0 
    Correy_votes = 0
    Li_votes = 0
    Otooley_votes = 0


    # Iterate through each row in the csv
    for row in csvreader: 

    # Count total votes
        Total_votes +=1

    # Count the candidates name appears and store in a list 
        if row[2] == "Khan": 
           Khan_votes +=1
        elif row[2] == "Correy":
             Correy_votes +=1
        elif row[2] == "Li": 
            Li_votes +=1
        elif row[2] == "O'Tooley":
            Otooley_votes +=1

  # Make two lists
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [Khan_votes, Correy_votes,Li_votes,Otooley_votes]

# Find the percentage
Khan_percent = (Khan_votes/Total_votes) *100
Correy_percent = (Correy_votes/Total_votes) * 100
Li_percent = (Li_votes/Total_votes)* 100
Otooley_percent = (Otooley_votes/Total_votes) * 100

#Zip candidates and votes together
candidates_and_votes=dict(zip(candidates,votes))
#Use max function find the winner of the dictionary
key=max(candidates_and_votes,key=candidates_and_votes.get)

# Print results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {Total_votes}")
print(f"----------------------------")
print(f"Khan: {Khan_percent:.3f}% ({Khan_votes})")
print(f"Correy: {Correy_percent:.3f}% ({Correy_votes})")
print(f"Li: {Li_percent:.3f}% ({Li_votes})")
print(f"O'Tooley: {Otooley_percent:.3f}% ({Otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

output=(
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {Total_votes}\n"
    f"----------------------------\n"
    f"Khan: {Khan_percent:.3f}% ({Khan_votes})\n"
    f"Correy: {Correy_percent:.3f}% ({Correy_votes})\n"
    f"Li: {Li_percent:.3f}% ({Li_votes})\n"
    f"O'Tooley: {Otooley_percent:.3f}% ({Otooley_votes})\n"
    f"----------------------------\n"
    f"Winner: {key}\n"
    f"----------------------------\n"
)
print(output)

#Write to the text path
with open(pathout, "w") as txt_file:
    txt_file.write(output)