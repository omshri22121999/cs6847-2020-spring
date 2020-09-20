## Assignment 1

The assingment consists of two parts. One is testing the server without autoscaling and one is testing it with auto-scaling

## Setting up the environment

To set up the image,

- Create a Linux (Ubuntu) Image. The one used for this assignment was Ubuntu 18.04 - Free tier(micro)

- Add the `server` folder to the image. Save the image as AMI

- When using the AMI, make sure to add the content of `server_setup.sh` to the user text(the script run at the beginning of the server creation)

- In the security groups, open the 8080 port with Custom TCP option for using the API's.

- Create the appropriate load balancer and auto scaler to load test the server

- To load test the server, [Apache Jmeter]("http://jmeter.apache.org/") is used.

- Boilerplate command `./jmeter -n -t Assgn1.jmx -Jthreads=<no. of required threads> -Jrps=<requests per second> -Jurl=<url> -Jport=<port the app is running on>`

- Example command `./jmeter -n -t Assgn1.jmx -Jthreads=1000 -Jrps=60000 -Jurl=ec2-35-171-20-26.compute-1.amazonaws.com -Jport=8080`
