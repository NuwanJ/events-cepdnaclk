from ics import Calendar, Event
import csv
from datetime import datetime
from dateutil import parser

'''
Can use a URL like following to directly download a CSV from a Google Sheet:
    https://docs.google.com/spreadsheets/d/{document-id}}/export?format=csv

Ex: https://docs.google.com/spreadsheets/d/1FGwBpZRo-BmWurgfO3RNLQ9_hwGfHGJVma8YyWfM_T8/export?format=csv
'''

# Read the CSV File from a Google Sheet -----
import requests
url = 'https://docs.google.com/spreadsheets/d/1FGwBpZRo-BmWurgfO3RNLQ9_hwGfHGJVma8YyWfM_T8/export?format=csv'
r = requests.get(url)
text = r.content.decode('utf-8')
csvreader = csv.reader(text.splitlines(), delimiter=',')

# # Read the CSV file from  local -------------
# file = open('data/data.csv')
# csvreader = csv.reader(file)
# #type(file)
# file.close()

# ---------------------------------------------

# Read the header of the CSV
header = []
header = next(csvreader)

# Read the data rows of the CSV
rows = []
for r in csvreader:
    row = {}
    res = {header[i]: r[i].strip('"') for i in range(len(header))}
    rows.append(res)
    # print(res)

# print(header)
# print(rows)


# Generate the ics compatible event list
c = Calendar()

for event in rows:
    # Prepare the date and time
    e_date = event['date']
    e_time = event['time']
    e_datetime = e_date + ' ' + e_time if (e_time != "None") else e_date
    e_begin =  parser.parse(e_datetime)

    e = Event()
    e.name = event['description']
    e.begin = e_begin
    e.description = event['description']
    e.url = event['link']
    # e.categories = event['tags']
    c.events.add(e)

# print(c.events)

# Write the events into ics file
with open('icalexport.ics', 'w') as my_file:
    my_file.writelines(c)
