import sys

W1, W2, count = 0, 0, 0

for line in sys.stdin:
    w1, w2 = line.split("\t")
    W1 += float(w1)
    W2 += float(w2)
    count += 1

print("{}\t{}".format(W1 / count, W2 / count))
