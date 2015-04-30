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
		###for assemblies
		#assrd= open('rdgraphs/%s.rd'%k, 'r')
		assrd = open('ehv2_full.rd','r')
				
		i=0
		header = assrd.readline()
		#print '%s %s_%s %s'%(header.split()[0],k,header.split()[1], header.split()[2])
		
		print '%s %s %s'%(header.split()[0],header.split()[1], header.split()[2])
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
	#seq = subprocess.check_output(['tail', '-1', 'ORFS/%s.fa'%orf])
	
	seq = subprocess.check_output(['tail', '-1', 'fake_contigs/%s.fa'%orf])
	###for full genome	
	#seq = subprocess.check_output(['tail', '-1', 'ehv2_genome_new.fa'])
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
	print '#insertFile ../../../bat/ehv2/CDS/%s_bplink.html'%gene


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


def even_odd_graph(orfdict):
	#graphs even and odd contigs
	contdict=orfdict
	print 'track real_contigsA addPairs('
	
        for i in range (0, len(result.keys()),2):
                gene = 'real_contig_%d'%(i+1)
		if i==len(result.keys())-1:	
                	print '%d : %d: link("%s", "lwgv.cgi?ann=ehv2/real_contigs/%s.ann")\n)'%(int(result[gene].values()[0][2]), int(result[gene].values()[0][3]), gene, gene)
		else:
	                print '%d : %d: link("%s", "lwgv.cgi?ann=ehv2/real_contigs/%s.ann"),'%(int(result[gene].values()[0][2]), int(result[gene].values()[0][3]), gene, gene)
	print 'track real_contigsB addPairs('
        for i in range (1, len(result.keys()),2):
                gene = 'real_contig_%d'%(i+1)
		if i==len(result.keys())-2:	
                	print '%d : %d: link("%s", "lwgv.cgi?ann=ehv2/real_contigs/%s.ann")\n)'%(int(result[gene].values()[0][2]), int(result[gene].values()[0][3]), gene, gene)
		else:
	                print '%d : %d: link("%s", "lwgv.cgi?ann=ehv2/real_contigs/%s.ann"),'%(int(result[gene].values()[0][2]), int(result[gene].values()[0][3]), gene, gene)
		
if __name__ == "__main__":
	##arg1 is blast.m8 file	
	fn =  sys.argv[1]
	result = get_coords_bp(fn)
	#graph_all_ass(fn)
	#print result
	#cut_ann_parts("gene_11", result)
	##arg2 is ORF name
	#ann_maker("%s"%sys.argv[2], result)
	even_odd_graph(result)
		#htmlfile=open('fake_contigs/%s_bplink.html'%gene,'w')
		#htmlfile.write('<br><h3><a href="http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/ehv2/fake_contigs/1.%s.fa&bp=out/ehv2/fake_contigs/1.%s.mvi.bp&mid=101&flank=100">Pileup</a></h3>'%(gene,gene)) 
		#htmlfile.close()
        	#saveout=sys.stdout
        	#outfile = open('fake_contigs/%s.ann'%gene,'w')
        	#sys.stdout=outfile
        	#ann_maker(gene, result)
        	#sys.stdout=saveout
        	#outfile.close()
