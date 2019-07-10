"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds,
 on the phone during September 2016.".
"""
# Variable to hold the longest time spent on the phone and its telephone number

longest_time = 0
longest_telephone_number = None

# A dictionary that saves each number
numbers_per_call = {}

for call in calls:









print (f"{longest_telephone_number} spent the longest time, {longest_time} \
seconds, on the phone during September 2016."
