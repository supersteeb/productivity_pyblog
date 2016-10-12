from sys import argv
import time

import csv

date_string = time.strftime("%Y-%m-%d")

script = argv

print "Opening the file..."
target = open(date_string + '.txt', 'w')

tasks_with_entry = ['code', 'read', 'exercise']
tasks = ['sudoku', 'chess', 'stretch lower back', 'do push-ups', 'forearm exercises', 'write left hand']
today = []

data = [date_string]

for i in range(len(tasks)):
    check = raw_input("Did you %s? (y/n) " % tasks[i])
    while check != 'y' and check != 'n':
    	check = raw_input("Sorry, I didn't catch that. Enter again: ")
    if check == 'y':
    	data.append(True)
    	print data
        target.write(tasks[i] + ": x")
        target.write("\n")
        print "wrote to text file that completed"
    if check == 'n':
    	data.append(False)
    	print data
        target.write(tasks[i] + ": ")
        target.write("\n")
        print "wrote to textfile that not completed. can always do later and change manually."

for i in range(len(tasks_with_entry)):
    check = raw_input("Did you %s? (y/n) " % tasks_with_entry[i])
    while check != 'y' and check != 'n':
    	check = raw_input("Sorry, I didn't catch that. Enter again: ")
    if check == 'y':
    	data.append(True)
    	entry = raw_input("Entry: ")
    	data.append(entry)
        target.write(tasks_with_entry[i] + ": " + entry)
        target.write("\n")
        target.write("\n")
    	print data
    if check == 'n':
    	data.append(False)
    	print data
    	data.append('')

journal = raw_input("Write what you've learned here (try to get 100 words) - or about any random topic. Don't press enter until you're done:\n")
data.append(journal)

print "\n"
print "Writing to text file..."

target.write("Journal:\n" + journal)

count_words = journal.split()
print "\nYou've written %d words.\n" % (len(count_words))

print "Thank you."
print "\n"
print "If you didn't finish any of them but finish them later but before the day is over, go to the text file and edit it."
target.close()

b = open('test1.csv', 'ab')
a = csv.writer(b)
data1 = [data]
a.writerows(data1)
b.close()