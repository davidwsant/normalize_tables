from argparse import ArgumentParser
import glob
import sys
from os.path import splitext
import pandas as pd
from sklearn.preprocessing import scale

args = ArgumentParser('python scale_tables.py', description="""Welcome to scale_tables.py. This program has been designed to scale rows of data.
				The input must be in a comma delimited (csv) format. The header line must contain the names of
				the columns (usually sample names). The first column must contain the names for each row
				(often Ensembl ID or gene names for genomic data). The output file will contain scaled data. 
				Example usage: python scale_tables.py --input_csv RCPM_table.csv --output_file Scaled_RCPM_table.csv""")

args.add_argument(
	'--input_csv',
	help="""\
This is the RCPM file. It must have a header row with the column names.
The first column should be the name you want for each row in the output file (often the Ensembl ID or gene name for genomic data).
This file must be in csv format. """,
	default=None
)

args.add_argument(
	'--output_file',
	help="""This is the name that you want for the output file. If you do not specify an output file name with this
	option, the name of the input file with "SCALED" added on the end will be used.""",
	default = None
)


args = args.parse_args()
# If no input was added for the input_csv, print a help message, list csv files currently in the directory and exit
if args.input_csv == None:
	list_of_csv_files = glob.glob('*.csv')
	print()
	print("""		Welcome to scale_tables.py. This program has been designed to scale rows of data.
		The input must be in a comma delimited (csv) format. The header line must contain the names of
		the columns (usually sample names). The first column must contain the names for each row
		(often Ensembl ID or gene names for genomic data). """)
	print("		You have not specificed an input file with the --input_csv option. Possible files in your directory include: ")
	print(list_of_csv_files)
	print("		Example usage: python scale_tables.py --input_csv RCPM_table.csv --output_file Scaled_RCPM_table.csv")
	print()
	sys.exit(0)

input_file = args.input_csv

# If they did not list an output file, use the input file name, but add "SCALED" to the end
output_file = args.output_file
if output_file == None:
	output_file = splitext(input_file)[0]+"_SCALED.csv"

input_data = pd.read_csv(input_file, index_col=0)
scaled = pd.DataFrame(scale(input_data))
scaled.columns = input_data.columns
scaled['names'] = input_data.index
scaled = scaled.set_index('names')
scaled.to_csv(output_file)
