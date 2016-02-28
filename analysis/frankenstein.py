import math
import csv 

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
class frankenstein:

	hear = []
	sk = []
	tim = []

	def __init__(self, infile):
		self.infile = infile

	def verne (self):
		line = csv.reader(self.infile)
		data = tuple(line)
		x = []
		i = 0
		j = 0 
		while i < len(data):
			if(data[i][2] != ''):
				x.append(data[i])
			i = i+1
		
		while j < len(x):
			self.hear.append(float(x[j][2]))
			self.sk.append(float(x[j][1]))
			self.tim.append(float(x[j][0]))
			j = j+1		

	def heart(self):
		return self.hear
	
	def skin(self):
		return self.sk

	def time (self):
		return self.tim

	def filter (self, mylist, q, r, p, k):
		i = 0
		x = mylist[0]
		filtered = []
		while i < len(mylist):
			p = p + q			
			k = p/(p + r)
			x = x + k*(mylist[i] - x)
			p = (1-k)*p
			filtered.append(x)
			i = i+1	
		return filtered	

	def clear (self):
		self.heart[:] = []	
		self.skin[:] = []
		self.time[:] = []