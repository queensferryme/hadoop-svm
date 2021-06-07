import json
import sys
from io import StringIO

import numpy as np


# read & average weights
al, sv, b = [], [], []
for line in sys.stdin:
    data = json.loads(line)
    al.append(np.genfromtxt(StringIO(data['al'])))
    sv.append(np.genfromtxt(StringIO(data['sv'])))
    b.append(float(data['b']))

al = np.hstack(al)
sv = np.vstack(sv)
b = np.mean(np.array(b))

# output
data = {}

s = StringIO()
np.savetxt(s, al, fmt='%.6f')
data['al'] = s.getvalue()

s = StringIO()
np.savetxt(s, sv, fmt='%.6f')
data['sv'] = s.getvalue()

data['b'] = b

print(json.dumps(data))
