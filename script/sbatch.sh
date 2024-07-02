#!/usr/bin/env bash
#SBATCH --job-name runJoBs
#SBATCH --time 144:00:00
#SBATCH --gres=gpu:v100:1
#SBATCH --mem=75000
#SBATCH --partition=prioritized

srun singularity exec --nv ~/software/lmp_kokkos_gpu.sif mpirun -np 1 lmp_kokkos_cuda_mpi_sm70 -pk kokkos neigh half neigh/qeq full newton on -k on g 1 -sf kk -nc -in temp_in.glass