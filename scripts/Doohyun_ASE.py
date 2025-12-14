from ase.io import read
from ase.visualize import view

# 1. CIF file read
structure = read('LLZO.cif')

# 2. 3D
view(structure, viewer='ngl')
