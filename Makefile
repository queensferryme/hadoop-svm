.PHONY: all data result run

all: data run result

data:
	python data.py 2
	hadoop fs -rm -r -f /input
	hadoop fs -put data/input /input

fmt:
	black .

result:
	python result.py

run:
	hadoop fs -rm -r -f /output
	hadoop jar ${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
	    -files   map.py,reduce.py  \
	    -input   /input            \
	    -output  /output           \
	    -mapper  "python map.py"   \
	    -reducer "python reduce.py"
