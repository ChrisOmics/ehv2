#!/usr/bin/python

import os
import csv
import csv
import re
fn = open('gene_coordinates.csv', 'r')
fn2 = open('genenames.csv','r')
for line in fn:
	str= line.split(',')[0]
	if "Unassigned" in str or "unassigned" in str:
		orf = re.findall(r'\d+',str)
		orf= 'U%s'%orf[0]
		#print orf
	else:
		orf=re.findall(r'\d+',str)[0]
		#print orf
	finalline= line.split(',')[0]+','+line
	for line2 in fn2:
		str2=line2.split(',')[0]
		if "Unassigned" in str2 or "U" in str2:
			orf2 = re.findall(r'\d+',str2)
			orf2= 'U%s'%orf2[0]
	#		print orf2
		else:
			try:
				orf2=re.findall(r'\d+',str2)[0]
			
			except IndexError:
				orf2 = str2
		#print orf,orf2
		if orf==orf2:
			finalline= str2+','+ line
		else:
			continue
	print finalline.strip()
	fn2.seek(0)
