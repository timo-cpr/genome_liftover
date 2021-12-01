# genome_liftover
Script for performing liftover between different genome builds of GWAS summary data.  
It is required to load a python module before running the script.  
eg. module load anaconda3/4.4.0

## Example for running code from command line:
python genome_liftover.py --infile {INFILE_PATH} --outfile {OUTFILE_PATH} --idxCHR {INDEX_OF_CHR_COLUMN} --idxBP {INDEX_OF_BP_COLUMN} --liftover {PATH_TO_LIFTOVER_CHAIN_FILE}           
    
example:    
python genome_liftover.py --infile mydata/nature_paper/gwas_summary.tsv --outfile /mydata/nature_paper/results.tsv --idxCHR 1 --idxBP 2 --liftover hg38ToHg19.over.chain.gz     


### Additional input arguments
--sep, help="File separator",default = "\t".        
--keep_old",help="If old coordinates should be kept. False: drop , True: keep, default = False, choices=[True, False].   

When assigning column indexes (--idxCHR/--idxBP) zero-indexing is used. Meaning that the first column of your data file is column 0.
### Required input arguments
--infile, help="Summary data file to perform liftover on",required=True.    
--outfile, help="Where to save the output file with liftover CHR, BP, and STRAND", required=True.   
--idxCHR, help="zero-index coloumn number of chromosome column",default = 1.    
--idxBP, help="zero-index coloumn number of basepair-position column",default = 2.     
--liftover, help="File with liftover chain", default = 'hg38ToHg19.over.chain.gz',required=True.      





## Liftover chain files can be found here for build hg38:
https://hgdownload.cse.ucsc.edu/goldenPath/hg38/liftOver/
