#!/bin/bash

# Copy/paste this job script into a text file and submit with the command:
#    sbatch thefilename
# job standard output will go to the file slurm-%j.out (where %j is the job ID)

#SBATCH --time=1:00:00   # walltime limit (HH:MM:SS)
#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=16   # 16 processor core(s) per node 
#SBATCH --job-name="hmmsearch commands combined"
#SBATCH --mail-user=demolnau@iastate.edu   # email address
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE
module load muscle/3.8.1551-ylw4paz
module load hmmer/3.2.1-mpich-nl2zszt
muscle -in  ../sequences/pfam_7tm_6_size_filtered_350aa.fasta -out pfam_7tm_6_size_filtered_350aa.aln
hmmbuild 7tm_6_profile.hmm pfam_7tm_6_size_filtered_350aa.aln
hmmsearch 7tm_6_profile.hmm ../sequences/filtered_by_size.fasta > hmmsearch_hym_pfam_7tm_6.output

