#!/usr/local/bin/python2.7
import sys
import os
import subprocess
import csv

filename = sys.argv[1]
reader = csv.reader(open(filename))

outfile=open('class1_pileups.csv','a')

for row in reader:
    assem = row[0].split()[0]
    assem = assem[1:]
    gene = row[0]
    gene = gene.split()[1].split('.')[1]
    gene = gene.upper()
    #subprocess.call(['mkdir',gene])
    os.chdir(gene)
    micro = row[1].split()
    if micro[1].startswith('ENSM'):
        microgene = micro[1]
    else:
        microgene = micro[0]
    #os.system('get_bat_assmbls_edit.pl '+ assem+ ' > '+ gene+'_bat.fa')
    #os.system('get_fa_mega_or_micro.pl micro ' + microgene + ' > '+ gene +'_micro.fa')
    #os.system('microblast.sh '+ gene)
    os.system('bpinv.sh micro '+ gene+'_micro.fa '+gene)
    os.system('bpinv.sh bat '+ gene+'_bat.fa '+gene)
    os.system('bpinv.sh rev '+ gene+'_bat_rev.fa '+gene)
    os.chdir('..')
    #outfile.write("%s,http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/%s/1.%s.fa&bp=out/%s/1.%s.b3.bp&mid=500&flank=500,"%(gene,gene, micro[0], gene, micro[0]))
    #outfile.write("http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/%s/1.%s.fa&bp=out/%s/1.%s.b3.bp&mid=500&flank=500,"%(gene, assem, gene, assem))
    #outfile.write("http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/%s/1.%sREV.fa&bp=out/%s/1.%sREV.b3.bp&mid=500&flank=500\n"%(gene, assem, gene, assem))
