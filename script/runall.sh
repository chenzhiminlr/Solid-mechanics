#!/bin/bash

for i in {1..16}; do
    dirname="${i}"
    mkdir -p "$dirname/loading"

    cp in.glass "$dirname/temp_in.glass"
    cp sbatch.sh "$dirname/temp_sbatch.sh"
    cp bks.dat "$dirname/bks.dat"

    cp in.loading "$dirname/loading/in.loading"
    cp sbatch_loading.sh "$dirname/loading/sbatch_loading.sh"

    random_seed=$(shuf -i 100000-999999 -n 1)

    sed -i "4s|variable seed equal .*|variable seed equal $random_seed|" "$dirname/temp_in.glass"

    pushd "$dirname" > /dev/null
    job_id=$(sbatch temp_sbatch.sh | awk '/Submitted batch job/ {print $4}')
    popd > /dev/null

    pushd "$dirname/loading" > /dev/null
    sbatch --dependency=afterok:$job_id sbatch_loading.sh
    popd > /dev/null
done