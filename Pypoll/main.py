<<<<<<< HEAD
#Pypoll
print("Election Results")
print("-------------------------")
from ast import NotIn
import os 
import csv

from matplotlib.collections import LineCollection

csvpath ="./Resources/election_data.csv"

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip first row
    next(csvreader, None)
  
    #set variables
    linecount=0
    totalvotes=0
    c_list=[]
    v_list=[]
    canditate=0
    votepercent=0
    winner=0
    winnerv_list=0
  
    
#counting total and getting list of candidates 
    for row in csvreader:
        totalvotes+=1
 
    #list of all of the individual candidates in list within the voter list then printing them
        if (row [2] not in c_list):
            c_list.append(row[2])
            v_list.append(0)
        c_index=c_list.index(row[2])
        v_list[c_index]+=1
print(f'Total Votes:{totalvotes}')
print("-------------------------")

#printing the winner and getting alist of all the cadidates
for x in range(len(c_list)):
        voteper=round((v_list[x]/totalvotes)*100,3)
        #printing the list of candidates
        print(f"{c_list[x]}:{voteper}% ({v_list[x]})")
        if winnerv_list<v_list[x]:
            winnerv_list=v_list[x]
            winner=c_list[x]

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")



f = open("analysis.txt", "w")
f = open("analysis.txt", "a")
f.write("Election Results")
f.write("-------------------------")
f.write("Total votes:" + str(totalvotes))
f.write("-------------------------")

for x in range(len(c_list)):
    voteper = round((v_list[x]/totalvotes)*100,3)
    f.write("\n" + str(c_list[x]) +" : " + str(voteper) 
                + "% ("+ str(v_list[x]) + ")")

f.write("-------------------------")
# print(winner)
f.write("Winner: " + str(winner))
f.write("-------------------------")



=======
#Pypoll
print("Election Results")
print("-------------------------")
from ast import NotIn
import os 
import csv

from matplotlib.collections import LineCollection

csvpath ="./Resources/election_data.csv"

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip first row
    next(csvreader, None)
  
    #set variables
    linecount=0
    totalvotes=0
    c_list=[]
    v_list=[]
    canditate=0
    votepercent=0
    winner=0
    winnerv_list=0
  
    
#counting total and getting list of candidates 
    for row in csvreader:
        totalvotes+=1
 
    #list of all of the individual candidates in list within the voter list then printing them
        if (row [2] not in c_list):
            c_list.append(row[2])
            v_list.append(0)
        c_index=c_list.index(row[2])
        v_list[c_index]+=1
print(f'Total Votes:{totalvotes}')
print("-------------------------")

#printing the winner 
for x in range(len(c_list)):
        voteper=round((v_list[x]/totalvotes)*100,3)
        print(f"{c_list[x]}:{voteper}% ({v_list[x]})")
        if winnerv_list<v_list[x]:
            winnerv_list=v_list[x]
            winner=c_list[x]

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")



f = open("analysis.txt", "w")
f = open("analysis.txt", "a")
f.write("Election Results")
f.write("-------------------------")
f.write("Total votes:" + str(totalvotes))
f.write("-------------------------")

for x in range(len(c_list)):
    voteper = round((v_list[x]/totalvotes)*100,3)
    f.write("\n" + str(c_list[x]) +" : " + str(voteper) 
                + "% ("+ str(v_list[x]) + ")")

f.write("-------------------------")
# print(winner)
f.write("Winner: " + str(winner))
f.write("-------------------------")



>>>>>>> b6673d509c7e7f8793e7411ef5797a1dfed3d6ad
