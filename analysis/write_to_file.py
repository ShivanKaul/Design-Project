import sys
import filter
import csv
import os

def call_filter(filename):
	# data = filter.filter(sys.argv[1])
	data = filter.filter(filename)

	# Write to output.csv
	with open(os.path.join(os.path.expanduser('~'),'Documents/Design-Project/analysis/OM',os.path.splitext(filename)[0] + '.csv'), "w") as f:
		writer = csv.writer(f)
		writer.writerows(data)
