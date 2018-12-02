

# pip install scikit-allel
import allel; 
import argparse
from argparse import RawTextHelpFormatter


parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,description=""" 
This script takes a vcf file as input and prints the sample names and the number of
heterozygous sites per sample in the standard output.""")
parser.add_argument('--vcf', required=True, dest='vcf', type=str, help="Input vcf file.")

args = parser.parse_args()


# check which version is installed
# print('scikit-allel', allel.__version__)
# print('allel', allel.__version__)


callset = allel.read_vcf(args.vcf)
gt = allel.GenotypeArray(callset['calldata/GT'])

print("\t".join(callset['samples']))
print("\t".join(map(str,gt.count_het(axis=0))))

# print(callset)
# print(sorted(callset.keys()))
# print(callset['calldata/GT'])
# print(gt)
# print(gt.is_het())
# print(gt.count_het(axis=0))


