#!/bin/bash

# check if at least one argument is provided
if [ $# -eq 0 ]; then
    echo "No arguments provided. Usage: $0 arg1 [arg2 ... argN]"
    exit 1
fi

echo "Source .tar.gz file path: $1"
echo "Destination: $2"
echo "Chunk prefix: $3"
echo "Chunk size: $4"

# define variables
SOURCE=$1
DESTINATION=$2
PART_PREFIX=$3
PART_SIZE=$4

# split the archive into smaller parts
split -b $PART_SIZE $SOURCE $PART_PREFIX

# cleanup the tar.gz file
rm $SOURCE

mv ${PART_PREFIX}* $DESTINATION