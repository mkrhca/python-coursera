#!/usr/bin/env python
"""
Example code to read and parse a CSV file
"""

from __future__ import print_function

def parse(csvfilename):
  """
  Reads csv file named csvfilename, its content and returns the data in the file
  as a list of lists.
  """
  table = []
  with open(csvfilename, "r") as csvfile:
    for line in csvfile:
      line = line.rstrip()
      columns = line.split(',')
      table.append(columns)
  return table

def print_table(table):
  """
  Prints out table, which must be a list of lists, in a nicely formatted way.
  """
  for row in table:
    # header column left justified
    print("{0:<19}".format(row[0]), end='')
    # Remaining columns right justified
    for col in row[1:]:
      print("{0:>4}".format(col), end='')
    print("", end='\n')

table = parse("hightemp.csv")
print_table(table)

print("")
