from ase.build import bulk
from ase.visualize import view
#. Cu의  면심입방 (FCC)구조 생성 

copper = bulk('Cu', 'fcc', a=3.6, cubic=True)

print(f"Structure created: {copper}")
print(f"Number of atoms: {len(copper)}")

view(copper)
