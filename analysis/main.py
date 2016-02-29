# import numpy as np
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
    plt.show()

# Start main script
for file in glob.glob("*.csv"):
    # for file in glob.glob("happy_kungfu2.csv"):
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
    # Build up list
    listOfTuples.append(converter.generate())

    # Plot
    # plot(converter.skin, converter.filtered_skin, converter.heart, converter.filtered_heart)

    # Print to file
with open("listOfTuples.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(listOfTuples)
