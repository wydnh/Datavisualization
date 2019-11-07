# -*- coding:utf-8 -*-

import csv

import matplotlib.pyplot as plt

from datetime import datetime


def get_weather_date(filename, dates, lows, highs):
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                low = int(row[3])
                high = int(row[1])
            except ValueError:
                print(current_date, "missing data")
            else:
                dates.append(current_date)
                lows.append(low)
                highs.append(high)


# death weather
dates, lows, highs = [], [], []
get_weather_date('death_valley_2014.csv', dates, lows, highs)
# fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.3)
plt.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, lows, highs, alpha=0.05)

# sitka weather
dates, lows, highs = [], [], []
get_weather_date('sitka_weather_2014.csv', dates, lows, highs)
plt.plot(dates, highs, c='red', alpha=0.6)
plt.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, lows, highs, alpha=0.15)

plt.title("Death high and low temperature - 2014", fontsize=24)
plt.xlabel('dates', fontsize=16)
# fig.autofmt_xdate()
plt.ylabel("temperature(F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 120)
plt.show()
