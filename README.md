# Fig Wasps
## Identification of fig wasp chemosensory genes in Dr. John Nason's Lab
1. Gather hymenopteran sequences from NCBI and literature
'''
cd sequences/
find hymenopteran_OR_protein_sequences/ -maxdepth 1| grep -v “_OR_prot.fasta”|while read fn; do cat "$fn" >> hym_OR_prot.fasta; done

'''
2. Filter to make sure there are no illegal characters.
'''
python ../scripts/allowed_letters.py hym_OR_prot.fasta filtered_hym.fasta
'''
3. Filter the hymenopteran sequences by size. A complete OR protein sequence with one 7tm_6 domain should be roughly between 350 aa - 500 aa.
'''

python ../scripts/filter_reads_by_size.py filtered_hym.fasta filtered_by_size.fasta

'''

4. Download the 7tm_6 Pfam family from the Pfam website. This contains 10148 protein sequences  
http://pfam.xfam.org/family/7tm_6#tabview=tab1

5. Remove duplicates from 10148 sequences
'''
python ../scripts/remove_duplicates.py Pfam_7tm_6.fasta no_dup_pfam_7tm_6.fasta
'''
6. Remove sequences that might contain additional 7tm_6 domains. The easiest way to do this is by size selection between 350aa and 500 aa again.
'''
python ../scripts/filter_reads_by_size.py no_dup_pfam_7tm_6.fasta pfam_7tm_6_size_filtered_350aa.fasta
'''
7. Now that we have examples of OR protein sequences with one 7tm_6 motif in them, we can make a profile using HMMBUILD. After creating a profile, we can identify hymenopteran sequences that contain good examples of the 7tm_6 domain using HMMSEARCH. This command was done on a hpc. 
'''
cd ../hmmsearch/
sbatch combined_hmmsearch_cmds.sh
'''
8. Navigating the HMMSEARCH results: We want to select just the lines that identify one 7tm_6 motif. We select for N=1 . Do this command while still in the HMMSEARCH folder.
'''
 tail -n+15 hmmsearch_hym_pfam_7tm_6.output| tr -s ' '| sed 's/ /\t/g'| awk -F '\t' '{if ($9 == 1) print $0}' > hym_7tm_6_N1.out

'''
9. Now that we can identify which hymenopteran OR sequences contain one 7tm_6 motif we can match and pull out the fasta sequences of interest.
'''
cd ../
python scripts/match_hmmsearch_outputs.py sequences/filtered_by_size.fasta sequences sequences/hym_7tm_6_N1.out sequences/exonerate_input.fasta
'''
10. Running Exonerate to idenitfy OR sequences in the genome of interest.
'''
mkdir exonerate/
cd exonerate/
sbatch exonerate_obtusifolia_cmd.sh
'''

