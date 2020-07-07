# genome_liftover
Script for performing liftover between different genome builds

## Example for running code from commandline:
python genome_liftover.py --infile {INFILE_PATH} --outfile {OUTFILE_PATH}  --idxCHR 1 --idxBP 2 --liftover {PATH_TO_LIFTOVER_CHAIN_FILE} \

When assigning column indexes (idxCHR/idxBP) zero-indexing is used. Meaning that first columns of your datafile is column 0.


## Liftover chain files can be found here for build hg38:
https://hgdownload.cse.ucsc.edu/goldenPath/hg38/liftOver/
