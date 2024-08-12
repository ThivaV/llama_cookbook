#!/bin/bash

# check if at least one argument is provided
if [ $# -eq 0 ]; then
    echo "No arguments provided. Usage: $0 arg1 [arg2 ... argN]"
    exit 1
fi

echo "Source chunk files path: $1"
# ex: ../data/master_data/kidney_disease_ct_scan_dataset_part_*

echo "Destination to make the complete tar.gz file: $2"
# ex: ../data/master_data/kidney_disease_ct_scan_dataset.tar.gz

echo "Chunk prefix: $3"
# ex: kidney_disease_ct_scan_dataset_part_

# define variables
SOURCE=$1
PART_PREFIX=$3

# concatenate the parts
cat $SOURCE > $s2

# cleanup splits after the tar.gz file creation
rm ${PART_PREFIX}*