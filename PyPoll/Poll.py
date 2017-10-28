#  The total number of votes cast

#  A complete list of candidates who received votes

#  The percentage of votes each candidate won

#  The total number of votes each candidate won

#  The winner of the election based on popular vote.



#import files
import csv

import os

from collections import Counter


#create candidates count
candidate = Counter()

votes = 0

# open filepaths
filepath = os.path.join("raw_data","election_data_2.csv")

#Read files 
with open(filepath,'r') as file:

    csvreader = csv.reader(file,delimiter=",")

    header = next(csvreader)



    for row in csvreader:

        votes = votes + 1

        candidate[row[2]] += 1


print("""Election Results

-------------------------""")

print(f"Total Votes: {votes}")

print("""---------------------""")


#create a dictionary to determine percentage votes
candidate = dict(candidate)

for key,value in candidate.items():

    percentage = '{0:.1%}'.format(float(value)/float(votes))

    print(f"{key}: {percentage} ({value})")



print("""-------------------------""")

#define the dictionary key
def key_with_max_value(dict):

    votes = list(dict.values())

    candidate = list(dict.keys())

    max_candidate = candidate[votes.index(max(votes))]

    max_votes = max(votes)

    print(f"Winner: {max_candidate}") 

key_with_max_value(candidate)

print("""-------------------------""")