#!/usr/bin/env python
"""
using csv.Dictreader.
Written by professors from rice University. Added here for my reference.
"""
from __future__ import print_function
import csv

#MONTHS = ('Jan', 'Feb', 'Mar', 'Apr',
#          'May', 'Jun', 'Jul', 'Aug',
#          'Sep', 'Oct', 'Nov', 'Dec')

def dictparse(csvfilename, keyfield, separator, quote, quotestrategy):
  """
  Reads csv file named csvfilename, parses its contents and return the data as a dictionary of dictionaries.
  """
  table = {}
  #with open(csvfilename, "rt", newline='') as csvfile:
  with open(csvfilename, "rt") as csvfile:
    csvreader = csv.DictReader(csvfile,
                               skipinitialspace =True,
                               delimiter=separator,
                               quotechar=quote,
                               quoting=quotestrategy)
    for row in csvreader:
      table[row[keyfield]] = row
  return table, csvreader.fieldnames

def print_table(table, fieldnames):
  """
  Prints out the table, which must be a dictionary of dictionaries, in a nicely formatted way.
  """
  print("{0:<19}".format(fieldnames[0]), end='')
  for field in fieldnames[1:]:
    print("{0:>6}".format(field), end='')
  print("")
  for name, row in table.items():
    # Header column left justified
    print("{0:<19}".format(name), end='')
    # Remaining columns right justified
    for field in fieldnames[1:]:
      print("{0:>6}".format(row[field]), end='')
    print("", end='\n')

table, fieldnames = dictparse("hightemp.csv", 'City', ',', '"', csv.QUOTE_MINIMAL)
print(fieldnames)
print_table(table, fieldnames)

print("")
print("")


table2, fieldnames2 = dictparse("hightemp2.csv", 'City', ',', '"', csv.QUOTE_NONNUMERIC)
print(fieldnames2)
print_table(table2, fieldnames2)

print("")
print("")

table3, fieldnames3 = dictparse("hightemp3.csv", 'City', ' ', "'", csv.QUOTE_NONNUMERIC)
print(fieldnames3)
print_table(table3, fieldnames3)

print("")
print("")
