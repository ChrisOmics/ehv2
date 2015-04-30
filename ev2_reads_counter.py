#!/usr/local/bin/python2.7
import sys
import os
import subprocess
import csv
import re
#filename = sys.argv[1]
reader = open('orfs.assemblies.long', 'r')
coords = open('orf_coords_ehv2.csv','r')
readsdict=dict()
orfdict=dict()
#outfile=open('ORF_pileups.csv','w')
print "Content-type: text/html"
#write <table> tag
print
print('<html>')
print('<body>')

for line in reader:
#    assem = row[0].split()[0]
    #assem = assem[1:]
    line = line.split()
    gene = line[0]
    assem = line[1]
    #gene = gene.split()[1].split('.')[1]
    #gene = gene.upper()
    #subprocess.call(['mkdir',gene])
    #os.chdir(gene)
    #micro = row[1].split()
    #if micro[1].startswith('ENSM'):
    #    microgene = micro[1]
    #3else:
    #    microgene = micro[0]
    #os.system('get_bat_assmbls_edit.pl '+ assem+ ' > '+ gene+'_bat.fa')
    #os.system('get_fa_mega_or_micro.pl micro ' + microgene + ' > '+ gene +'_micro.fa')
    #os.system('microblast.sh '+ gene)
    #os.system('../blast_to_ann.py > %s_micro.ann' %gene)
    #os.system('sed "1s/.*/\>'+assem+'REV/" '+ gene+'_bat_rev.fa > tmp2')
    #os.system('mv tmp2 '+ gene+'_bat_rev.fa')
    #print'<table>'
    #print '<tr><td>%s</td><td>%s</td><td>'%(gene,assem)
    #cmd1='reads_counter.sh bat_bp/proccessed/%s.%s' %(gene,assem)
    p3=subprocess.check_output('/home/chris/bin/reads_counter.sh bat_bp/proccessed/%s.%s' %(gene,assem), shell = True) 
    reads=p3.split('|')
    #print reads[3]
    #print '</td></tr></table></body></html>'
    if gene in readsdict:
	readsdict[gene] = readsdict[gene] + int(reads[3])
    else:
	readsdict[gene] = int(reads[3])
print'graph myGraph addPoints('
for line2 in coords:
	orf = line2.split(',')[0]
	coords = re.findall(r'\d+',line2.split(',')[1])
	queryStart = int(coords[0])
        queryEnd = int(coords[1])
	middle = (queryStart + queryEnd)/2
	startco = line2
	if orf in readsdict:
		orfdict[orf]=[readsdict[orf],middle, queryStart,queryEnd]
		print' %d : %d ,' %(middle, readsdict[orf])
print ')'
print readsdict  
print orfdict
print len(readsdict)

    #os.system('blast4.sh '+ gene+'_micro.fa micro')
    #os.system('blast4.sh '+ gene+'_bat.fa bat')
    #os.chdir('..')
    #outfile.write("%s,http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/%s/1.%s.fa&bp=out/%s/1.%s.b3.bp&mid=200&flank=200,http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/%s/1.%s.fa&bp=out/%s/1.%s.b3.bp&mid=200&flank=200,http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/%s/1.%sREV.fa&bp=out/%s/1.%sREV.b3.bp&mid=200&flank=200,http://etna.mssm.edu/chris/web/cgi-bin/lwgv-0.4/examples/lwgv.cgi?ann=../../../bat/all_genes/class2/%s/%s_micro.ann\n"%(gene,gene, micro[0], gene, micro[0], gene,assem,gene,assem,gene,assem,gene,assem,gene,gene))

