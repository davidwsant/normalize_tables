## Dave's Normalizing Tables Programs

Welcome to Z_score_tables.py and scale_tables.py. These programs have been designed
to scale rows of data (often RNA-seq data). The input must be in a comma delimited
(csv) format. The header line must contain the names of the columns (usually sample
names). The first column must contain the names for each row (often Ensembl ID or
gene names for genomic data). The output file will contain scaled data. For Z-scores
this means that each value will represent the Z-score for its given row.

Example usage:
```
python scale_tables.py --input_csv RCPM_table.csv --output_file Scaled_RCPM_table.csv
```

optional arguments:

  -h, --help            
                        show this help message and exit

  -i INPUT_CSV, --input_csv INPUT_CSV

                        This is the RCPM file. It must have a header row with
                        the column names. The first column should be the name
                        you want for each row in the output file (often the
                        Ensembl ID or gene name for genomic data). This file
                        must be in csv format.

  -o OUTPUT_FILE, --output_file OUTPUT_FILE

                        This is the name that you want for the output file. If
                        you do not specify an output file name with this
                        option, the name of the input file with "Z_score"
                        added on the end will be used.
