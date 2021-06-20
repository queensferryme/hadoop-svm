import json
import subprocess
from io import StringIO

import matplotlib.pyplot as plt
import numpy as np


data = np.vstack([np.genfromtxt(f"data/input/dataset{i}.csv") for i in range(1, 6)])

positive = data[data[:, -1] > 0]
plt.scatter(positive[:, 0], positive[:, 1], c="red")

negative = data[data[:, -1] <= 0]
plt.scatter(negative[:, 0], negative[:, 1], c="blue")

plt.savefig("result/data.png")

xmin, xmax = np.min(data[:, 0]), np.max(data[:, 0])
ymin, ymax = np.min(data[:, 1]), np.max(data[:, 1])
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

w = np.genfromtxt("data/weight.csv")
plt.axline(
    (xmin, (w[0] * xmin + w[2]) / -w[1]),
    (xmax, (w[0] * xmax + w[2]) / -w[1]),
    c="green",
    label="ground truth",
)

process = subprocess.Popen(
    ["hadoop", "fs", "-cat", "/output/part-00000"], stdout=subprocess.PIPE
)
result = json.load(process.stdout)

sv = np.genfromtxt(StringIO(result["sv"]))
positive = sv[sv[:, -1] > 0]
negative = sv[sv[:, -1] < 0]
plt.scatter(positive[:, 0], positive[:, 1], c="blue", marker="d")
plt.scatter(negative[:, 0], negative[:, 1], c="red", marker="d")

plt.legend()

plt.savefig("result/sv.png")

alpha = np.genfromtxt(StringIO(result["al"]))
b = float(result["b"])


def predict(x):
    sum = 0
    for i in range(len(sv)):
        x_i, y_i = sv[i, :-1], sv[i, -1]
        sum += alpha[i] * y_i * np.dot(x_i, x.T)
    return 1 if sum > 0 else -1


prediction = np.array([predict(x) for x in data[:, :-1]])

plt.clf()

positive = data[prediction > 0]
plt.scatter(positive[:, 0], positive[:, 1], c="red")

negative = data[prediction <= 0]
plt.scatter(negative[:, 0], negative[:, 1], c="blue")

plt.savefig("result/result.png")
