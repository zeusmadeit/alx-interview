#!/usr/bin/python3
""" reads stdin line by line and computes metrics """
import sys

for line in sys.stdin:
    if line.rstrip() == 'exit':
        break
    print(f'Processing Message from sys.stdin *****{line}*****')

