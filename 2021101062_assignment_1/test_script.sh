#write a bash script to take a file from command line as input 
#and then send this file to another python file as input

#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <test_file>"
    exit 1
fi

test_file="$1"

if [ ! -f "$test_file" ]; then
    echo "Error: File '$test_file' not found."
    exit 1
fi

python_script="test.py"

if [ ! -f "$python_script" ]; then
    echo "Error: Python script '$python_script' not found."
    exit 1
fi

python3 "$python_script" "$test_file"
