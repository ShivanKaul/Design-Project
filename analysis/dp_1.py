import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import csv
import os 
import glob

# importing class 
from convert_csv import *
from base import *
from compare import *
from value import *

for files in glob.glob("*.csv"):
	infile = open(files, "r")

	if 'fear' in os.path.basename(infile.name):
		tag = 'fear'
	elif 'happy' in os.path.basename(infile.name):
		tag = 'happy'
	else:
		tag = 'physical'
	# initiate all lists
	oxy_1 = []
	hea =[]
	sk = []
	time =[]
	x = []
	# call for conversion 
	test1 = convert_csv(infile, tag)
	# need to do this for every file 
	test1.clear()						
	x = test1.generate() # list of tuples 
	hea = test1.heart()
	sk = test1.skin()
	time = test1.time()
	# filter 
	oxy_1 = test1.filter(sk, q=590.0, r=50000.0, p=399900.0, k=0.0) 
	oxy_2 = test1.filter(hea, q=0.99, r=260.0, p=1000.0, k=0.0)
	#print the plot
	plt.figure(1)
	plt.subplot(211)
	plt.plot(sk, 'r')
	plt.plot(oxy_1, 'b')

	plt.subplot(212)
	plt.plot(hea, 'r')
	plt.plot(oxy_2, 'b')

	plt.show()
