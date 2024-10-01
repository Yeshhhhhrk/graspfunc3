#!/usr/bin/env python3

import os
import sys
import generate_qhull_file as gqf

# For generating *.qhull files from *.pdb files for all proteins.

#   For a protein, a qhull file is a list of residues with their
# coordinates. It is required for calculating the lengths of sides,
# areas of tetrahedra, etc., and is also used as an input to qhull
# for generating the protein's *.sc file.


# USAGE:
#  $ python __FILE__.py <pdb-files.dat> <rank-files.dat>
#
# This should be run in the top-level directory.

def main():
  pdbFile = open(sys.argv[1], 'r')
  rankFile = open(sys.argv[2], 'r')
  pdbs = pdbFile.readlines()
  ranks = rankFile.readlines()
  pdbFile.close()
  rankFile.close()

  def clean_up(x):
    return x.split('\n')[0]

  pdbs = list(map(clean_up, pdbs))  # Convert map object to list
  ranks = list(map(clean_up, ranks))  # Convert map object to list

  for p, r in zip(pdbs, ranks):
    if os.path.isfile(p) and p[-4:] == '.pdb' and \
       os.path.isfile(r) and \
       r.split('.')[0][:3].lower() == p.split('.')[0][:3].lower() and \
       "rank" in r and \
       not (r[:-5] == ".rank"):  # ignore the *.rank files if present
      print('Processing: {0}\t{1}'.format(p, r))
      assert(os.path.basename(p).split('.')[0] == os.path.basename(r).split('.')[0])
      gqf.generate_qhull_file(p, r)
      print('Done with: {0}\t{1}\n'.format(p, r))

# if this is being run standalone
if __name__ == '__main__':
  main()
