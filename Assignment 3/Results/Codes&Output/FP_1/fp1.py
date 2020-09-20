from pyspark import SparkContext
import sys
from pyspark.mllib.fpm import FPGrowth

sc = SparkContext("local","FP1")
data = sc.textFile(sys.argv[1])
transactions = data.map(lambda line: list(set(line.strip().split(','))))
min_support = 0.04
f = open("data/fp1_out.txt","w")
model = FPGrowth.train(transactions, minSupport=min_support, numPartitions=20)
model.save(sc,"target/tmp/frequent_model_1")
result = model.freqItemsets().collect()
f.write("Support : "+str(min_support)+"\n")
for fi in result:
    f.write(str(fi)+"\n")
