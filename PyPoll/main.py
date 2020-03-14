<<<<<<< HEAD
import csv
with open('election_data.csv') as csv_file:
    polls = csv.reader(csv_file, delimiter=',') # import csv data
    candidate=[]        #candidate list
    votecnt = []        #votecount list for individual candidates
    pctvt = []          #pctvt list for individual candidates
    headder = next(polls)   #strip header
    totvote=0    #initialzie counter for the total number of votes
    for row in polls:
        totvote = totvote+1  #count vote
        isnew = True        # boolean for determining if this vote is for a new candidate
        for x in range(len(candidate)):  #loop to check for candidates already in candidate list
            if candidate[x] == row[2]:      
                votecnt[x] = votecnt[x] + 1  #count vote for candidate in list
                isnew = False               #sets boolean for new candidate to false
        if isnew == True:                   #conditional to determine if this vote is for a new candidate
           candidate.append(row[2])
           votecnt.append(1)
    for x in votecnt:                   #calculates percent of the vote for each candidate
        pctvt.append(100*x/totvote)
    print("Election Results")               #printing results to terminal
    print("-----------------------")
    print(f"Total Votes: {totvote}")    
    print("------------------------")
    wnnrpct = 0
    for x in range(len(candidate)):
        print(f"{candidate[x]}: {round(pctvt[x],2)}% ({votecnt[x]})")
        if pctvt[x] > wnnrpct:
            winner = candidate[x]
            wnnrpct = pctvt[x]
    print("------------------------")
    print(f"The winner is {winner}")
with open('election_results.txt', 'w') as text:   #printing results to text file election_results.txt
    text.write("Election Results \n")
    text.write(f"Total Votes: {totvote} \n")
    for x in range(len(candidate)):
        text.write(f"{candidate[x]}: {round(pctvt[x],3)}% ({votecnt[x]}) \n")
    text.write(f"The winner is {winner}!")
=======
import csv
with open('election_data.csv') as csv_file:
    polls = csv.reader(csv_file, delimiter=',') # import csv data
    candidate=[]        #candidate list
    votecnt = []        #votecount list for individual candidates
    pctvt = []          #pctvt list for individual candidates
    headder = next(polls)   #strip header
    totvote=0    #initialzie counter for the total number of votes
    for row in polls:
        totvote = totvote+1  #count vote
        isnew = True        # boolean for determining if this vote is for a new candidate
        for x in range(len(candidate)):  #loop to check for candidates already in candidate list
            if candidate[x] == row[2]:      
                votecnt[x] = votecnt[x] + 1  #count vote for candidate in list
                isnew = False               #sets boolean for new candidate to false
        if isnew == True:                   #conditional to determine if this vote is for a new candidate
           candidate.append(row[2])
           votecnt.append(1)
    for x in votecnt:                   #calculates percent of the vote for each candidate
        pctvt.append(100*x/totvote)
    print("Election Results")               #printing results to terminal
    print("-----------------------")
    print(f"Total Votes: {totvote}")    
    print("------------------------")
    wnnrpct = 0
    for x in range(len(candidate)):
        print(f"{candidate[x]}: {round(pctvt[x],2)}% ({votecnt[x]})")
        if pctvt[x] > wnnrpct:
            winner = candidate[x]
            wnnrpct = pctvt[x]
    print("------------------------")
    print(f"The winner is {winner}")
with open('election_results.txt', 'w') as text:   #printing results to text file election_results.txt
    text.write("Election Results \n")
    text.write(f"Total Votes: {totvote} \n")
    for x in range(len(candidate)):
        text.write(f"{candidate[x]}: {round(pctvt[x],3)}% ({votecnt[x]}) \n")
    text.write(f"The winner is {winner}!")
>>>>>>> fe3fce55be5f04456b922da48a6b0119f1540b52
