#!/usr/local/bin/python2.7
import sys
import os
import subprocess
import csv


##input: assembly, start, stop
#return: reads total

def get_coords_bp(fn):
	##input blast.m8 file and get back nested dictionary with the coordinates of each ORF and each assembly with qb,qe,sb,se
	##input: blast.m8
	##output: dictionary of coords
	infile = open(fn,'r')
	orf_dict= dict()
	assem_dict=dict()
	oldorf=()
	#orf_dict['ORF7']=""
	for line in infile:
		line = line.split()
		ORF = line[0]
		assem=str(line[1])
		qstart=line[6]
		qstop=line[7]
		astart=line[8]
		astop=line[9]

		
		if ORF not in orf_dict.keys():
			
		
			assem_dict = {}
	
			if assem not in assem_dict.keys():

				assem_dict[assem] = [qstart, qstop, astart,astop]
				#listt=[]	

				#listt.append(qstart)
				#listt.append(qstop)
				#listt.append(astart)
				#listt.append(astop)
				#assem_dict[assem]=listt
			else:

				listt =[]
				listt = assem_dict[assem]	
				listt.append(qstart)
                                listt.append(qstop)
                         
			        listt.append(astart)
                                listt.append(astop)
				assem_dict[assem]=listt

			orf_dict[ORF] = assem_dict


			
		else:


			if assem not in assem_dict.keys():
				assem_dict[assem] = [qstart, qstop, astart,astop]
				listt=[]	
				listt.append(qstart)
				listt.append(qstop)

				listt.append(astart)
				listt.append(astop)
				assem_dict[assem]=listt
			else:
				listt =[]
				listt = assem_dict[assem]	
			
				listt.append(qstart)
				listt.append(qstop)

				listt.append(astart)
                                listt.append(astop)
                                assem_dict[assem]=listt
			listt2 = assem_dict 

			orf_dict[ORF] = listt2
		
	return orf_dict
	

def cut_ann_parts(orf, orfdict):
	coords = orfdict
	
	###print'graph all_reads addPoints('
	for k, v in coords[orf].iteritems():
		#os.system('bp_read_grapher.py bat_bp/proccessed/%s.%s.b3.bp > rdgraphs/%s.rd'%(orf,k,k))
		#counter to get all of the groups of start stop coords, query and subject
		
		assrd= open('rdgraphs/%s.rd'%k, 'r')
		i=0
		header = assrd.readline()
		print '%s %s_%s %s'%(header.split()[0],k,header.split()[1], header.split()[2])
		#get all coords for each part
		while i < len(v):
			qb= int(v[i])
			qe = int(v[i+1])
			sb = int(v[i+2])
			se = int(v[i+3])
			
			###start counter to translate the subject coordinate into query coordinate
			if qb < qe:
				j=qb
			elif qb>qe:
				j=qe
			for line in assrd:
						
				line = line.strip().split(' : ')
				if sb < se:		
					if int(line[0])>=sb and int(line[0])<se:
						#print j, line
						print "%s : %s" %(j, line[1])
						j+=1
					elif int(line[0])==se and i ==len(v)-4:
						print"%s : %s )\n"%(j, line[1].split(',')[0])
						
						j+=1
				elif se < sb:
					if int(line[0])>=se and int(line[0])<sb:
						#print j, line
						print "%s : %s" %(j, line[1])
						j+=1
					elif int(line[0])==sb and i == len(v)-4:
						
						print"%s : %s )\n"%(j, line[1].split(',')[0])
					
						j+=1
			assrd.seek(0)
			
			assrd.readline()	
			i+=4
		assrd.close()
	

def ann_maker(orf, orfdict):
	gene = orf
	seq = subprocess.check_output(['tail', '-1', 'ORFS/%s.fa'%orf])
	#full seq	
	##seq = subprocess.check_output(['tail', '-1', 'ehv2_genome_new.fa'])
	coords = orfdict
	#print coords[gene]
	print "begin genome %s"%gene
	for k,v in coords[gene].iteritems():
		print "track %s addPairs("%k
		i=0
		while i<(len(v)-4):
			#print v
			print '%s : %s,'%(v[i], v[i+1])
			
			i+=4
		if i == len(v)-4:
			print '%s : %s'%(v[i], v[i+1])
			print ")"
	#############must use bp_read_grapher to generate rd graph file
	cut_ann_parts(orf, coords)
	print 'sequence %s addSeq(%s)'%(gene, seq)
	print 'end genome'
	print 'showGenome(%s)'%gene


def graph_all_ass (fn):
	#input m8 blast file
	#output: read graphs for everyone
        
        result = get_coords_bp(fn)
	###to unpack all***

        for k, v in result.iteritems():
		#print k, v 
                for a in v.keys():
			#print k, a               	
        #graphs all 
			if not os.path.isfile("rdgraphs/%s.rd"%a):
				#print a
        			os.system('bp_read_grapher.py bat_bp/proccessed/%s.%s.b3.bp > rdgraphs/%s.rd'%(k,a,a))
	

fn =  sys.argv[1]
result = get_coords_bp(fn)
#graph_all_ass(fn)
#cut_ann_parts("ORF44", result)
##arg2 is ORF name

for i in result.keys():

	gene = i 
	#saveout=sys.stdout
	#outfile = open('ann/%s.ann'%gene,'w')
	#sys.stdout=outfile
	#ann_maker(gene, result)
	#sys.stdout=saveout
	#outfile.close()
	print '<a href="http://etna.mssm.edu/chris/web/cgi-bin/lwgv-0.4/examples/lwgv.cgi?ann=../../../bat/ehv2/ann/%s.ann">%s</a><br><br>'%(gene,gene)
