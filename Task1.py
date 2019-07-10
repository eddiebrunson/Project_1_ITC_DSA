"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Top level array of different telephone numbers
differentNumbers = []

for row in texts:
    if row[0] not in differentNumbers:
        differentNumbers.append(row[0])

    if row [1] not in differentNumbers:
        differentNumbers.append(row[1])

for row in calls:
    if row[0] not in differentNumbers:
        differentNumbers.append(row[0])

    if row[1] not in differentNumbers:
        differentNumbers.append(row[1])
        
print("There are {len(differentNumbers)} different telephone numbers \
 in the records.")
