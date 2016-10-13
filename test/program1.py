#practice

from sys import argv
import time

import csv

date_string = time.strftime("%Y-%m-%d")

script = argv



print "Opening the file..."
target = open(date_string + '.txt', 'w')

tasks_with_entry = ['code', 'read', 'train']
tasks = ['sudoku', 'ricochet robots', 'run', 'forearm exercises']
today = []

for i in range(len(tasks)):
    check = raw_input("Did you %s? (y/n) " % tasks[i])
    while check != 'y' and check != 'n':
    	check = raw_input("Sorry, I didn't catch that. Enter again: ")
    if check == 'y':
    	target.write(tasks[i] + ": x")
    	target.write("\n")
    		# add to database for date.time == True
    if check == 'n':
    	target.write(tasks[i] + ": ")
    	target.write("\n")
    		# add to database for date.time.now == False

for i in range(len(tasks_with_entry)):
    check = raw_input("Did you %s? (y/n) " % tasks_with_entry[i])
    while check != 'y' and check != 'n':
        check = raw_input("Sorry, I didn't catch that. Enter again: ")
    if check == 'y':
        target.write(tasks_with_entry[i] + ": x\n")
        entry = raw_input("Elaborate:\n")
        target.write(entry)
        target.write("\n")
            # add to database for date.time == True
    if check == 'n':
        target.write(tasks_with_entry[i] + ": ")
        target.write("\n")
            # add to database for date.time.now == False

journal = raw_input("Write what you've learned here (try to get 100 words) - or about any random topic. Don't press enter until you're done:\n")
target.write("\n")
target.write("journal: ")
target.write(journal)

count_words = journal.split()
print "\nYou've written %d words.\n" % (len(count_words))

print "Thank you."
print "\n"
print "If you didn't finish any of them but finish them later but before the day is over, go to the text file and edit it."
target.close()