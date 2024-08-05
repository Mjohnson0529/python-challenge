# dependencies 
import os
import csv

# relative path
poll_csv = os.path.join('Resources', 'election_data.csv' )

# list of votes
canvotes = []

# counter for the amount of votes
totalvote = 0

# list of candidates 
candidates = []

# list for the percentage of votes
pctvote = []

# read csv file
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read header row
    csv_header = next(csvreader)

    # read through every line after the header
    for row in csvreader:
        
        # count the total number of votes 
        totalvote += 1
        # add candidates to list with amount of votes
        if row[2] not in candidates:
            candidates.append(row[2])
            canvotes.append(1)
        else:
            canvotes[candidates.index(row[2])] += 1
    # calculate pctage of votes for each candidate 
    can1 = candidates[0]
    can2 = candidates[1]
    can3 = candidates[2]
    can1_pct = round((canvotes[0]/totalvote) * 100,3)
    can2_pct = round((canvotes[1]/totalvote) * 100,3)
    can3_pct = round((canvotes[2]/totalvote) * 100,3)
    # find the winner 
    winner = max(canvotes)
    wincan = candidates[canvotes.index(winner)]
    
    # print analysis
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {totalvote}')
    print('-------------------------')
    print(f'{can1}: {can1_pct}% ({canvotes[0]})' )
    print(f'{can2}: {can2_pct}% ({canvotes[1]})' )
    print(f'{can3}: {can3_pct}% ({canvotes[2]})' )
    print('-------------------------')
    print(f'Winner: {wincan}')
    print('-------------------------')


#print to text file
output = os.path.join("Analysis", "pypoll.txt")

# write in file

pypoll = open(output, 'w')
pypoll.write('Election Results\n')
pypoll.write('-------------------------\n')
pypoll.write(f'Total Votes: {totalvote}\n')
pypoll.write('-------------------------')
pypoll.write(f'{can1}: {can1_pct}% ({canvotes[0]})\n' )
pypoll.write(f'{can2}: {can2_pct}% ({canvotes[1]})\n' )
pypoll.write(f'{can3}: {can3_pct}% ({canvotes[2]})\n' )
pypoll.write('-------------------------\n')
pypoll.write(f'Winner: {wincan}\n')
pypoll.write('-------------------------\n')