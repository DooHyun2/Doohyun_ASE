from ase.build import bulk
from ase.visualize import view
#diamond structure
si = bulk('Si', 'diamond', a=5.43, cubic=True)
view(si)
