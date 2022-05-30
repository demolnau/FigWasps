# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:19:46 2022

@author: Devin
remove duplicates from a fasta sequence
returns a fasta sequence without duplicates
"""
from Bio import SeqIO
import sys

#read in sequences as a dictionary
record_dict = SeqIO.to_dict(SeqIO.parse(sys.argv[1], "fasta"))
output_file=open(sys.argv[2],"w")

def identify_duplicates(record_dictionary):
    double_check=[]
    duplicates=[]
    for key in record_dictionary:
        true_name=key.split("/")
        if true_name[0] in double_check:
            if true_name[0] not in duplicates:
                duplicates.append(true_name[0])
        else:
            double_check.append(true_name[0])
        
    return duplicates  

to_remove=identify_duplicates(record_dict)


def remove_duplicates(list_to_remove, record_dictionary):
    dict2 = record_dictionary.copy()
    for key,value in record_dictionary.items():
        if any(terms in key for terms in list_to_remove): 
            dict2.pop(key)
    print("Original total: "+str(len(record_dictionary)))   
    print(str(len(list_to_remove))+" sequences removed")
    print("New total: "+str(len(dict2)))
    return dict2   
dict_no_dup=remove_duplicates(to_remove, record_dict)

# %%  
def make_fasta_file(dictionary_of_interest, output_file_name):
    output_file=open(output_file_name,"w")
    for key,value in dictionary_of_interest.items():
        output_file.write(">"+str(key)+"\n")
        output_file.write(str(value.seq) + "\n")
    output_file.close()

make_fasta_file(dict_no_dup,sys.argv[2])













