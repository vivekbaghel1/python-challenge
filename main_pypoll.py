# import os and cvs module
import os
import csv

# define file path 
csv_path = os.path.join('.','election_data.csv')

# open csv file
with open(csv_path, 'r') as csvfile:
    election_read = csv.reader(csvfile, delimiter=',')

    election_header = next(election_read)

    total_votes = 0

    for rows in election_read:
        #print(row)
        total_votes = total_votes + int(rows[0])



    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:", total_votes)
    
