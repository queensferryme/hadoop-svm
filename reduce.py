import sys

import numpy as np


# read & average weights
ws = np.genfromtxt(sys.stdin)
ws = np.average(ws, 0)


# output
np.savetxt(sys.stdout.buffer, ws, fmt='%.6f', newline=' ')
print()
