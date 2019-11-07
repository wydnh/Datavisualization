# -*- coding:utf-8 -*-

import csv

import matplotlib.pyplot as plt

from datetime import datetime


def get_weather_date(filename, dates, precipi_sums):
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for index, column in enumerate(header_row):
            print(index, column)
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                precipi_sum = int(row[18])

            except ValueError:
                print(current_date, "missing data")
            else:
                dates.append(current_date)
                precipi_sums.append(precipi_sum)


dates, precipi_sums = [], []
get_weather_date('beijing_2014.csv', dates, precipi_sums)

# fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, precipi_sums, c='red', alpha=0.5)
# plt.plot(dates, lows, alpha=0.5)
# plt.fill_between(dates, lows, highs, alpha=0.1)

plt.title("Death high and low temperature - 2014", fontsize=24)
plt.xlabel('dates', fontsize=16)
# fig.autofmt_xdate()
plt.ylabel("temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
