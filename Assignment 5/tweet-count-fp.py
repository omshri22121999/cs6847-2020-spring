import json
import os
from pyspark import SparkContext,SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import string
import sys
import re
from pyspark.mllib.fpm import FPGrowth

stop_words = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"]
def writeToFile(rdd):
	with open("count.txt","w") as f:
		f.write(str(rdd.count()))
	rdd_words = rdd.map(lambda line: list(filter(lambda a: a != "" and a not in stop_words, list(set(line.strip().split(' ')))))).filter(lambda x:x!=[])
	model = FPGrowth.train(rdd_words, minSupport=0.02, numPartitions=20)
	result = model.freqItemsets().collect()
	with open("frequent_items.txt","w") as g:
		for i in range(5):
			g.write(json.dumps(result[i].items)+"\n")

os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars ~/spark-2.3.4-bin-hadoop2.6/jars/spark-streaming-kafka-0-8-assembly_2.11-2.3.4.jar pyspark-shell'
# sc.stop()
config = SparkConf().set('spark.io.compression.codec', 'snappy').set("spark.executor.memory", "4g").set("spark.driver.memory", "4g")
sc = SparkContext(conf = config)
batch_interval = 600
ssc = StreamingContext(sc, batch_interval)

twitterKafkaStream = KafkaUtils.createStream(ssc,"localhost:2181","spark-streaming",{"newyork":1})
# twitterKafkaStream = KafkaUtils.createStream(ssc,"localhost:2181","spark-streaming",{"california":1})
tweets = twitterKafkaStream.map(lambda v:json.loads(v[1])).map(lambda x: re.sub(r'[^a-zA-Z0-9@/:\' ]+', '', x['text'].lower()))
tweets.foreachRDD(writeToFile)

ssc.start()
ssc.awaitTermination()
