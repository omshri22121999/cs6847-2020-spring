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
(training, test) = ratings.randomSplit([0.8, 0.2])

reg_param = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]
maxIter = [5,10,15,20]

f = open("ALS_out.txt","w")

for i in reg_param:
	for j in maxIter:
		als = ALS(maxIter=j, regParam=i, userCol="userId", itemCol="movieId", ratingCol="rating",coldStartStrategy="drop")
		model = als.fit(training)

		predictions = model.transform(test)
		evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
	                                predictionCol="prediction")
		rmse = evaluator.evaluate(predictions)
		f.write("No.of Iterations = " + str(j) + " & Regularization Parameter = "+str(i)+"\n\n")
		f.write("Root-mean-square error = " + str(rmse)+"\n\n")
