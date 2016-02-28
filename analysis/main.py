import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import csv
import os 
import glob

from converter import Converter
from base import *
from compare import *

listOfTuples = []

def plot(skin, filtered_skin, heart, filtered_heart):
	plt.figure(1)
	plt.subplot(211)
	plt.plot(skin, 'r')
	plt.plot(filtered_skin, 'b')
	plt.subplot(212)
	plt.plot(heart, 'r')
	plt.plot(filtered_heart, 'b')

# Start main script
for file in glob.glob("*.csv"):
	if file == "listOfTuples.csv":
		continue
	infile = open(file, "r")
	print file

	# Assign tags
	if 'fear' in os.path.basename(infile.name):
		tag = 'fear'
	elif 'happy' in os.path.basename(infile.name):
		tag = 'happy'
	else:
		tag = 'physical'

	# Convert
	converter = Converter(infile, tag)

	listOfTuples.append(converter.generate())
	heart = converter.heart()
	skin = converter.skin()
	time = converter.time()

	# Filter 
	filtered_skin = converter.filter(skin, q=590.0, r=50000.0, p=399900.0, k=0.0) 
	filtered_heart = converter.filter(heart, q=0.99, r=260.0, p=1000.0, k=0.0)

	# Plot
	plot(skin, filtered_skin, heart, filtered_heart)

	# Print to file
	with open("listOfTuples.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(listOfTuples)


