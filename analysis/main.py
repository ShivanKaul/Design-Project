# import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import glob

from converter import Converter
from base import *
from compare import *
from learn import learn
from learn import learn_with_test


def get_tag(infile, binary=True):
    # Assign tags: multiclass or binary
    if binary:
        if 'physical+tenderness' in os.path.basename(infile.name):
            tag = 'physcal+tenderness'
        elif 'physical+happy' in os.path.basename(infile.name):
            tag = 'physical+happy'
        elif 'physical+fear' in os.path.basename(infile.name):
            tag = 'physical+fear'
        elif 'physical' in os.path.basename(infile.name):
            tag = 'physical'
        else:
            tag = 'emotion'
    else:
        if 'fear' in os.path.basename(infile.name):
            tag = 'fear'
        if 'disgust' in os.path.basename(infile.name):
            tag = 'disgust'
        elif 'happy' in os.path.basename(infile.name):
            tag = 'happy'
        elif 'sadness' in os.path.basename(infile.name):
            tag = 'sadness'
        elif 'tenderness' in os.path.basename(infile.name):
            tag = 'tenderness'
        elif 'anger' in os.path.basename(infile.name):
            tag = 'anger'
        elif 'physical+tenderness' in os.path.basename(infile.name):
            tag = 'physcal+tenderness'
        elif 'physical+happy' in os.path.basename(infile.name):
            tag = 'physical+happy'
        elif 'physical+fear' in os.path.basename(infile.name):
            tag = 'physical+fear'
        else:
            tag = 'physical'
    return tag


# Print to file
def printToFile(filename, data):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def plot(skin, filtered_skin, heart, filtered_heart):
    plt.figure(1)
    plt.subplot(211)
    plt.plot(skin, 'r')
    plt.plot(filtered_skin, 'b')
    plt.subplot(212)
    plt.plot(heart, 'r')
    plt.plot(filtered_heart, 'b')
    plt.show()


def main(matcher, combined=False):
    listOfTuples = []
    for file in glob.glob(matcher):
        if not combined:
            if "physical+" in file:
                continue
    # for file in glob.glob("happy_Trevor.csv"):
        if file == "listOfTuples.csv" or file == "output.csv":
            continue
        infile = open(file, "r")
        print file

        tag = get_tag(infile, binary=False)

        # Convert
        converter = Converter(infile, tag)
        # Build up list
        listOfTuples = listOfTuples + converter.generate()
    return listOfTuples

    # printToFile("listOfTuples.csv", listOfTuples)

# test = main("test/physical_pushups2.csv")
learn(main("ProComp_CSV/*.csv"))
# learn_with_test(main("ProComp_CSV/*.csv"), test)

    # Plot
    # plot(converter.skin, converter.filtered_skin, converter.heart, converter.filtered_heart)
