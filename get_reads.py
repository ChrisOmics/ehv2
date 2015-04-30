#!/usr/local/bin/python2.7
import sys
import os
import subprocess
import csv

##input: assembly, start, stop
#return: reads total

def get_reads(assem, start, stop):
	start = int(start)
	stop = int(stop)	
	os.system('get_bat_assmbls_edit.pl %s > tmpassem.fa'%assem)
	os.system('clean_fasta.sh tmpassem.fa')		
	os.system('get_part_seq.pl tmpassem.fa %d %d > tmpassempart.fa' %(start,stop))
	os.system('blast4wait.sh tmpassempart.fa tmp')
	counts = subprocess.check_output(['reads_counter.sh', 'tmp'])
	readcounts =  counts.split(' | ')
	return(readcounts)	
#res =get_reads("BatA2226.a3384", 1, 103)

if __name__ == "__main__":
	assem, start, stop = sys.argv[1:]
	result = get_reads(assem, start, stop)
	print result

