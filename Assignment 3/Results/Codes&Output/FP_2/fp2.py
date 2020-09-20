from pyspark import SparkContext
import sys
from pyspark.mllib.fpm import FPGrowth

sc = SparkContext("local","FP2")
data = sc.textFile(sys.argv[1])
transactions = data.map(lambda line: list(set(line.strip().split(','))))
for i in transactions.collect():
	print str(i)
min_support = 0.0236
f = open("fp2_out.txt","w")
model = FPGrowth.train(transactions, minSupport=min_support, numPartitions=20)
model.save(sc,"target/tmp/frequent_model_2")
result = model.freqItemsets().collect()
for fi in result:
	f.write(str(fi)+"\n")
