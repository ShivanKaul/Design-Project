import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import csv

from frankenstein import *
from base import *
from compare import *

infile = open("C:\Users\wearable\Documents\emily.csv", "r")
#infile2 = open("C:\Users\wearable\IT.txt", "r")
#oxy = []
oxy_1 = []
hea =[]
sk = []
time =[]
test1 = frankenstein(infile)
#oxy = test1.verne()
test1.verne()
hea = test1.heart()
sk = test1.skin()
time = test1.time()
oxy_1 = test1.filter(sk, q=590.0, r=599900.0, p=399900.0, k=0.0)
oxy_2 = test1.filter(hea, q=0.35, r=159.0, p=1000.0, k=0.0)
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
