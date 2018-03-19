The functionality of this application is to read the log file  and Call three sub command to hanlde three different requirements, <br/>
requirements where to create are <br/>
1 :- Histogram for the HTTPS Status Code. <br/>
2:- To get the first top Ten Request Time. <br/>
3:- To create Mean and Median for the Requst time. <br/>

## Getting Started

These instructions will get you a copy of the Application up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 2.6 or Greater install <br/>
Cement 2.X

### Installing

To Install Cement , Please refer below link <br/>
http://cement.readthedocs.io/en/latest/dev/installation/ <br/>


## How to Execute this Application
To Execute this program we have to follow step as mentioned below :- <br/>
To execute the command to get the Histogram of HTTP Status is <br/>
python myapp.py histogramHttpStatus --foo FileName <br/>
To execute the command to get the  top 10 Request time infomration  is <br/>
python myapp.py topTenStatusTimes --foo File Name <br/>
To execute the command to get the  MeanAndMedian for Request time is <br/>
python myapp.py meanAndMedianStatusTimes --foo FileName <br/>

## Authors
Sudeep Jain
