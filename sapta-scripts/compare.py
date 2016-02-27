import matplotlib
import numpy as np
import matplotlib.pyplot as plt

import math 
from statistics import *
class compare:

	dork = []
	pork = []
	cork = []
	fork = []

	sock = 0.0
	lock = 0.0

	def __init__(self, mylist1, mylist2, ol):
		self.mylist1 = mylist1
		self.mylist2 = mylist2
		self.ol = ol

	def maximus (self, mylist3):
		i = 0
		j = 0
		k = 0
		temp = []
		mylist = []
		length = len(mylist3)-1
		while i < len(mylist3):
			temp.append(mylist3[i])
			j = j+1
			i = i+1
			if (j == self.ol or i == length):
				if(len(temp) == 1):
					j = 0
					temp=[]
				else:
					j = 0
					mylist.append(temp)
					k = k+1
					temp = []
		return mylist			

	def clear(self):
		self.dork[:] = [] 	
	
	def xavier (self):
		self.dork = self.maximus(self.mylist1)
		self.pork = self.maximus(self.mylist2)
		base = 0.0 
		mars = statistics(self.pork[0])
		venus = statistics(self.pork)
		base = mars.mymean(self.pork[0])
		statbase = mars.mymean(self.pork[0])
		# i = 0
		# temp = 0.0 
		# temp1 = 0.0
		# temp2 = 0.0
		# slop = 0.0
		# while i < len(self.pork): 
		# 	while j < len(self.pork[i]): 
		# 		temp = self.pork[i][j]
		# 		j = j + 1
		# 		if (temp > base+8.0):			#need to change the value for threshhold
		# 			temp1 = venus.standardev(self.pork[i])
		# 			if(temp1 > statbase*2):		#checks the standard deviation for the subset 
		# 				temp2 = venus.rootmenasquare(self.pork[i])		#checks the rootmean value to determine if physical 
		# 				if(temp2 > 84.0):
		# 					print 'Physical Activity'
		# 				elif(self.hitler(i) > ):
		# 						#do something here to determine if hte slope is steep enough to classify as emotion
		# 		elif (venus.mymean(self.pork[i]) < base):
		# 			base = venus.mymean(self.pork[i])
	
	#this just calculates the gradient of best fit line between the previous subset and present subset min and max values.	
	def hitler (self, k):
	 	min1 = min(self.pork[k-1])
	 	mx1 = max(self.pork[k])
	 	merged = []
	 	merged = self.pork[k-1] + self.pork[k]
	 	jupiter = statistics(calcifer)
	 	calcifer = []
	 	i = merged.index(min(merged))
	 	while i <= merged.index(max(merged)):
	 		calcifer.append(merged[i])
	 		i = i + 1
	 	return 	jupiter.lineread(calcifer)
