#!/bin/bash
# Copy/paste this job script into a text file and submit with the command:
#    sbatch thefilename
# job standard output will go to the file slurm-%j.out (where %j is the job ID)

#SBATCH --time=120:00:00   # walltime limit (HH:MM:SS)
#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=32   # 16 processor core(s) per node
#SBATCH --job-name="exonerate obtusifolia whole"
#SBATCH --mail-user=demolnau@iastate.edu   # email address
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --mem=1000GB
# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE
module load exonerate/2.4.0-py2-ddwi7zh
exonerate --model protein2genome --maxintron 1100 ../sequences/exonerate_input.fasta /home/demolnau/work/genomes/W2g_HiCanu.fasta --showtargetgff TRUE > exonerate_obtusifolia_whole.output
