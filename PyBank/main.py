#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd
import numpy_financial as npf
import numpy as np


# In[5]:


from pathlib import Path


# In[ ]:


### Homework PyBank


# In[ ]:


# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset.
# The net total amount of Profit/Losses over the entire period.
# The average of the changes in Profit/Losses over the entire period.
# The greatest increase in profits (date and amount) over the entire period.
# The greatest decrease in losses (date and amount) over the entire period.


#   Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38,382,578
# Average Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1,926,159)
# Greatest Decrease in Profits: Sep-2013 ($-2,196,167)


# In[6]:


print(f"current working directory:{Path.cwd()}")


# In[108]:


import os
import csv

# set you file path for txt file and import csv
csvpath=os.path.join("Resources", "budget_data.csv")
txtpath=os.path.join("Analysis", "BudgetAnalysis.txt")

# define your variables
total_months=0
net_pnl=0
avg_pnl=0
net_change_list=[]
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]


with open(csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    # handle first row of data
    
    first_row=next(csvreader)
    total_months+=1
    net_pnl+=int(first_row[1])  
    previous_net_pnl=int(first_row[1])
    
    #for loop
    
    for i in csvreader:
        total_months+=1
        net_pnl+= int(i[1])
        net_change=int(i[1])-previous_net_pnl
        previous_net_pnl=int(i[1])
        net_change_list.append(net_change)
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[1] = net_change
            greatest_decrease[0] = i[0]
        if net_change > greatest_increase[1]:
            greatest_increase[1] = net_change
            greatest_increase[0] = i[0]
    

avg_change=sum(net_change_list)/len(net_change_list)

output = (
    f"Financial Analysis\n"
    f"--------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_pnl}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)


with open(txtpath,'w') as text:
    text.write(output)


# In[ ]:





# In[ ]:





# In[ ]:




