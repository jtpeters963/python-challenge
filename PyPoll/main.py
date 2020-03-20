import csv
with open('../election_data.csv') as csv_file:
    polls = csv.reader(csv_file, delimiter=',') # import csv data
    candidate={}        #candidate dictionary initialization
    totvote=0 
    head = next(polls)   #strip header
    for row in polls:
        totvote = totvote+1  #count vote
        if row[2] not in candidate:
            candidate.update({row[2]:1})   #append dictionary with new candidates
        else:
             candidate[row[2]] = candidate[row[2]]+1    #counting votes for the candidate
    print("Election Results")               #printing results to terminal
    print("-----------------------")
    print(f"Total Votes: {totvote}")    
    print("------------------------")
    winct = 0
    for x in candidate:
        print(f"{x}: {round(100*candidate[x]/totvote,2)}% ({candidate[x]})")
        if candidate[x] > winct:
            winner = x
            winct = candidate[x]
    print("------------------------")
    print(f"The winner is {winner}")
with open('election_results.txt', 'w') as text:   #printing results to text file election_results.txt
    text.write("Election Results \n")
    text.write(f"Total Votes: {totvote} \n")
    for x in candidate:
        text.write(f"{x}: {round(100*candidate[x]/totvote,2)}% ({candidate[x]}) \n")
    text.write(f"The winner is {winner}!")
