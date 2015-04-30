#!/usr/local/bin/python2.7
import sys
import os
import subprocess
import csv

filename = sys.argv[1]
reader = csv.reader(open(filename))

outfile=open('ORF_pileups.csv','w')

for row in reader:
#    assem = row[0].split()[0]
    #assem = assem[1:]
    gene = row[0]
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
    os.system('blast4.sh ORFS/%s.fa bp/%s' %(gene,gene))
    #os.system('blast4.sh '+ gene+'_micro.fa micro')
    #os.system('blast4.sh '+ gene+'_bat.fa bat')
    #os.chdir('..')
    #outfile.write("%s,http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/%s/1.%s.fa&bp=out/%s/1.%s.b3.bp&mid=200&flank=200,http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/%s/1.%s.fa&bp=out/%s/1.%s.b3.bp&mid=200&flank=200,http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/%s/1.%sREV.fa&bp=out/%s/1.%sREV.b3.bp&mid=200&flank=200,http://etna.mssm.edu/chris/web/cgi-bin/lwgv-0.4/examples/lwgv.cgi?ann=../../../bat/all_genes/class2/%s/%s_micro.ann\n"%(gene,gene, micro[0], gene, micro[0], gene,assem,gene,assem,gene,assem,gene,assem,gene,gene))

