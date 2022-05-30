from Bio import SeqIO
import sys



record_dict = SeqIO.to_dict(SeqIO.parse(sys.argv[1], "fasta"))
output_file=open(sys.argv[2],"w")


#record_dict = SeqIO.to_dict(SeqIO.parse("D:/Cybox/Research/restart/sequences/Pfam_7tm_6.fasta", "fasta"))
#output_file=open("sequences/Pfam_7tm_6_size_selection_output_350_500.fasta","w")

def filter_by_size(record_dictionary):
    counter=0
    removed=0
    too_short=[]
    too_long=[]
    for key,value in record_dictionary.items():
        if len(value) > 350:
            if len(value)<500:
                counter=counter+1
                output_file.write(">"+str(key)+"\n")
                output_file.write(str(value.seq) + "\n")
            else:
                too_long.append(key)
                removed=removed+1
        else:
            too_short.append(key)
            removed=removed+1
        
    
    print("Original total: "+str(len(record_dict)))   
    print(str(removed)+" sequences removed")
    print("New total: "+str(counter))
    output_file.close()
        
filter_by_size(record_dict)