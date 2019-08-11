#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv


# In[4]:


csvpath = os.path.join("Resources","budget_data.csv")
# csvpath


# In[5]:


with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)

    months = []
    for row in csv_reader:
        months.append(row[0])
    
    nummonths = (len(months))
    

    
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
        
    nettotal = 0
    for row in csv_reader:
        nettotal += float(row[1])
        


# In[6]:




with open(csvpath, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    
    profitloss_change=[]
    profitloss = [] 
    profitloss_date= []
    
    
    for row in csv_reader:
        profitloss.append(row[1])
        profitloss_date.append(row[0])
    
    for row in range(1,len(profitloss)):
        profitloss_change.append(float(profitloss[row]) - float(profitloss[row-1]))
                          
    avg_change = sum(profitloss_change)/len(profitloss_change)
    avg_change = round(avg_change,2)
    max_change = round(max(profitloss_change))
    min_change = round(min(profitloss_change))
    
    max_change_date_index = profitloss_change.index(max(profitloss_change))
    max_change_date =profitloss_date[max_change_date_index+1]
    min_change_date_index = profitloss_change.index(min(profitloss_change))
    min_change_date =profitloss_date[min_change_date_index+1]
    
    
    
    print ("Financial Analysis")
    print ("----------------------------")
    print (f"Total Months: {nummonths}")
    print(f"Total: ${int(nettotal)}")
    print (f"Average  Change: ${avg_change}")
    print (f"Greatest Increase in Profits: {max_change_date} (${max_change}) ")
    print (f"Greatest Decrease in Profits: {min_change_date} (${min_change}) ")
          


# In[7]:


output_path = os.path.join("PyBank_output.txt")
with open(output_path, 'w', newline='') as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {nummonths}\n")
    outfile.write(f"Total: ${int(nettotal)}\n")
    outfile.write(f"Average  Change: ${avg_change}\n")
    outfile.write(f"Greatest Increase in Profits: {max_change_date} (${max_change})\n")
    outfile.write(f"Greatest Decrease in Profits: {min_change_date} (${min_change})\n")
    

