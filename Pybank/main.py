#py_budget
print("Financial Analysis")
print("----------------------------------")

import os 
import csv


csvpath ="./Resources/budget_data.csv"

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #I coded the lines because line count is the same as number of months presumably 
   
    #skip first row 
    next(csvreader, None)
    
#variables
    linecount=0
    total=0
    totalchange_mean=0
    increase=0
    decrease=0
    total_change=0 
    change=0 
    previousrow=0
    current=0
    #empty month 
    month=0
    increasemonth=0
    decreasemonyh=0
    #storing things in a list
    oc=[]

    for row in csvreader:
        #date.append(row[0])
        linecount+=1
        total=total+int(row[1])
        #setting a special case for row 2 two becase our change for row 2 is 0 
        #below code for calc average change
        if csvreader.line_num==2:
            previousrow=int(row[1])
        change=int(row[1])-previousrow
        total_change=total_change+change
        previousrow=int(row[1])

        # #for greatest increase
        if (increase<int(row[1])):
            increase=int(row[1])
            increasemonth=row[0]
            
        # #for greatest decrease
        if(decrease>int(row[1])):
            decrease=int(row[1])
            decreasemonth=row[0]

    totalchange_mean=total_change/linecount

    print(f'Total months:{linecount}')
    print(f'Total:${total}')
    print(f'Average Change:${round(totalchange_mean,2)}')
   
    print(f'Greatest Increase in Profits:{increasemonth}(${increase})')
    print(f'Greatest Decrease in Profits:{decreasemonth}(${decrease})')
#Don't forget output

f = open("analysis.txt", "w")
f = open("analysis.txt", "a")
f.write("Financial Analysis")
f.write("-------------------------")
f.write("Total months:" + str(linecount))
f.write("-------------------------")
f.write("Total:$"+ str(total))
f.write("Average Change:$"+str(round(totalchange_mean,2)))
f.write("'Greatest Increase in Profits:"+str(increasemonth)+"  $"+str(increase))
f.write("'Greatest Decrease in Profits:"+str(decreasemonth)+"  $"+str(decrease))
