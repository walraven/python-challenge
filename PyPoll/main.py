#pyPoll Homework by Taylor Walraven
import pandas as pd #does the work for us
import os

#set the filename
csv_path = os.path.join('Resources', 'election_data.csv')

#read file into a data frame
election_df = pd.read_csv(csv_path)

#.value_counts() handily counts votes and sorts the counts
results = election_df['Candidate'].value_counts()

#determine the total number of votes cast
num_votes = results.sum() #stored as variable instead of repeatedly calling

#display results

print ("Election Results")
print ("=========================")
print ("Total Votes: {}".format(num_votes))
print ("=========================")
for i in range(len(results)): #nice and elegant
    print("{}: {}% ({})".format(results.index[i],round((results[i]/num_votes*100), 2),results[i]))
print ("=========================")
print ("Winner: {}".format(results.index[0])) #This will be the winner as results is sorted
print ("=========================")

#output to text file

#set filename
file_name = os.path.join("output.txt")

#print to file
with open (file_name, mode = 'w') as text_file:
    text_file.write ("Election Results\n")
    text_file.write ("=========================\n")
    text_file.write ("Total Votes: {}\n".format(num_votes))
    text_file.write ("=========================")
    for i in range(len(results)):
        text_file.write("{}: {}% ({})\n".format(results.index[i],round((results[i]/num_votes*100), 2),results[i]))
    text_file.write ("=========================\n")
    text_file.write ("Winner: {}\n".format(results.index[0]))
    text_file.write ("=========================\n")

    #all done!
    text_file.close()