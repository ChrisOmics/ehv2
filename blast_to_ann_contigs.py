#!/usr/local/bin/python2.7
##input filename (.m8 blast file)  and reference ( micro, mega, final) 

import sys
import os
import subprocess
import re
filename=sys.argv[1]
#ref = sys.argv[2]
infile = open(filename, 'r')
seqfile =open('ehv_seqs.fa','r')
#gene = os.path.basename(os.getcwd())
#seq = subprocess.check_output(['tail', '-1', gene+'_'+ref+'.fa'])


gene="novel_bat_gammaherpesvirus"
seq=seqfile.readlines()[0]


frags =dict() 
for line in infile:
    line = line.split()
    orf = line[0]
    #assem = line[1]
    #orf = line[1]
    #queryStart = line[6] 
    #queryEnd = line[7]
    queryStart = line[8] 
    queryEnd = line[9]
    #print'track %s addPairs( %d:%d )'%(assem, int(coords[0]), int(coords[1])) 
    if orf not in frags.keys():
	
	frags[orf] = [queryStart, queryEnd]
	listt=[]
    else:

	listt=[]


	listt = frags[orf]

	listt.append(queryStart)
	listt.append(queryEnd)
	
	frags[orf] = listt
    

print "begin genome %s"%gene


for key,value in frags.iteritems():
	i=0
	
        print'track %s addPairs( '%(key)
	while i < len(value)-2:
		print'%d:%d,'%(int(value[i]), int(value[i+1]))
		i+=2
	if i==len(value)-2:
		
		print '%d:%d )\n'%(int(value[i]), int(value[i+1]))






		


print 'sequence %s addSeq(%s)'%(gene,seq.strip())
print 'end genome'
print 'showGenome(%s)'%gene

seqfile.close()
infile.close()
