#files and directories

from pathlib import Path

path = Path("ecommerce")
print(path.exists())
print(path.glob('*.py'))
# Absolute Path
    # C:\Program Files\Microsoft
    # /usr/local/bin
# Relative path