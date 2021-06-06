.PHONY: all data run

all: run

data:
	python dataset.py 3
	hadoop fs -rm -r -f /input
	hadoop fs -put data/input /input

run:
	hadoop fs -rm -r -f /output
	hadoop jar ${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
	    -files   map.py,reduce.py  \
	    -input   /input            \
	    -output  /output           \
	    -mapper  "python map.py"   \
		-reducer "python reduce.py"
