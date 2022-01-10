#!/bin/bash

#SBATCH --mail-user=cao20@iu.edu
#SBATCH --ntasks=1
#SBATCH --time=8:10:00

#####SBATCH --mem=58gb
#SBATCH --partition=general

#SBATCH --mail-type=FAIL,BEGIN,END
#SBATCH --job-name=dp
#SBATCH --output=dp_%j.out
#SBATCH --error=dp_%j.err

######  Module commands #####


######  Job commands go below this line #####
cd $SLURM_SUBMIT_DIR

python dpknapsack.py tiny.txt
python dpknapsack.py knapsack_tiny.txt
python dpknapsack.py knapsack_big.txt

scontrol show job=$SLURM_JOB_ID
