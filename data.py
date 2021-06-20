import os
import sys

import numpy as np


dim = int(sys.argv[1])

weight = np.random.randn(dim + 1)
threshold = 3 ** dim


def generate_dataset(path):
    dataset = []
    while len(dataset) < 200:
        x = np.random.uniform(-50, 50, dim)
        dotprod = np.sum(weight[:-1] * x) + weight[-1]
        if abs(dotprod) < threshold:
            continue
        dataset.append(np.hstack([x, 1 if dotprod > 0 else -1]))
    np.savetxt(path, np.array(dataset), fmt="%.6f")


if not os.path.exists("data/input"):
    os.makedirs("data/input")
for i in range(1, 6):
    generate_dataset(os.path.join("data/input", f"dataset{i}.csv"))
np.savetxt("data/weight.csv", weight, fmt="%.6f")
