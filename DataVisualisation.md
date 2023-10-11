---
title: "Data Visualisation Tools"
date: January 31 2023
fontsize: 12pt
---

[Home](/) &bull; [Autumn 2023 Meeting Schedule](/ProgramAutumn23.md) &bull; [Spring 2023 Meeting Schedule](/ProgramSpring23.md) &bull; [Data Visualisation with Python](/DataVisualisation.md) &bull; [Creating a Database with PostgreSQL](/PostgreSQL1.md) 


# Data Visualisation with Python - Examples

## Visualizing max. and min. manuscript dates from a csv. file using the plotting library Matplotlib

### Example 1

Tips: 
* The csv. file and the py. file with the script have to be in the same folder
* You can easily edit the "max_rows" value to include more or less data

<br>
import csv as csv
<br>
import matplotlib.pyplot as plt
<br>
file = open("file_name.csv", 'r')
<br>
csv_data = csv.reader(file)
<br>
manuscript_ids = []
<br>
manuscript_start_dates = []
<br>
manuscript_end_dates = []
<br>
manuscript_intervals = []
<br>
next(file)
<br>
row_count = 0
<br>
max_rows = 1000
<br>
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
<br>    
plt.barh(manuscript_ids, manuscript_intervals, left=manuscript_start_dates)
<br>
plt.xlabel("Years")
<br>
plt.ylabel("Manuscript number")
<br>
plt.title("Manuscript time periods")
<br>
plt.savefig('figure.png')
<br>
plt.show()
<br>
plt.close()