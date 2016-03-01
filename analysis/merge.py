import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import csv
import os 
import glob
import sys

from converter import *
from convertom import *
from write_to_file import *
from value import *

for files in glob.glob("*.csv"):
	# if files == e or d:
	# 	continue
	infile = open(files, "r")
	print files
	
	# Assign tags
	if 'fear' in os.path.basename(infile.name):
		tag = 'fear'
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

	a = os.path.basename(infile.name)

	omf = 'OM_' + os.path.splitext(a)[0] + '.txt'
	call_filter(omf)

	infileOM = open(os.path.join(os.path.expanduser('~'),'Documents/Design-Project/analysis/OM','OM_' + a), "r")
	cnvom = Convertom(infileOM)
	x = cnvom.generate()

	heartom = cnvom.heart
	breath = cnvom.breath
	timeom = cnvom.time

	converter = Converter(infile, tag)
	y = converter.generate()
	heart = converter.filtered_heart
	skin = converter.filtered_skin 
	time = converter.time

	heartsync = intervalues(time, heart, timeom)
	skinsync = intervalues(time, skin, timeom)
	merged = zip(timeom, heartsync, heartom, breath, skinsync, [tag]*len(heartsync))

	b = os.path.basename(infile.name)
	c = os.path.splitext(b)[0] + '_merged'

	with open(os.path.join(os.path.expanduser('~'),'Documents/Design-Project/analysis/Merged',c + '.csv'), "w") as f:
		writer = csv.writer(f)
		writer.writerows(merged)

	