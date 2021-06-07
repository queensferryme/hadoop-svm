import json
import sys
from io import StringIO

import numpy as np


# initialize dataset
dataset = np.genfromtxt(sys.stdin)
# initialize parameters
C = 1.0
epochs = 10000
kernel = lambda x1, x2: np.dot(x1, x2.T)
max_passes = 3
n = dataset.shape[0]
tolerance = 1e-3

def error(x, y):
    sum = 0
    for i in range(n):
        alpha_i, x_i, y_i = alpha[i], dataset[i, :-1], dataset[i, -1]
        sum += alpha_i * y_i * kernel(x_i, x)
    return sum + b - y

# training
alpha, b, passes  = np.zeros(n), 0, 0
for epoch in range(1, epochs):
    updated = 0
    for i in range(n):
        x_i, y_i = dataset[i, :-1], dataset[i, -1]

        error_i = error(x_i, y_i)
        if not (y_i * error_i < -tolerance and alpha[i] < C) and not (y_i * error_i > tolerance and alpha[i] > 0):
            continue

        j = np.random.choice([x for x in range(0, n) if x != i])
        x_j, y_j = dataset[j, :-1], dataset[j, -1]
        error_j = error(x_j, y_j)

        alpha_i, alpha_j = alpha[i], alpha[j]

        if y_i != y_j:
            L, H = max(0, alpha_j - alpha_i), min(C, C + alpha_j - alpha_i)
        else:
            L, H = max(0, alpha_i + alpha_j - C), min(C, alpha_i + alpha_j)
        if abs(L - H) < tolerance:
            continue

        eta = 2 * kernel(x_i, x_j) - kernel(x_i, x_i) - kernel(x_j, x_j)
        if eta > 0:
            continue

        alpha[j] = alpha_j - y_j * (error_i - error_j) / eta
        alpha[j] = np.clip(alpha[j], L, H)
        if abs(alpha[j] - alpha_j) < tolerance:
            continue
        alpha[i] = alpha_i + y_i * y_j * (alpha_j - alpha[j])

        b1 = b - error_i - y_i * (alpha[i] - alpha_i) * kernel(x_i, x_i) - y_j * (alpha[j] - alpha_j) - kernel(x_i, x_j)
        b2 = b - error_i - y_i * (alpha[i] - alpha_i) * kernel(x_i, x_j) - y_j * (alpha[j] - alpha_j) - kernel(x_j, x_j)
        if 0 < alpha[i] < C:
            b = b1
        elif 0 < alpha[j] < C:
            b = b2
        else:
            b = (b1 + b2) / 2

        updated += 1

    passes = passes + 1 if updated == 0 else 0
    if passes >= max_passes:
        break


# output
al = StringIO()
np.savetxt(al, alpha[(0 < alpha) & (alpha < C)], fmt='%.6f')
sv = StringIO()
np.savetxt(sv, dataset[(0 < alpha) & (alpha < C)], fmt='%.6f')
print(json.dumps({ 'al': al.getvalue(), 'sv': sv.getvalue(), 'b': b }))
