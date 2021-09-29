from ics import Calendar, Event
import csv
from datetime import datetime
from dateutil import parser

# Read the CSV File -------------------------
file = open('data/data.csv')
csvreader = csv.reader(file)
# type(file)

header = []
header = next(csvreader)

rows = []
for r in csvreader:
    row = {}
    # for item in r:
        # print(item)
    res = {header[i]: r[i].strip('"') for i in range(len(header))}
    rows.append(res)
    # print(res)

file.close()

# print(header)
# print(rows)

c = Calendar()

for event in rows:
    e = Event()
    e_desc = event['description']
    e_date = event['date']
    e_time = event['time']

    if(e_time != "None"):
        e_datetime = e_date + ' ' + e_time
    else:
        e_datetime = e_date

    print(e_datetime)
    print(e_desc)

    e_begin =  parser.parse(e_datetime + " +05:30")

    e.name = e_desc
    e.begin = e_begin
    e.description = event['description']
    e.url = event['link']
    # e.categories = event['tags']
    c.events.add(e)

# print(c.events)

with open('icalexport.ics', 'w') as my_file:
    my_file.writelines(c)
