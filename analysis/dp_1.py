import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import csv
import os 
from convert_csv import *
from base import *
from compare import *

infile = open("physical_walking.csv", "r")
if 'fear' in os.path.basename(infile.name):
	tag = 'fear'
elif 'happy' in os.path.basename(infile.name):
	tag = 'happy'
else:
	tag = 'physical'

#infile2 = open("C:\Users\wearable\IT.txt", "r")
#oxy = []
oxy_1 = []
hea =[]
sk = []
time =[]
x = []
test1 = convert_csv(infile, tag)
#oxy = test1.verne()
x = test1.generate()
hea = test1.heart()
sk = test1.skin()
time = test1.time()
oxy_1 = test1.filter(sk, q=590.0, r=50000.0, p=399900.0, k=0.0)
oxy_2 = test1.filter(hea, q=0.99, r=260.0, p=1000.0, k=0.0)
# test2 = compare(oxy, oxy_1, 14)
# test2.xavier()
# test2.clear()
plt.figure(1)
plt.subplot(211)
plt.plot(sk, 'r')
plt.plot(oxy_1, 'b')

plt.subplot(212)
plt.plot(hea, 'r')
plt.plot(oxy_2, 'b')

plt.show()
