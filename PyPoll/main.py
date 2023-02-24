import os
import csv

vote_begin = 0
charles_begin_count = 0
diana_begin_count = 0
raymon_begin_count = 0
#establishes beginning counts for loop

file_path = os.path.join("Resources", "election_data.csv")
with open(file_path) as csvfile:
    csvreader=csv.reader(csvfile, delimiter= ",")
    csvheader = next(csvreader)
    #goes through every row in CSV

    for row in csvreader:
        total_votes = vote_begin + 1
        vote_begin = total_votes
        #calculates total votes

        if row[2] == "Charles Casper Stockham":
            charles_count = charles_begin_count + 1
            charles_begin_count = charles_count
        elif row[2] == "Raymon Anthony Doane":
            raymon_count = raymon_begin_count + 1
            raymon_begin_count = raymon_count
        else: 
            diana_count = diana_begin_count + 1
            diana_begin_count = diana_count
         #if statement counts votes if name is in index 2

charles_percent = "{:.3%}".format(charles_count / total_votes)
diana_percent = "{:.3%}".format(diana_count / total_votes)
raymon_percent = "{:.3%}".format(raymon_count / total_votes)
candidates = ["Charles Casper Stockham", "Diana DeGette","Raymon Anthony Doane"]
percent = [charles_percent, diana_percent, raymon_percent]
winnerpercent = max(percent)
winnerindex = percent.index(winnerpercent)
winnername = candidates[winnerindex]
#calculations for output

output =(
f'Election Results\n'
f'-------------------------\n'
f'Total Votes: {total_votes}\n'
f'-------------------------\n'
f'Charles Casper Stockham: {charles_percent} ({charles_count})\n'
f'Diana DeGette: {diana_percent} ({diana_count})\n'
f'Raymon Anthony Doane: {raymon_percent} ({raymon_count})\n'
f'-------------------------\n'
f'Winner: {winnername}\n'
f'-------------------------\n'
)
#aggregate data for output

output_file = os.path.join("Analysis","PyBank_final.txt")
with open (output_file, "w") as txtfile:
   txtfile.write(output)
#write to a file

