import csv
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from practice_dugga_func import orderChromosomes

#task 2.1
parser = argparse.ArgumentParser()
parser.add_argument('--filename', help = 'Specify a csv file')

args=parser.parse_args()

df = pd.read_csv(args.filename)

#task 2.2
chr_orderd = orderChromosomes()

#task 2.3
plt.scatter(df['chromosome'], df['cnv_log2'], xunits=chr_orderd)
plt.xlabel('Chromosome')
plt.ylabel('CNV value (log2)')
plt.title('CNV value vs chromosome')
plt.savefig('CNV_overview.png',dpi =300)