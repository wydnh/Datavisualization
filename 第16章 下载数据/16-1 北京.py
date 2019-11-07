# -*- coding:utf-8 -*-

import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'Beijing_2014.csv'
with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    highs, dates, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# fig = plt.figure(dpi=128, figsize=(10, 6))
# fig.autofmt_xdate()
# plt.tick_params(axis='both', which='major', labelsize=16)
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, alpha=0.5)
plt.fill_between(dates, lows, highs, alpha=0.1)
plt.title("Death high and low temperature - 2014", fontsize=24)
plt.xlabel('dates', fontsize=16)
plt.ylabel("temperature(F)", fontsize=16)
plt.show()
