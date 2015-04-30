#!/usr/local/bin/python2.7
##input filename (.m8 blast file)  and reference ( micro, mega, final) 

import sys
import os
import subprocess
import re
filename=sys.argv[1]
#ref = sys.argv[2]
infile = open(filename, 'r')
seqfile =open('seqfile.csv','r')
#gene = os.path.basename(os.getcwd())
#seq = subprocess.check_output(['tail', '-1', gene+'_'+ref+'.fa'])


gene="novel_bat_gammaherpesvirus"
seq=seqfile.readlines()[0]


frags =dict() 
for line in infile:
    line = line.split()
    orf = line[0]
    assem = line[1]
  
    queryStart = line[6] 
    queryEnd = line[7]
    #print'track %s addPairs( %d:%d )'%(assem, int(coords[0]), int(coords[1])) 
    if frags[orf] in frags:
	frags[orf] = frags[orf].append([queryStart, queryEnd])
    else:
	frags[orf] = [queryStart, queryEnd]
    #print frags

print "begin genome %s"%gene

print'track %s addPairs('%"ORFS"
for key,value in frags.iteritems():
	i=0
        #print'track %s addPairs( %d:%d )'%(key, int(value[0]), int(value[1]))
	#while i < len(value):
	#	print'%d:'%int(value[i]) 
	if "ORF" in key:
		print'%d : %d : link("%s", "www.google.com"),'%(int(value[0]), int(value[1]),key)
print ')'

print'track %s addPairs('%"Named Genes"
for key,value in frags.iteritems():
        #print'track %s addPairs( %d:%d )'%(key, int(value[0]), int(value[1]))

        if "ORF" not in key:
                print'%d : %d : link("%s", "www.google.com"),'%(int(value[0]), int(value[1]),key)
print ')'
print 'sequence %s addSeq(%s)'%(gene,seq.strip())
print 'end genome'
print 'showGenome(%s)'%gene

seqfile.close()
infile.close()
