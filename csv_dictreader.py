#!/usr/bin/env python
"""
using csv.Dictreader.
Written by professors from rice University. Added here for my reference.
"""
from __future__ import print_function
import csv

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr',
          'May', 'Jun', 'Jul', 'Aug',
          'Sep', 'Oct', 'Nov', 'Dec')

def dictparse(csvfilename, keyfield):
  """
  Reads csv file named csvfilename, parses its contents and return the data as a dictionary of dictionaries.
  """
  table = {}
  #with open(csvfilename, "rt", newline='') as csvfile: # works only in python 3
  with open(csvfilename, "rt") as csvfile:
    csvreader = csv.DictReader(csvfile, skipinitialspace =True)
    for row in csvreader:
      table[row[keyfield]] = row
  return table

def print_table(table):
  """
  Prints out the table, which must be a dictionary of dictionaries, in a nicely formatted way.
  """
  print("City               ", end='')
  for month in MONTHS:
    print("{0:>6}".format(month), end='')
  print("")
  for name, row in table.items():
    # Header column left justified
    print("{0:<19}".format(name), end='')
    # Remaining columns right justified
    for month in MONTHS:
      print("{0:>6}".format(row[month]), end='')
    print("", end='\n')

table = dictparse("hightemp.csv", 'City')
print_table(table)

print("")
