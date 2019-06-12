# Exercise 6
from pathlib import Path

input_dir  = Path("data")

# 1. Download the following MSG data (usual password): https://box.uni-marburg.de/index.php/s/9CIXvdZQtHI5Zwb
#    Save the file into the data directory but don't commit it to github!!! [1P]

# 2. Read the Scene using SatPy. [1P]

# 3. Load the composites "natural_color" and "convection" [2P]

# 4. Resample the fulldisk to the Dem. Rep. Kongo and its neighbours [4P] 
#    by defining your own area in Lambert Azimuthal Equal Area. 
#    Use the following settings:
#      - lat and lon of origin: -3/23
#      - width and height of the resulting domain: 500px
#      - projection x/y coordinates of lower left: -15E5
#      - projection x/y coordinates of upper right: 15E5 

# 5. Plot the resampled Scene on your screen in both loaded composites. [2P]
#    You don't have to save the images.