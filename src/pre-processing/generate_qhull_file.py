#!/usr/bin/env python3

# For generating *.qhull files from *.pdb files for all proteins.

#   For a protein, a qhull file is a list of residues with their
# coordinates. It is required for calculating the lengths of sides,
# areas of tetrahedra, etc., and is also used as an input to qhull
# for generating the protein's *.sc file.

# USAGE (for standalone):
#  $ python __FILE__.py <protein.pdb> <protein.rank>

def generate_qhull_file(pdbFile, rankFile):
  pdbData = []
  with open(pdbFile, "r") as f:
    lines = [line for line in f.read().splitlines() if line]  # List comprehension for split + filter
  for line in lines:
    pdbData.append(line.split())

  rank = []
  with open(rankFile, "r") as g:
    lines = [line for line in g.read().splitlines() if line]  # List comprehension for split + filter
  for line in lines:
    rank.append(line.split())

  h_name = pdbFile[:-4] + '.qhull'
  h = open(h_name, "w")
  strp = "3\n" + str(len(lines)) + "\n"
  h.write(strp)
  tempJ = []
  for i in range(len(lines)):
    try:
      a = rank[i][1]
    except Exception:
      import pdb
      pdb.set_trace()

    #   print a
    leng = 0
    found = False
    for j in pdbData:
      leng += 1
      if len(j) > 6:
        #if j[0] == 'ATOM' and j[2] == 'CA' and a in j[4]: # for g1/1ug9, g8/3AJX
        #if j[0] == 'ATOM' and j[2] == 'CA' and a == j[5]: # for other proteins
        if (j[0] == 'ATOM' and j[2] == 'CA' and j[4] == 'A' + str(a)):
          tempJ = j
          found = True
          h.write('{0:>6} {1:>6} {2:>6}\n'.format(j[5], j[6], j[7]))  # f-strings for formatting
        elif (j[0] == 'ATOM' and j[2] == 'CA' and j[4] == 'A' and j[5] == a):  # for g9/3eu8
          tempJ = j
          found = True
          h.write('{0:>6} {1:>6} {2:>6}\n'.format(j[6], j[7], j[8]))  # f-strings for formatting

    if not found:
      print("Warning: Residue #" + str(a) + " (at pos. " + str(i) + ") Not found!")

  h.close()

# if this is being run standalone
if __name__ == '__main__':
  import sys
  generate_qhull_file(sys.argv[1], sys.argv[2])
