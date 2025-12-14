from ase.build import molecule, bulk
from ase.visualize import view
# bulk
nacl = bulk('NaCl', 'rocksalt', a=5.64, cubic=True)
view(nacl)	
