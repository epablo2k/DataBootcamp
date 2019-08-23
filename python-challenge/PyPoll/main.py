import random


votes = {} # name, numberofvotes
num = 1



f=open("election_data.csv", "r")

f1 = f.readlines()
	

	
for x in f1:


	if num > 1:
		voterid,county,candidate = x.split(",")
		candidate = candidate.replace("\n","")
		
		
		exists = candidate in votes.keys()
		
		if exists == True:
			votes[candidate] = int(votes[candidate]) + 1 # Add 1 vote
		else:
			votes[candidate] = 1  
	else:
		print("Reading file, please wait...", flush=True)
					
	num = num + 1
	
total_votes = 0
winner_name = ""
winner_votes = 0


for candidate in votes:
	total_votes = total_votes + votes[candidate]
	if (winner_votes==0 or winner_votes < votes[candidate]):
		winner_votes = votes[candidate]
		winner_name = str(candidate)

fo=open("py_poll_report.txt","w+")

print("Total votes: %s" % (total_votes))
fo.write("Total votes: %s\n" % (total_votes))

for candidate in votes:
	print("candidate %s got %s votes %s%%" % (str(candidate),votes[candidate],round((100/total_votes)*votes[candidate],2)))
	fo.write("candidate %s got %s votes %s%%\n" % (str(candidate),votes[candidate],round((100/total_votes)*votes[candidate],2)))


print("the winner is: %s" %(winner_name))
fo.write("the winner is: %s" %(winner_name))

print("Please check file py_poll_report.txt for more details")

f.close() 
fo.close() 



