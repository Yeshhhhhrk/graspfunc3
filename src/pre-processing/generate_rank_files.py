#!/usr/bin/env python3

import os
import sys
import re

# For generating *.rank files for all proteins

# USAGE:
#  $ python __FILE__.py <rank-files.dat>

# This assumes that there is a rank_files.dat in the
# current directory containing a list of the original
# POOL-generated rank files.

def main():
  for line in open(sys.argv[1], 'r'):
    if not line:
      continue
    generate_rank_file(line.split('\n')[0], line[3])


def generate_rank_file(fl, n):
  f = open(fl, 'r')
  lines = f.readlines()
  f.close()

  newdir = "."
  if not os.path.isdir(newdir):
    os.mkdir(newdir)
  f = open(newdir + '/' + fl.split('/')[-1].split('.')[0] + '.rank', 'w')

  for line in lines:
    #if count > 200:
    #  break
    strs = re.split("\s+", line)
    f.write(strs[1] + " " + strs[2] + "\n")
  f.close()

main()
