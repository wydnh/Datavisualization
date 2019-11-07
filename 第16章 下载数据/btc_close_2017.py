# import requests
#
# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# req = requests.get(json_url)
# with open('btc_close_2017_request.json', 'w') as f:
#     f.write(req.text)
# file_requests = req.json()

import json

import pygal

import math


def get_btc_data(filename, dates, months, weeks, weekdays, closes):
    with open(filename) as f:
        btc_date = json.load(f)
        # print(btc_date)

    for btc_dict in btc_date:
        date = btc_dict['date']
        month = int(btc_dict['month'])
        week = int(btc_dict['week'])
        weekday = btc_dict['weekday']
        close = int(float(btc_dict['close']))
        dates.append(date)
        months.append(month)
        weeks.append(week)
        weekdays.append(weekday)
        closes.append(close)

        line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
        line_chart.x_labels = dates
        closes_log = [math.log10(_) for _ in closes]
        line_chart.add('收盘价', closes_log)

        line_chart.title = '收盘价(¥)'
        line_chart.x_labels_major = dates[::20]
        line_chart.render_to_file('收盘价折线图(¥).svg')


filename = 'btc_close_2017.json'
dates, months, weeks, weekdays, closes = [], [], [], [], []
get_btc_data(filename, dates, months, weeks, weekdays, closes)
