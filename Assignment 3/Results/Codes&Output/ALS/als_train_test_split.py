from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row
import sys

spark = SparkSession.builder.appName("ALS").getOrCreate()

lines = spark.read.text(sys.argv[1]).rdd
parts = lines.map(lambda row: row.value.split("::"))
ratingsRDD = parts.map(lambda p: Row(userId=int(p[0]), movieId=int(p[1]),
                                     rating=float(p[2])))
ratings = spark.createDataFrame(ratingsRDD)

splits = [0.9,0.85,0.8,0.75,0.7]


f = open("ALS_out_2.txt","w")

for i in splits:
	(training, test) = ratings.randomSplit([i, 1-i])
	als = ALS(maxIter=20, regParam=0.1, userCol="userId", itemCol="movieId", ratingCol="rating",coldStartStrategy="drop")
	model = als.fit(training)

	predictions = model.transform(test)
	evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
                                predictionCol="prediction")
	rmse = evaluator.evaluate(predictions)
	f.write("Train-Test Split = [" + str(i) + " / "+str(1-i)+"]\n\n")
	f.write("Root-mean-square error = " + str(rmse)+"\n\n")
