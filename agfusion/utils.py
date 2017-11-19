# all combinations except those that do not produce some sort of
# chimeric protein are commented out

import itertools
import os

agfusion_db = os.path.join(
    os.path.split(__file__)[0],
    'data',
    'agfusion.db'
)

AGFUSION_DB_URL = "https://github.com/murphycj/AGFusionDB/raw/master/agfusion."

# this is mostly contigent on the maximum ensembl release supported
# by pyensembl

GENOME_SHORTCUTS = {
    'GRCm38':['mus_musculus',87],
    'mm10':['mus_musculus',87],
    'mm9':['mus_musculus',67],
    'GRCh38':['homo_sapiens',87],
    'hg38':['homo_sapiens',87],
    'hg19':['homo_sapiens',75]
}

MAX_ENSEMBL_RELEASE = 87

AVAILABLE_ENSEMBL_SPECIES = {
    'homo_sapiens':range(75,MAX_ENSEMBL_RELEASE+1),
    'mus_musculus':range(67,MAX_ENSEMBL_RELEASE+1)
}

ENSEMBL_MYSQL_TABLES = {
    'homo_sapiens':{},
    'mus_musculus':{}
}
for i in range(75,MAX_ENSEMBL_RELEASE+1):
    if i < 76:
        ENSEMBL_MYSQL_TABLES['homo_sapiens'][i] = 'homo_sapiens_core_' + str(i) + '_37'
    else:
        ENSEMBL_MYSQL_TABLES['homo_sapiens'][i] = 'homo_sapiens_core_' + str(i) + '_38'

for i in range(67,MAX_ENSEMBL_RELEASE+1):
    if i < 68:
        ENSEMBL_MYSQL_TABLES['mus_musculus'][i] = 'mus_musculus_core_' + str(i) + '_37'
    else:
        ENSEMBL_MYSQL_TABLES['mus_musculus'][i] = 'mus_musculus_core_' + str(i) + '_38'

# min amino acid length of domain to plot it

MIN_DOMAIN_LENGTH = 5

# just

STANDARD_CHROMOSOMES = [str(i) for i in range(1,23)] + ['X','Y','MT']

# the available protein domain annotations

PROTEIN_ANNOTATIONS = [
    'pfam', 'smart', 'superfamily', 'tigrfam', 'pfscan',
    'tmhmm', 'seg', 'ncoils', 'prints',
    'pirsf', 'signalp'
]

JUNCTION_LOCATIONS = [
    'CDS','CDS (start)','CDS (end)','5UTR','5UTR (end)',
    '3UTR','3UTR (start)','exon','intron','intron (cds)',
    'intron (before cds)','intron (after cds)'
    ]

CODING_COMBINATIONS = list(itertools.product(JUNCTION_LOCATIONS,JUNCTION_LOCATIONS))
CODING_COMBINATIONS = {i:{'protein_coding_potential':False,'truncated':False} for i in CODING_COMBINATIONS}


CODING_COMBINATIONS['CDS','CDS'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS','CDS (start)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS','CDS (end)'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['CDS','5UTR'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['CDS','5UTR (end)'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['CDS','3UTR'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['CDS','3UTR (start)'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['CDS','intron'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['CDS','intron (cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS','intron (before cds)'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['CDS','intron (after cds)'] = {'protein_coding_potential':True,'truncated':True}

CODING_COMBINATIONS['CDS (end)','CDS'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (end)','CDS (start)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (end)','CDS (end)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (end)','5UTR'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (end)','5UTR (end)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (end)','3UTR'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (end)','3UTR (start)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (end)','intron'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (end)','intron (cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (end)','intron (before cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (end)','intron (after cds)'] = {'protein_coding_potential':True,'truncated':False}

#CODING_COMBINATIONS['CDS (start)','CDS'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (start)','CDS (start)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['CDS (start)','CDS (end)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['CDS (start)','5UTR'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['CDS (start)','5UTR (end)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['CDS (start)','3UTR'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['CDS (start)','3UTR (start)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (start)','intron'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['CDS (start)','intron (cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['CDS (start)','intron (before cds)'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['CDS (start)','intron (after cds)'] = {'protein_coding_potential':True,'truncated':True}

#CODING_COMBINATIONS['5UTR','CDS'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['5UTR','CDS (start)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR','CDS (end)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR','5UTR'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR','5UTR (end)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR','3UTR'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR','3UTR (start)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR','intron'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR','intron (cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['5UTR','intron (before cds)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR','intron (after cds)'] = {'protein_coding_potential':True,'truncated':False}

#CODING_COMBINATIONS['5UTR (end)','CDS'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['5UTR (end)','CDS (start)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR (end)','CDS (end)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR (end)','5UTR'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR (end)','5UTR (end)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR (end)','3UTR'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR (end)','3UTR (start)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR (end)','intron (cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['5UTR (end)','intron (before cds)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['5UTR (end)','intron (after cds)'] = {'protein_coding_potential':True,'truncated':False}

CODING_COMBINATIONS['3UTR','CDS'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR','CDS (start)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR','CDS (end)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR','5UTR'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR','5UTR (end)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR','3UTR'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR','3UTR (start)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR','intron'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR','intron (cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR','intron (before cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR','intron (after cds)'] = {'protein_coding_potential':True,'truncated':False}

CODING_COMBINATIONS['3UTR (start)','CDS'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR (start)','CDS (start)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR (start)','CDS (end)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR (start)','5UTR'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR (start)','5UTR (end)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR (start)','3UTR'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR (start)','3UTR (start)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR (start)','intron'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR (start)','intron (cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR (start)','intron (after cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR (start)','intron (before cds)'] = {'protein_coding_potential':True,'truncated':False}

#CODING_COMBINATIONS['3UTR (end)','CDS'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['3UTR (end)','CDS (start)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['3UTR (end)','CDS (end)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['3UTR (end)','5UTR'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['3UTR (end)','5UTR (end)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['3UTR (end)','3UTR'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['3UTR (end)','3UTR (start)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['3UTR (end)','intron'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['3UTR (end)','intron (cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['3UTR (end)','intron (before cds)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['3UTR (end)','intron (after cds)'] = {'protein_coding_potential':True,'truncated':False}

#CODING_COMBINATIONS['intron','CDS'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron','CDS (start)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron','CDS (end)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron','5UTR'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron','5UTR (end)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron','3UTR'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron','3UTR (start)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron','intron'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron','intron (cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron','intron (before cds)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron','intron (after cds)'] = {'protein_coding_potential':{'protein_coding_potential':True,'truncated':False},'truncated':False}

CODING_COMBINATIONS['intron (cds)','CDS'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (cds)','CDS (start)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (cds)','CDS (end)'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['intron (cds)','5UTR'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['intron (cds)','5UTR (end)'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['intron (cds)','3UTR'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['intron (cds)','3UTR (start)'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['intron (cds)','intron'] = {'protein_coding_potential':True,'truncated':True}
CODING_COMBINATIONS['intron (cds)','intron (cds)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron (cds)','intron (before cds)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron (cds)','intron (after cds)'] = {'protein_coding_potential':True,'truncated':False}

#CODING_COMBINATIONS['intron (before cds)','CDS'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (before cds)','CDS (start)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron (before cds)','CDS (end)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (before cds)','5UTR'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (before cds)','5UTR (end)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron (before cds)','3UTR'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron (before cds)','3UTR (start)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron (before cds)','intron'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron (before cds)','intron (cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (before cds)','intron (before cds)'] = {'protein_coding_potential':True,'truncated':False}
#CODING_COMBINATIONS['intron (before cds)','intron (after cds)'] = {'protein_coding_potential':True,'truncated':False}

CODING_COMBINATIONS['intron (after cds)','CDS'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (after cds)','CDS (start)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (after cds)','CDS (end)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (after cds)','5UTR'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (after cds)','5UTR (end)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (after cds)','3UTR'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (after cds)','3UTR (start)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (after cds)','intron'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (after cds)','intron (cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (after cds)','intron (before cds)'] = {'protein_coding_potential':True,'truncated':False}
CODING_COMBINATIONS['intron (after cds)','intron (after cds)'] = {'protein_coding_potential':True,'truncated':False}
