#!/usr/local/bin/python2.7
import sys
import os
import subprocess
import csv

#filename = sys.argv[1]
#reader = open(filename, 'r')

#outfile=open('ORF_pileups.csv','w')
i=1

while i < 40:
#for line in reader:
    #line = line.split(',')
#    assem = row[0].split()[0]
    #assem = assem[1:]
    #gene = line[0]
    #assem = line[1]
    #gene = gene.split()[1].split('.')[1]
    #gene = gene.upper()
    #subprocess.call(['mkdir',gene])
    #os.chdir(gene)
    #micro = row[1].split()
    #if micro[1].startswith('ENSM'):
    #    microgene = micro[1]
    #3else:
    #    microgene = micro[0]
    #os.system('get_bat_assmbls_edit.pl %s > batass/%s_%s.fa' %(assem, gene, assem))
    #os.system('get_fa_mega_or_micro.pl micro ' + microgene + ' > '+ gene +'_micro.fa')
    #os.system('microblast.sh '+ gene)
    #os.system('../blast_to_ann.py > %s_micro.ann' %gene)
    #os.system('sed "1s/.*/\>'+assem+'REV/" '+ gene+'_bat_rev.fa > tmp2')
    #os.system('mv tmp2 '+ gene+'_bat_rev.fa')
    #if "gene_9" in gene:
	gene = 'real_contig_%d'%i
#    	os.system('blastn -query real_contigs/%s.fa -dust no -evalue 1e-3 -num_descriptions 200000 -num_alignments 200000 -db reed/MVI_IT_cell.fa | useParse_p.pl > real_contigs/bps/%s.mvi.bp &' %(gene, gene))
	i+=1
        os.system('perl /home/chris/Util/website/dna_mth/bp_invrt.pl real_contigs/bps/%s.mvi.bp real_contigs/%s.fa /home/chris/Util/website/dna_mth/out/ehv2/real_contigs 1'%(gene,gene))
    #os.system('blast4.sh '+ gene+'_micro.fa micro')
    #os.system('blast4.sh '+ gene+'_bat.fa bat')
    #os.chdir('..')
    #outfile.write("%s,http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/%s/1.%s.fa&bp=out/%s/1.%s.b3.bp&mid=200&flank=200,http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/%s/1.%s.fa&bp=out/%s/1.%s.b3.bp&mid=200&flank=200,http://etna.mssm.edu/chris/web/dna_mth/pile_up_view.pl?fa=out/%s/1.%sREV.fa&bp=out/%s/1.%sREV.b3.bp&mid=200&flank=200,http://etna.mssm.edu/chris/web/cgi-bin/lwgv-0.4/examples/lwgv.cgi?ann=../../../bat/all_genes/class2/%s/%s_micro.ann\n"%(gene,gene, micro[0], gene, micro[0], gene,assem,gene,assem,gene,assem,gene,assem,gene,gene))

