import sys
import filter
import csv

data = filter.filter(sys.argv[1])

with open("output.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(data)
