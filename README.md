# Hadoop SVM

Train a support vector machine distributedly on a Hadoop cluster.

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
    -files   map.py,reduce.py
    -input   /input
    -output  /output
    -mapper  "python map.py"
    -reducer "python reduce.py"
```

## References

1. Alham, N. K., Li, M., Liu, Y., & Hammoud, S. (2011). A MapReduce-based distributed SVM algorithm for automatic image annotation. *Computers & Mathematics with Applications, 62(7)*, 2801-2811.
2. <http://cs229.stanford.edu/materials/smo.pdf>

