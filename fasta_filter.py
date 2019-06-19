#!/usr/local/bin/env python3
import sys
import os
from Bio import SeqIO

directory = sys.argv[1]
for filename in os.listdir(directory):
	if filename.endswith(".fasta"):
		input_file = filename
		output_file1 = input_file.split(".") [0] + ".good.fas"
		output_file2 = input_file.split(".") [0] + ".bad.fas"
		sequences = {}
		good_reads = []
		bad_reads = []
		with open(filename, "r") as file:
			for line in file:
				line=line.rstrip()
				if (line[0] == ">"):
					header = line
					sequences[header] = ""
				else:
					data = line
					sequences[header] += data
#figure out which reads are good/bad
		for header in sequences.keys():
			length = int(len(sequences[header]))
			#print (length)
			filter = 1-int(sys.argv[2])/100
			#print (filter)
			min_length = length - (filter * length)
			#print (min_length)
			dash_count = sequences[header].count('-')
			#print (dash_count)
			true_length = length - dash_count
			#print (true_length)
			if (true_length > min_length):
				good_reads.append(header)
			else:
				bad_reads.append(header)
		good = len(good_reads)
		bad = len(bad_reads)
		print (input_file)
		print ("Good reads:", good)
		print ("Bad reads:", bad)
#write good reads
		with open(output_file1 , "w+") as good_out:
			for header in good_reads:
				good_out.write("{}\n{}\n".format(header, sequences[header]))
#write bad reads
		with open(output_file2, "w+") as bad_out:
			for header in bad_reads:
				bad_out.write("{}\nExcluded because too short\n".format(header))
	else:
		continue
