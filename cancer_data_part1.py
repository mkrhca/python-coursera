#!/usr/bin/env python
"""
Week 3 practice project template for Python Data Analysis
Reading and writing CSV files using lists

The data that we will process in the practice project was generated in 2005 by the Environmental Protection Agency
as part of an effort to understand the affect of air toxics on human health. The specific county-level data on
cancer-risk from air toxics is stored in an .xls file located here. As part of our initial processing of this data,
we have downloaded and manually removed some of the extra text from the data set. This processed CSV file which will
be a critical component of our remaining practice projects is available on Google Storage here.
https://www.epa.gov/national-air-toxics-assessment/2005-national-air-toxics-assessment
https://www.epa.gov/national-air-toxics-assessment/2005-nata-assessment-results#county
https://storage.googleapis.com/codeskulptor-isp/course3/cancer_risk05_v4_county.csv
"""
from __future__ import print_function
import csv

#########################################################
# Part 1 - Week 3

def print_table(table):
  """
  Echo a nested list to the console
  """
  for row in table:
    print(row)


def read_csv_file(file_name):
  """
  Given a CSV file, read the data into a nested list
  Input: String corresponding to comma-separated  CSV file
  Output: Lists of lists consisting of the fields in the CSV file
  """
  table = []
  with open(file_name) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',',  skipinitialspace=True)
    for row in csvreader:
      table.append(row)
  return table

def write_csv_file(csv_table, file_name):
  """
  Input: Nested list csv_table and a string file_name
  Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
  """
  with open(file_name, "wt") as csvoutfile:
    csv_writer = csv.writer(csvoutfile, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerows(csv_table)

def test_part1_code():
  """
  Run examples that test the functions for part 1
  """

  # Simple test for reader
  test_table = read_csv_file("test_case.csv")  # create a small CSV for this test
  print_table(test_table)
  print()

  # Test the writer
  cancer_risk_table = read_csv_file("cancer_risk05_v4_county.csv")
  write_csv_file(cancer_risk_table, "cancer_risk05_v4_county_copy.csv")
  cancer_risk_copy = read_csv_file("cancer_risk05_v4_county_copy.csv")

  # Test whether two tables are the same
  for row in range(len(cancer_risk_table)):
    for col in range(len(cancer_risk_table[0])):
      if cancer_risk_table[row][col] != cancer_risk_copy[row][col]:
        print("Difference at", row, col, cancer_risk_table[row][col], cancer_risk_copy[row][col])

test_part1_code()
