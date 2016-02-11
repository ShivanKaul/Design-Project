import sys
import filterPhys
import csv

data = filterPhys.filter(sys.argv[1])

with open("output.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(data)
