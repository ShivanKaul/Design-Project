import sys

def filterOM(lines):
	print lines
	started = False
	resting = False
	data = []
	cell = []
	for line in lines:
		splut = line.split(" ")
		if 'H:' in line:
			started = True
			H = splut[1]
			T = splut[3]
			cell.append(T)
			cell.append(H)
		elif 'B:' in line:
			B = splut[1]
			cell.append(B)
			data.append(cell)
			cell = []
		elif started and not resting:
			data.append([" "])
			resting = True

	return data

def filter(filename):
	openFile = open(filename, 'rU')
	allLines = openFile.read().splitlines()
	data = filterOM(allLines)
	return data
