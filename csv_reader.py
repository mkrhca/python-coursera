#!/usr/bin/env python
"""
using the csv module.
Written by professors from rice University. Added here for my reference. 
"""
from __future__ import print_function
import csv

def parse(csvfilename):
  """
  Reads CSV file named csvfilename, parses its content and returns the data
  within the file as a list of lists.
  """
  table = []
  with open(csvfilename, "r") as csvfile:
    csvreader = csv.reader(csvfile, skipinitialspace = True)
    for row in csvreader:
      table.append(row)
  return table

def print_table(table):
  """
  Prints out the table, which must be a list of lists, in a nicely formatted way.
  """
  for row in table:
    # Header column left justified
    print("{0:<19}".format(row[0]), end='')
    # Remaining columns right justified
    for col in row[1:]:
      print("{0:>4}".format(col), end='')
    print("", end='\n')

table = parse("hightemp2.csv")
print_table(table)

print("")
