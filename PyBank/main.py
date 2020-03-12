import csv
with open('budget_data.csv') as csv_file:
    budget = csv.reader(csv_file, delimiter=',')   #import the csv data
    income = 0              #initialize accounting variables
    x=0             #month counter
    avgsum = 0      # sum for average change
    prevyr = 0      #initialze the profit of a previous year holder
    biginc=0        #initial value for determining the month with the greatest increase
    bigdec=0        #initial value for determining the month with greatest decrease
    headder = next(budget)    #strip the header
    for row in budget:                    #loop start
        income = income + float(row[1])    #calculate net income
        curyr = float(row[1])              # initialize current year's  profit/loss
        if x >0:                            # starts the calculation for average change on second month
            avgsum = avgsum + curyr - prevyr
        if curyr-prevyr > biginc:           #conditional for determining if this month had the greatest increase
            biginc= curyr-prevyr
            dateinc = row[0]
        elif curyr-prevyr < bigdec:         #conditional for determining if this month had the greatest decrease
            bigdec= curyr-prevyr
            datedec = row[0]
        prevyr = curyr                      #stores this months profit for next step in loop
        x = x+1                             #count the months
    avgchg = avgsum / (x-1)
    print(f"Total Months: {x}")             #print results to terminal
    print(f"Total: ${income}")
    print(f"Average Change: ${round(avgchg,2)}")
    print(f"Createst Increase in Profits: {dateinc}(${biginc})")
    print(f"Greatest Decrease in Profits: {datedec}(${bigdec})")
    with open('budget.txt', 'w') as text:       #print results to text file budget.txt
        text.write(f"Total Months: {x} \n")
        text.write(f"Total: ${income} \n")
        text.write(f"Average Change: ${round(avgchg,2)} \n")
        text.write(f"Createst Increase in Profits: {dateinc}(${biginc}) \n")
        text.write(f"Greatest Decrease in Profits: {datedec}(${bigdec}) \n")
    