import subprocess

import matplotlib.pyplot as plt
import numpy as np


data = np.genfromtxt('data/input/dataset1.csv')

positive = data[data[:, -1] > 0]
plt.scatter(positive[:, 0], positive[:, 1], c='red')

negative = data[data[:, -1] <= 0]
plt.scatter(negative[:, 0], negative[:, 1], c='blue')

xmin, xmax = np.min(data[:, 0]), np.max(data[:, 0])
ymin, ymax = np.min(data[:, 1]), np.max(data[:, 1])
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

w = np.genfromtxt('data/weight.csv')
plt.axline(
    (xmin, (w[0] * xmin + w[2]) / -w[1]),
    (xmax, (w[0] * xmax + w[2]) / -w[1]),
    c='green',
    label='ground truth'
)

process = subprocess.Popen(['hadoop', 'fs', '-cat', '/output/part-00000'], stdout=subprocess.PIPE)
w = np.genfromtxt(process.stdout)
plt.axline(
    (xmin, (w[0] * xmin + w[2]) / -w[1]),
    (xmax, (w[0] * xmax + w[2]) / -w[1]),
    c='yellow',
    label='prediction'
)

plt.legend()

plt.savefig('result.png')
