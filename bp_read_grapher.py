#!/usr/local/bin/python2.7

import sys
import os
import subprocess
import re


def bp_parser(fn):
#input: bp file
#output: refrence read length. and a dictionary
#dictionary key = read, values = query start, query end, subject start, subject end


        infile = open(fn,'r')
        #read in first line of bp
        headerline = infile.readline()
        reads_dict=dict()
      
        #determine length of refrence assmebly
        reflen =  int(headerline.split("len=")[1])
	reads_dict=dict()
	for line in infile:
		if line.startswith("SUB"):
			readname = line.split()[0].split(':')[1]
			readlen = int(line.split("len=")[1])
		if line.startswith("qb"):
			qb = line.split()[0].split(":")[1]
			qe = line.split()[1].split(":")[1]
			sb = line.split()[2].split(":")[1]
			se = line.split()[3].split(":")[1]
			reads_dict[readname]=[readlen, qb, qe, sb, se]
	return (reflen, reads_dict)
	infile.close()


def bp_read_grapher(fn):
#input: bp file
#output: graph for read count in .ann format.

        infile = open(fn,'r')
	headerline = infile.readline()
        #read in first line of bp
        counts_dict=dict()
        #determine length of refrence assmebly
	reflen, reads_dict = bp_parser(fn)
       	print reflen
        print 'graph read_counts addPoints('
        for i in range(1, reflen+1):
                icount=0
       		for key, value in reads_dict.iteritems():
		
			if i >=int(value[1]) and i <= int(value[2]):
                        	icount += 1
               
                if i == int(reflen):
                        print '%d : %d )'%(i, icount)
                else:
                        print '%d : %d ,'%(i, icount)	

bp_read_grapher(sys.argv[1])
