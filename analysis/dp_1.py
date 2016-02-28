import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from base import *
from compare import *

infile = open("C:\Users\wearable\Trevor.txt", "r")
#infile2 = open("C:\Users\wearable\IT.txt", "r")
oxy = []
oxy_1 = []
test1 = base(infile)
test1.clear()
oxy = test1.start()
oxy_1 = test1.filter(0.15, 150.0, 1000.0, 0.0)
test2 = compare(oxy, oxy_1, 14)
test2.xavier()
test2.clear()

plt.plot(oxy, 'r')
plt.plot(oxy_1, 'b')
plt.show()
