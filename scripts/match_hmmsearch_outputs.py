"""
Purpose: to take the exonerate output file and match those to the hymenopteran OR sequences that it were identified
arguments below:
python hymenopteran_wasp_OR_Sequences(filtered for illegal characters & size) hmm_search_output new_fasta_sequence_of_output 
"""


# %%
from enum import unique
from operator import contains
from Bio import SeqIO
import pandas as pd
import sys
import numpy as np


# %%
record_dict = SeqIO.to_dict(SeqIO.parse(sys.argv[1], "fasta"))
df_manual = pd.read_csv(sys.argv[2], sep='\t', names=["blank", "full sequence E-value","full sequence score","full sequence bias", "best domain E-value", "best domain score", "best domain bias", "Domain exp", "Domain N", "Sequence", "Description"])
df_manual = df_manual.drop(columns=["blank","Description"])

# %%
def match_key_to_fasta_sequence(keys_of_interest, dictionary_of_interest):
    output_dictionary={}
    for key,value in dictionary_of_interest.items():
        if key in keys_of_interest:
            output_dictionary[key]=value
    print("Number of sequences identified:" + str(len(keys_of_interest)))
    print("Number of unique sequences identified:"+str(len(np.unique(keys_of_interest))))
    print("Number of sequences in chalcid OR sequence dictionary:" + str(len(dictionary_of_interest)))  
    print("Number of sequences in matched OR sequences:" + str(len(output_dictionary)))
    return output_dictionary

manual_dict=match_key_to_fasta_sequence(df_manual["Sequence"].to_list(), record_dict)  

# %%  
def make_fasta_file(dictionary_of_interest, output_file_name):
    output_file=open(output_file_name,"w")
    for key,value in dictionary_of_interest.items():
        output_file.write(">"+str(key)+"\n")
        output_file.write(str(value.seq) + "\n")
    output_file.close()


# %%
make_fasta_file(manual_dict,sys.argv[3])