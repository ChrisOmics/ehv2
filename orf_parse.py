#!/usr/local/bin/python2.7
##input coordinates file. with colmn 1 name, col2 coords 

import sys
import os
import subprocess
import re
filename=sys.argv[1]
#ref = sys.argv[2]
infile = open(filename, 'r')
#seqfile =open('','r')
#gene = os.path.basename(os.getcwd())
#seq = subprocess.check_output(['tail', '-1', gene+'_'+ref+'.fa'])

seqfile="ehv2_genome_new.fa"
gene="novel_bat_gammaherpesvirus"
#seq=seqfile.readlines()[0]
print "begin genome %s"%gene

frags = {}
for line in infile:
    line = line.split(',')
    #final = line[0]
    assem = line[0]
  
    coords = re.findall(r'\d+',line[1])
   
    queryStart = coords[0] 
    queryEnd = coords[1]
    #print'track %s addPairs( %d:%d )'%(assem, int(coords[0]), int(coords[1])) 
    frags[assem] = [queryStart, queryEnd]
    #print frags

##for multiple on one track
print 'track Genes addPairs('

i=1
#print frags.values()[0][0], frags.keys()
for key,value in frags.iteritems():
	qb=int(value[0])
	qe=int(value[1])
	overlap = 0
	for k, v in frags.iteritems():
		if qb > int(v[0]) and qb < int(v[1]):
			overlap =1	
			i+=1
			print key, k
		elif qe >int(v[0]) and qe < int(v[1]):
			overlap = 1
			i+=1
			print key, k
		else:
			continue
	#if overlap == 0:
	#	print'%d : %d : link("%s","lwgv.cgi?ann=../../../bat/ehv2/genes/%s.ann"), '%(int(value[0]), int(value[1]),key,key)

	#if overlap ==1 :
	#	print')\ntrack Genes_%d addPairs(%d : %d : link("%s","lwgv.cgi?ann=../../../bat/ehv2/genes/%s.ann"))\ntrack Genes addPairs('%(i,int(value[0]), int(value[1]),key,key)
			
	print'%d : %d : link("%s","lwgv.cgi?ann=ehv2/genes/%s.ann"), '%(int(value[0]), int(value[1]),key,key)
	###for all on sepearte tracks
        #print'track %s addPairs( %d:%d )'%(key, int(value[0]), int(value[1]))
	##to make the fasta folders w seqs
	#os.system('echo ">%s" > CDS/%s.fa'%(key,key))
	#os.system('./get_part_seq.pl %s %d %d |tail -1  >> CDS/%s.fa '%(seqfile, int(value[0]), int(value[1]), key))
	

print ')'
#print 'sequence %s addSeq(%s)' %(gene,seq.strip())
print 'end genome'
print 'showGenome(%s)'%gene

#seqfile.close()
infile.close()
