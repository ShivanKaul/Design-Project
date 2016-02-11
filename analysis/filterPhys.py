import sys

def filterOM(lines):
	data = []
	cell = []
	for line in lines:
		splut = line.split(" ")
		if 'H:' in line:
			H = splut[1]
			T = splut[3]
			cell.append(T)
			cell.append(H)
		elif 'B:' in line:
			B = splut[1]
			cell.append(B)
			data.append(cell)
			cell = []
	return data

def filter(filename):
	openFile = open(filename, 'rU')
	allLines = openFile.read().splitlines()
	data = filterOM(allLines)
	print data
	return data
