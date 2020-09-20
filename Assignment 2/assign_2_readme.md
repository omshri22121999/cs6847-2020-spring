# Hints to run the program
Here we list down the commands and the steps we used for running the map-reduce tasks. We were a team of only 2 students, hence we excecuted the program on 1 master and 2 slaves.

## Installation

Install Virtual Box into all the 

```bash
sudo apt-get update
sudo apt-get upgrade
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb http://download.virtualbox.org/virtualbox/debian xenial contrib"
sudo apt-get update
sudo apt-get install virtualbox-5.2
```

## Uploading data and files into corresponding folders in the master VM through FileZilla

```python
Host : sftp://192.168.43.62
Username : mool
Password : mool
Port : 22
```

## Running the final map reduce(Ex. most popular route)

Run the following in the /usr/local/hadoop directory.
```python
bin/hadoop jar./share/haddop/tools/lib/hadoop-streaming-2.5.2.jar -D mapred.reduce.tasks=12
-mapper ~/cs6847-coud-computing/most-popular/mapper.py -reducer ~/cs6847-coud-computing
/most-popular/reducer.py input /input/df_t.csv -output /outputFile
```

## Changing the number of reducers:
Change the value of the parameter "mapred.reduce.tasks" to the required number of reducers.(12 Ideal)

## Changing the slow start parameter
```bash
Change the value mapred.reduce.slowstart.completed.maps in steps from 0.0 to 1.0 in the mapred-site.xml
A good value to choose will be greater than 0.8
```
