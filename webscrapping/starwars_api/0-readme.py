#!/usr/bin/env python3
''' a script that reads and prints the content of a file.
    The first argument is the file path
    The content of the file must be read in utf-8
    If an error occurred during the reading, print the error object
'''
import sys
import json
import requests


try:
	file = open('{}'.format(sys.argv[1]), 'r')
	for value in file:
		print(value, end='')
except ValueError:
	print("Error: File does not exist\npath:{}".format(sys.argv[1]))
