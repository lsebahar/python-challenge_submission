# py-poll code

#importing modules
import csv
import os

#opening csv
csvpath = os.path.join("election_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader)

    #storing header
    csv_header = next(csvreader)

    #creating lists for new candidates & all votes
    candidates = []
    votes = []
    total_votes = 0

    #counting total votes and adding new candidates to candidates list
    for a,b,c in csvreader:
        total_votes += 1
        if c not in candidates:
            candidates.append(c)
        votes.append(c)
    
    #determining number of candidates for percent calcs
    #creating dictionary for each candidate & their vote total, percent
    #creating variable to store winner
    cand_num = len(candidates)
    vote_count = {}
    vote_perc = {}
    winner = ''
    
    for cand in candidates:
        vote_count[cand] = votes.count(cand)
        vote_perc[cand] = float(votes.count(cand) / total_votes)
        if winner not in candidates or vote_count[cand] > vote_count[winner]:
            winner = cand
        

#creating variable for display for concision

message = "Election Results"
message += '\n'
message += "--------------------------"
message += '\n'
message += f'Total Votes: {total_votes}'
message += '\n'
message += "--------------------------"
message += '\n'
for candidate in candidates:
    message += f'{candidate}: {(vote_perc[candidate]):.3%} ({vote_count[candidate]})'
    message += '\n'
message += "--------------------------"
message += '\n'
message += f'Winner: {winner}'
message += '\n'
message += "--------------------------"

#print message for terminal output
print(message)

#writing to text file for result
f = open('election_data_analysis.txt', 'w+')

f.write(message)

f.close()