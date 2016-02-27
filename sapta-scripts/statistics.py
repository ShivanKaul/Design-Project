import math 

class statistics:

	def __init__(self, funbun):
		self.funbun = funbun

	def mymean (self, mylist):
		i = 0
		me = 0.0
		length = len(mylist)
		while i < len(mylist):
			me = me + mylist[i]
			i = i+1
		
		return me/(length)


	def standardev (self, mylist):
		i = 0
		std = 0.0
		mea = self.mymean(mylist)
		while i < len(mylist):
			num = abs(mylist[i] - mea)
			num = math.pow(num, 2)
			std = std + num
			i = i + 1
		std = std/(len(mylist)-1)
		std = math.sqrt(std)
		return std


	def stats (self, mylist, ol):
		i = 0
		j = 0
		temp = []
		stdx = []
		length = len(mylist)-1
		while i < len(mylist):
			temp.append(mylist[i])
			i = i+1
			j = j+1
			if (j == ol or i == length):
				if(len(temp) == 1):
					j = 0
					temp = []
				else:
					j = 0
					stdx.append(self.standardev(temp))
					temp = []
		return stdx 
	
	def difference (self, mylist):
		i = 0
		diff = []
		temp = self.mymean(mylist)
		while i < len(mylist):
			num = mylist[i] - temp
			num = abs(num)
			diff.append(num)
			temp = mylist[i]
			i = i+1
		
		return diff

	def rootmean (self, mylist, ol):
		i = 0
		j = 0
		temp = []
		rootmeansq = []
		length = len(mylist)-1
		while i < len(mylist):
			temp.append(mylist[i])
			i = i+1
			j = j+1
			if (j == ol or i == length+1):
				if(len(temp) == 1):
					j=0
					temp=[]
				else:
					j = 0
					rootmeansq.append(self.rootmeansquare(temp))
					temp =[]
		return rootmeansq		

	def rootmeansquare (self, mylist):
		rootmeansq = 0.0
		i = 0
		while i < len(mylist):
			rootmeansq = math.pow(mylist[i], 2) + rootmeansq
			i = i+1
		rootmeansq = math.sqrt(rootmeansq/(len(mylist)))
		return rootmeansq
	
	def mymeanps (self, mylist, ol):
		i = 0
		j = 0
		temp = []
		my2 = []
		length = len(mylist)-1
		while i < len(mylist):
			temp.append(mylist[i])
			i = i+1
			j = j+1
			if (j == ol or i == length):
				if(len(temp) == 1):
					j = 0
					temp = []
				else:
					j = 0
					my2.append(self.mymean(temp))
					temp = []
		return my2 	

	def lineread(self, mylist):
		Y = (len(mylist) + 1)/2
		y = 0
		X = self.mymean(mylist)
		slope = 0.0
		temp = 0.0
		while y < len(mylist): 
			temp = ((mylist[y] - X)*(y - Y))/(math.pow(mylist[y] - X, 2))
			slope = temp + slope 
		return slope	