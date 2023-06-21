#!/bin/python3

import zlib
import argparse
import os
import sys

# Define command-line arguments
parser = argparse.ArgumentParser(description='Compress a file using zlib')

parser.add_argument('infile', help='Input file to be compressed')
parser.add_argument('outfile', help='Output file to store compressed data')

# Check if no arguments were provided
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

# Check if input file exists
if not os.path.isfile(args.infile):
    print(f"Input file {args.infile} does not exist.")
    exit(1)

# Check if output file already exists
if os.path.isfile(args.outfile):
    print(f"Output file {args.outfile} already exists.")
    exit(1)

# Read the file
with open(args.infile, 'rb') as f_in:
    data = f_in.read()

# Compress the file
compressed_data = zlib.compress(data)

# Write the compressed file
with open(args.outfile, 'wb') as f_out:
    f_out.write(compressed_data)
