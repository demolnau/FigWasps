#!/bin/bash
set -e
set -u
set -o pipefail
input="$1"
filename="$(basename ${input} _accessions_with_versions.txt)_gene_accession.txt"
cat $1 | cut -f1 >  $filename

filename2="$(basename ${input} _accessions_with_versions.txt)_transcript_id.txt"
cat $1 | cut -f4 >  $filename2

#wc -l ${filename}| awk '{print $1}'
#word_count="$(wc -l ${filename}| awk '{print $1}')"
#declare -i word_count
#let split=word_count/2
#split=($word_count) / 2
#accessions=head -n${split}
#versions=tail -n${split}



