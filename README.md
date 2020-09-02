# genome_liftover
Script for performing liftover between different genome builds

## Example for running code from commandline:
python genome_liftover.py --infile {INFILE_PATH} --outfile {OUTFILE_PATH}  --idxCHR 1 --idxBP 2 --liftover {PATH_TO_LIFTOVER_CHAIN_FILE} \

### Additional input arguments
--sep, help="File separator",default = "\t".     
--idxCHR, help="zero-index coloumn number of chromosome column",default = 1.    
--idxBP, help="zero-index coloumn number of basepair-position column",default = 2.   
--keep_old",help="If old coordinates should be kept. False: drop , True: keep, default = False, choices=[True, False].   

When assigning column indexes (--idxCHR/--idxBP) zero-indexing is used. Meaning that the first column of your data file is column 0.
### Required input arguments
--liftover, help="File with liftover chain", default = 'hg38ToHg19.over.chain.gz',required=True.   
--infile", help="Summary data file perform liftOver on",required=True).   
--outfile", help="Where to save the output file with liftover CHR,BP and STRAND", required=True.   





## Liftover chain files can be found here for build hg38:
https://hgdownload.cse.ucsc.edu/goldenPath/hg38/liftOver/
