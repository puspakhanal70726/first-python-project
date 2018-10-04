import matplotlib.pyplot as plt
import numpy as np
import csv


years = []
id = []
values = []

with open("Virginia-max.csv") as csvfile:
    reader = csv.reader(csvfile)
    # reader = csv.reader(csvfile, quoting=csv.Quote_NORNUM)
    next(reader, None)
    next(reader, None)
    for row in reader: #each row is a lsit
    # results.append(row)
    # print (row)
        years.append(row[1])
        values.append(row[9])
plt.bar(years, values)
plt.xticks(rotation=45)
plt.show()
