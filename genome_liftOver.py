'''
	Script which performs lifts over from different genome builds
	
	# Developed by: Peter Bruun-Rasmussen
	# Feel free to contact me for questions

	Build on top of these resources:
	https://github.com/konstantint/pyliftover
	https://pypi.org/project/pyliftover/
	http://fouryears.eu/2013/02/25/the-curse-of-genomic-coordinates/

	Example for running code:
	python genome_liftover.py --infile {INFILE_PATH} --outfile {OUTFILE_PATH}  --idxCHR 1 --idxBP 2 --liftover {PATH_TO_LIFTOVER_CHAIN_FILE}

'''

import pandas as pd
import numpy as np
import argparse
from pyliftover import LiftOver


## LIFTOVER FUNCTION ##

def _l(row,liftover):
	# If positions are not found, set to NaN
	_new_chromosome = "NaN" 
	_new_position = "NaN"
	_new_strand = "NaN"
	
	try:
		l_ = liftover.convert_coordinate(row["CHR_old"], int(row["BP_old"]))
		if l_:
			if len(l_) > 1:
				print("Liftover with more than one candidate: %s", t.variant_id)
			_new_chromosome = l_[0][0]
			_new_position = int(l_[0][1])
			_new_strand = l_[0][2]
	except:
		pass

	return pd.Series((_new_chromosome, _new_position, _new_strand))

## MAIN FUNCTION ##

def liftover():
	# Load GWAS results
	print("-- Loading file : "+args.infile+" -- ")
	data = pd.read_csv(args.infile,sep=args.sep,dtype=str)

	## Preprocess
	print("-- Formating file --")
	# Get coloumns names
	chr_name = data.columns[int(args.idxCHR)]
	BP_name = data.columns[int(args.idxBP)]
	# Rename columns
	data.rename({chr_name:"CHR_old",BP_name:"BP_old"},axis=1,inplace=True)

	# Put "chr" in front on CHR column
	#mask_chr = data["CHR_old"].str.contains("(?i)chr",regex=True)
	data.loc[~data["CHR_old"].str.contains("(?i)chr",regex=True),"CHR_old"] = data.loc[~data["CHR_old"].str.contains("(?i)chr",regex=True),"CHR_old"].apply(lambda x: "chr" + str(x)) 
	# Set all chr to lowercase
	data["CHR_old"] = data["CHR_old"].str.lower()
	# replace chr23 with chrX
	data["CHR_old"].replace("chr23","chrX",inplace=True)
	data["CHR_old"].replace("chrx","chrX",inplace=True)

	# Convert BP to integer
	data["BP_old"] = data["BP_old"].astype(int)

	# LiftOver
	print("-- liftOver running --")
	lo = LiftOver(args.liftover)
	data[["CHR","BP","STRAND"]] = data.apply(_l,liftover=lo,axis=1)
	print("-- liftOver Done --")

	# Convert BP to integer
	data["BP"] = data["BP"].astype(int)

	if not args.keep_old:
		# Drop old coordinates
		data.drop(["CHR_old","BP_old"],axis=1,inplace=True)

	# Save liftover'ed file
	print("-- Saving file to: " + str(args.outfile))
	data.to_csv(args.outfile,sep="\t",na_rep="NaN",index=False)

if __name__ == "__main__":

	parser = argparse.ArgumentParser("Liftover Basepair position between builds")
	parser.add_argument("--sep", help="File separator",default = "\t")
	parser.add_argument("--idxCHR", help="zero-index coloumn number of chr",default = 1)
	parser.add_argument("--idxBP", help="zero-index coloumn number of Basepair position",default = 2)
	parser.add_argument("--liftover", help="File with liftover chain", default = 'hg38ToHg19.over.chain.gz',required=True)
	parser.add_argument("--infile", help="Summary data file perform liftOver on",required=True)
	parser.add_argument("--outfile", help="Where to save the output file with liftover CHR,BP and STRAND", required=True)
	parser.add_argument("--keep_old",help="If old coordinates should be kept. False: drop , True: keep", default = False, choices=[True, False])
	args = parser.parse_args()

	# run script
	liftover()

