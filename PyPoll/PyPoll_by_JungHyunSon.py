#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
csvpath = os.path.join("Resources","election_data.csv")


# In[2]:





with open(csvpath, 'r') as csvfile:
    csvread = csv.DictReader(csvfile)
#     next(csvread, None)
    vote_count = {}
    

  
    for row in csvread:
#         print(row)
        if row["Candidate"] in vote_count:
            vote_count[row["Candidate"]] = vote_count[row["Candidate"]]+1
        else: 
            vote_count[row["Candidate"]] = 1


# In[3]:


totalvotes = 0
totalvotes = sum(vote_count.values())


# In[4]:


candidates = []
results = []

for key, value in vote_count.items():
    candidates.append(key)
    results.append(value)


# for row in candidates:
#     print(row)


# In[5]:


percentages =[]

for row in results:
    percentages.append('{:.3%}'.format(row/totalvotes))

    


# In[6]:


# election_dict = {candidates[i]:[percentages[i], results[i]] for i in range(0,len(candidates))}
# election_dict["Khan"]


election_zip = list(zip(candidates, results, percentages))


winner = ""

for row in election_zip:
    if max(results) == row[1]:
        winner = row[0]

# print(winner)


# In[7]:


# for x,y in election_dict.items():
#     print (f"{x} {election_dict[x]}")

print("Election Results")
print("------------------------- ")
print(f"Total Votes: {totalvotes} ")
print("------------------------- ")
for row in election_zip:
    print(f"{row[0]} {row[2]} ({row[1]})")
# for key,value in election_dict.items():
#     print("{}:  {}".format(key,value))   
print("------------------------- ")
print(f"Winner: {winner}")    
print("------------------------- ")


# In[8]:




output_path = os.path.join("PyPoll_output.txt")
with open(output_path, 'w', newline='') as outfile:
    outfile.write("Election Results\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Votes: {totalvotes} \n")
    outfile.write("----------------------------\n")
    for row in election_zip:
        outfile.write(f"{row[0]} {row[2]} ({row[1]})\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Winner: {winner}\n")


# In[ ]:





# In[ ]:




