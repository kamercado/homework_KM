#Python - open and read csv file
import csv
file_location = '../Instructions/PyPoll/Resources/election_data.csv'
#count votes as looping
total_votes = 0
#keep list of all candidate entries as looping
candidate_list = []
#list to keep tally of each candidate's votes (like a new column)
tally = []
#list to store percentages later on
percentage_list = []


#read csvfile
with open (file_location, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)
	print(f"CSV Header: {csv_header}")
#loop through rows - grab candidates
	for rows in csvreader:
		#counting how many total votes
		total_votes += 1
		#define variable candidate for reference
		candidate = rows[2]
		#while looping through rows, want to check if candidate name is already in list
		#if already in list, add count - if not, make new value in candidatelist
		if candidate in candidate_list:
			#index for tally should be the same as index of candidate on list for alignment
			tally[candidate_list.index(candidate)] +=1
		else:
			#create a new value and count it as 1 vote for new value
			candidate_list.append(candidate)
			tally.append(int(1))
#check work
print(candidate_list)
print(tally)


#percentages - loop through all in tally then divide by total votes
for i in tally:
	percentage_votes = ((i/((int(total_votes)))*100))
	percentage_list.append(percentage_votes)
#check work
print(percentage_list)

#winner - find max of tally list
winner = max(tally)
print(winner)
#grab index of tally list to grab same index for candidate list to find winner
tally_index = tally.index(winner)
candidate_winner = candidate_list[tally_index]
print(candidate_winner)

print("")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
#loop through percentage, candidate, and tally lists to populate
for i in range(len(candidate_list)):
	print(f"{candidate_list[i]}: {percentage_list[i]}% ({tally[i]})")
print("-------------------------")
print(f"Winner: {candidate_winner}")
print("-------------------------")

#export .txt file

txtfile = open("PyPoll_Results.txt",'w')
txtfile.write("Election Results\n")
txtfile.write("-------------------------\n")
txtfile.write(f"Total Votes: {total_votes}\n")
txtfile.write("-------------------------\n")
#loop through percentage, candidate, and tally lists to populate
for i in range(len(candidate_list)):
	txtfile.write(f"{candidate_list[i]}: {percentage_list[i]}% ({tally[i]})\n")
txtfile.write("-------------------------\n")
txtfile.write(f"Winner: {candidate_winner}\n")
txtfile.write("-------------------------\n")
txtfile.close()
print("")
print("Complete. .txt file created.")