import math


infile = open("C:\Users\wearable\IT.txt", "r")
infile2 = open("C:\Users\wearable\it2.txt", "r")
line = infile.readlines()
line2 = infile2.readlines()
infile.close()
infile2.close()
i = 0
original = []
original2 =[]
filtered = []
while i < len(line):
	num = float(line[i])
	original.append(num)
	i = i+1
i = 0
while i < len(line2):
	num = float(line2[i])
	original2.append(num)
	i = i+1

#print original
#print 
#print original2


def filter (q, r, p, k, mylist):
	i = 0
	x = mylist[0]
	while i < len(mylist):
		p = p + q
		k = p/(p + r)
		x = x + k*(mylist[i] - x)
		p = (1-k)*p
		filtered.append(x)
		i = i+1
	return 

filter(10.0, 500.0, 1000.0, 0.0, original2)

#print filtered 
#print

def mymean (mylist):
	i = 0
	me = 0.0
	length = len(mylist)
	while i < len(mylist):
		me = me + mylist[i]
		i = i+1
	
	return me/(length)

#print mymean(original)

def standardev (mylist):
	i = 0
	std = 0.0
	mea = mymean(mylist )
	while i < len(mylist):
		num = abs(mylist[i] - mea)
		num = math.pow(num, 2)
		std = std + num
		i = i + 1
	std = std/(len(mylist)-1)
	std = math.sqrt(std)
	return std

#print standardev(original)

def stats (mylist, ol):
	i = 0
	j = 0
	temp = []
	stdx = []
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
				stdx.append(standardev(temp))
				temp =[]

	return stdx 

def difference (mylist):
	i = 0
	diff = []
	temp = mymean(mylist)
	while i < len(mylist):
		num = mylist[i] - temp
		num = abs(num)
		diff.append(num)
		temp = mylist[i]
		i = i+1
	
	return diff

#print difference(original2)	
print stats(difference(original2), 35)
print stats(difference(original), 75)
print stats(original2, 35)
print stats(original, 75)

