"""
Read in a fasta sequence to check for any illegal amino acids or nonalphabetic characters
input:fasta sequence
output:fasta sequence (filtered)

"""
# %%
from operator import contains
from Bio import SeqIO
import pandas as pd
import sys


# %%
fasta_to_check=SeqIO.to_dict(SeqIO.parse(sys.argv[1],"fasta"))
#fasta_to_check=SeqIO.to_dict(SeqIO.parse("D:/Cybox/Research/restart/sequences/hym_OR_prot.fasta", "fasta"))


#%%
allowed_letters=("A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y","X","Z")
def is_allowed_specific_char(string1):
    tracker=0
    for letter in string1:
        if letter in allowed_letters:
            tracker= tracker + 0
        else:
            tracker= tracker + 1
    if tracker > 0:
        return False
    else :
        return True


# %%
def filter_nonletter(record_dictionary):
    removed=0
    nonletter_list=[]
    dict3 = record_dictionary.copy()
    for key,value in record_dictionary.items():
        if is_allowed_specific_char(str(value.seq)) == False :
            nonletter_list.append(key)
            dict3.pop(key)
            removed=removed+1

    print("Original total: "+str(len(record_dictionary)))   
    print(str(removed)+" sequences removed")
    print("New total: "+str(len(dict3)))
    return dict3

# %%   
filtered_fasta=filter_nonletter(fasta_to_check)
   
    
# %%  
def make_fasta_file(dictionary_of_interest, output_file_name):
    output_file=open(output_file_name,"w")
    for key,value in dictionary_of_interest.items():
        output_file.write(">"+str(key)+"\n")
        output_file.write(str(value.seq) + "\n")
    output_file.close()

#make_fasta_file(filtered_fasta, "filtered.fasta")
make_fasta_file(filtered_fasta,sys.argv[2])