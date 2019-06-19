#!/bin/bash
mkdir backups
for f in ./*.fasta; do
	sed -i.bak 's/seq1//g;s/>\([^_]*_\)\(.*\)$/>\2\1/;/^>/ s/$/_seq1/' "$f"
done
mv *.fasta.bak ./backups

