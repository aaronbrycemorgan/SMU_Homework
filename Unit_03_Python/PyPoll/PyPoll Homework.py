#!/usr/bin/env python
# coding: utf-8

# import dependencies
import pandas as pd

# read in the file
original_file = "Resources/election_data.csv"

file = pd.read_csv(original_file, encoding="UTF-8")
# file.head()

# looking over the file
# file.info()

# calculating total votes
total_votes = len(file["Voter ID"])
# total_votes

# looking over the candidates and their attributed votes
candidate_counts = file["Candidate"].value_counts()
# candidate_counts

# calculating khan's votes
khan_count = candidate_counts["Khan"]
# khan_count

# calculating correy's votes
correy_count = candidate_counts["Correy"]
# correy_count

# calculating li's votes
li_count = candidate_counts["Li"]
# li_count

# calculating o'tooley's votes
otooley_count = candidate_counts["O'Tooley"]
# otooley_count

# calculating khan's vote percentage
khan_percentage = round(((khan_count / total_votes) * 100),3)
# khan_percentage

# calculating correy's vote percentage
correy_percentage = round(((correy_count / total_votes) * 100),3)
# correy_percentage

# calculating li's vote percentage
li_percentage = round(((li_count / total_votes) * 100),3)
# li_percentage

# calculating o'tooley's vote percentage
otooley_percentage = round(((otooley_count / total_votes) * 100),3)
# otooley_percentage

# created a dictionary to loop through to find winner
candidate_dicts = [{"Count": correy_count, "Name": "Correy"},
                   {"Count": li_count, "Name": "Li"},
                   {"Count": otooley_count, "Name": "O'Tooley"},
                   {"Count": khan_count, "Name": "Khan"}]

# looping through the dictionary to find the winner by name
vote_winner = ''
highest_vote = 0
for can in candidate_dicts:
    if can["Count"] > highest_vote:
        highest_vote = can["Count"]
        vote_winner = can["Name"]

# vote_winner

# printing the results of the analysis
results_PyPoll = "Election Results" + '\n' + "------------------------" + '\n' + "Total Votes: " + str(total_votes) + '\n' + "------------------------" + '\n' + "Khan: " + str(khan_percentage) + "% " + "(" + str(khan_count) + ")" + '\n' + "Correy: " + str(correy_percentage) + "% " + "(" + str(correy_count) + ")" + '\n' + "Li: " + str(li_percentage) + "% " + "(" + str(li_count) + ")" + '\n' + "O'Tooley: " + str(otooley_percentage) + "% " + "(" + str(otooley_count) + ")" + '\n' + "------------------------" + '\n' + "Winner: " + vote_winner + '\n' + "------------------------"
results_PyPoll

# write data in a file. 
file1 = open("results_PyPoll.txt","w")
file1.write(results_PyPoll)
file1.close()
