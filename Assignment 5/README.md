

# Assignment 5

By Om Shri Prasath - EE17B113

## Requirements

- Amazon EC2 Instance
- Twitter API's
(Note : Bounding Boxes for locations got from [here](https://anthonylouisdagostino.com/bounding-boxes-for-all-us-states/))

## Setup

- Create a Amazon EC2 Instance with at least 8GB of RAM.
- Allow security group to allow HTTP inbound and Custom TCP at port 5000
- SSH into the instance
- Install **pip** , **java** and **apache** using the following commands:

```bash
sudo apt update
sudo apt install python-pip openjdk-8-jre-headless apache2
```

- Download the latest version of **pre-built** Kafka from [here](https://kafka.apache.org/downloads) using **wget**.

```bash
wget https://downloads.apache.org/kafka/2.5.0/kafka_2.13-2.5.0.tgz
```

- Extract the zip file :

```bash
tar -xzf kafka_2.13-2.5.0.tgz
```

- Delete the zip **(not necessary though)**

```bash
rm kafka_2.13-2.5.0.tgz
```

- Go into the Kafka folder and run both Zookeeper and Kafka.

```bash
nohup ~/kafka_2.13-2.5.0/bin/zookeeper-server-start.sh ~/kafka_2.13-2.5.0/config/zookeeper.properties > ~/zookeeper-logs &
nohup ~/kafka_2.13-2.5.0/bin/kafka-server-start.sh ~/kafka_2.13-2.5.0/config/server.properties > ~/kafka-logs &
```

- Create a topic for the tweets to be stored using the following command :

```bash
~/kafka_2.13-2.5.0/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic newyork
~/kafka_2.13-2.5.0/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic california
```

- After creating the topic, the server is ready to run. Install the required python libraries for streaming tweets.

```bash
pip install kafka-python python-twitter tweepy numpy flask
```

- Upload `tweet-streaming.py` code to the server.

- Run the `tweet-streaming.py` file after adding the Twitter API credentials.

```bash
screen
python tweet-streaming.py
```
Then use Ctrl+A and D to exit.

- Check if the tweets are streaming by checking the topic : 
```bash
~/kafka_2.13-2.5.0/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic newyork --from-beginning
```

- The tweets will be streaming until stopped.
- Download the latest version of **pre-built** Spark from [here](http://spark.apache.org/downloads.html) using **wget**.
```bash
wget https://downloads.apache.org/spark/spark-2.4.6/spark-2.4.6-bin-hadoop2.7.tgz
```

- Extract the zip file :

```bash
tar -xzf spark-2.4.6-bin-hadoop2.7.tgz
```

- Delete the zip **(not necessary though)**

```bash
rm spark-2.4.6-bin-hadoop2.7.tgz
```
- Run the following command to install Spark Kafka Streaming Library 

```bash
wget https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-8-assembly_2.11/2.4.6/spark-streaming-kafka-0-8-assembly_2.11-2.4.6.jar -P ~/spark-2.4.6-bin-hadoop2.7/jars/
```

- Upload `tweet-count-fp.py` code to the server.

- Run the `tweet-count-fp.py` file.
```bash
nohup spark-2.4.6-bin-hadoop2.7/bin/spark-submit tweet-count-fp.py > out.log &
```
- Once the output of the count and frequent sets occur, copy `server.py` and run it as below:
```bash
screen
python server.py
```

- Do the above same for California in new machine.
- After that copy `test.html` to `/var/www/html` in one of the machines and subsitute the *ip address* of the machines in the particular function of the city `setNewYork` and `setCalifornia`
- Now the data will be viewed using the html page.
