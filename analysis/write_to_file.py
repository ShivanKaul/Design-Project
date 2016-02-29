import sys
import filter
import csv

def call_filter(filename):
	# data = filter.filter(sys.argv[1])
	data = filter.filter(filename)

	# Write to output.csv
	with open(filename + ".csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(data)
