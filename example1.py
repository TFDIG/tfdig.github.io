# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:40:13 2023

@author: serenanb
"""

import csv as csv 
import matplotlib.pyplot as plt

file = open("example1.csv", 'r')

csv_data = csv.reader(file)

manuscript_ids = [] 
manuscript_start_dates = [] 
manuscript_end_dates = [] 
manuscript_intervals = []

next(file)

row_count = 0 
max_rows = 5

for row in csv_data:
    
    row[1] = int(row[1])
    row[2] = int(row[2])

    manuscript_ids.append(row[0])
    manuscript_start_dates.append(row[1])
    manuscript_end_dates.append(row[2])
    manuscript_intervals.append(row[2] - row[1])

    row_count += 1
    if(row_count >= max_rows):
        break

file.close()    
   

plt.barh(manuscript_ids, manuscript_intervals, left=manuscript_start_dates) 
plt.xlabel("Years") 
plt.ylabel("Manuscript number") 
plt.title("Manuscript time periods") 
plt.savefig('figure.png') 
plt.show() 
plt.close()