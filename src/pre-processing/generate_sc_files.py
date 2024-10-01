#!/usr/bin/env python3

import os
import sys

# For generating *.sc files for all proteins.

# NOTE: This requires qhull files as input.

# USAGE:
#  $ python __FILE__.py <pdb-files.dat>

def main():
  pdbFile = open(sys.argv[1], 'r')
  pdbs = pdbFile.readlines()
  pdbFile.close()

  def clean_up(x):
    return x.split('\n')[0]

  def qhullify(x):
    return x.replace('.pdb', '.qhull')

  pdbs = list(map(clean_up, pdbs))  # Convert map object to list
  qhulls = list(map(qhullify, pdbs))  # Convert map object to list

  for q in qhulls:
    if os.path.isfile(q) and q[-6:] == '.qhull':
      print('Processing: {0}'.format(q))
      generate_sc(os.path.dirname(q), os.path.basename(q))

def generate_sc(qhullPath, qhull):
  qhullPath = "."
  qhullFile = qhullPath + '/' + qhull
  command = "qhull TI \"" + qhullFile + "\" d QJ Ft | grep -v \"\\.\" | cut -d\' \' -f2,3,4,5 >\"" + qhullPath + "/" + qhull[:-6] + ".sc\""
  print("Command: ", command)
  os.system(command)

main()
