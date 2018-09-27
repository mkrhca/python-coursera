#Project Description: File Differences
# https://www.coursera.org/learn/python-representation/supplement/M2jL1/project-description-file-differences
def singleline_diff(line1, line2):
  if len(line1) < len(line2):
    for i in range(len(line1)):
      if line1[i] != line2[i]:
        return i
  elif len(line1) > len(line2):
    for i in range(len(line2)):
      if line1[i] != line2[i]:
        return i
  else:
    for i in range(len(line2)):
      if line1[i] != line2[i]:
        return i

  return "IDENTICAL"

def singleline_diff_format(line1, line2, idx):
  retval = line1 + "\n"
  retval += "=" * idx + "^\n"
  retval += line2 + "\n"
  return retval

def multiline_diff(lines1, lines2):
  if singleline_diff(lines1, lines2) == "IDENTICAL":
    return ("IDENTICAL", "IDENTICAL")
  else:
    retval = singleline_diff(lines1, lines2)
    return (lines1, retval)

def get_file_lines(filename):
  with open(filename) as f:
    list_of_lines = f.readlines()

  list_of_lines = [x.strip() for x in list_of_lines]
  return list_of_lines

def file_dif_format(filename1, filename2):
  first_file_list = get_file_lines(filename1)
  second_file_list = get_file_lines(filename2)
  for i in range(len(first_file_list)):
    test = multiline_diff(first_file_list[i], second_file_list[i])
    if not "IDENTICAL" in test:
      output_string = "Line " + str(i) + ":"
      output_string += "\n"
      idx = singleline_diff(first_file_list[i], second_file_list[i])
      diff_values = singleline_diff_format(first_file_list[i], second_file_list[i], idx)
      output_string += diff_values
      return output_string

  return "No differences\n"

print file_dif_format('/tmp/f1', '/tmp/f2')
