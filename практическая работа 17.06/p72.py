file = open('text.txt', 'r')
from pathlib import Path
path = Path('text.txt')
print(path.read_text())
file.close()