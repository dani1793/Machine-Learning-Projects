# Url Crawler

## Introduction
The code provide scripts to automatically crawl data from url. The script is non I/O blocking and can be converted into corn job if required. 

## Usage
### Crawling Script
The crawler takes in a csv file without header. The first column of each row should contain the url to crawl and the rest of the columns are the regex combination for data to be crawled. The sample row for csv file could look like as follows. The separator for the below example is **;**.
`https://dawn.com;((the)\D+\.);((in)\D+\.);((div)\D+\.)`
**NOTE: The separator should be selected so that it does not conflict with regex provided**

The ouput file has format of as follows
`https://dawn.com,((the)\D+\.),<crawled data>`

The script takes in command line input and flags to configure the crawler. The available inputs are defined below

| Flags       | Description |
| ------------- |:-------------:| 
| --input-file | The .csv file which contain url with regex      | 
| --input-delimiter | The delimiter used for input csv file | 
| --output-file | The .csv file which contain results of crawled data | 
| --output-delimiter | The delimiter used for output csv file | 
| --batch-size | The number of urls processed per batch | 

A sample command looks is as follows
`python /Users/daniyalusmani/aalto/cgi/main.py --input-file /Users/daniyalusmani/aalto/cgi/data.csv --input-delimiter ';' --batch-size '25' --output-file '/Users/daniyalusmani/aalto/cgi/res.csv' --output-delimiter ';'`

### Cron Script
**python-crontab** package was used for creating cron jobs. To install cron job conda environment was used
`conda install -c conda-forge python-crontab`

There are some additional parameters used by cron script the parameters are as follows
| Flags       | Description |
| ------------- |:-------------:| 
| --repeat | The option tell if we want to repeat the script or not(takes 'true' or 'false')      | 
| --cron-user | The user which would be used to authorize the cron job      | 
| --hour | The number of hours after which cron job should be repeated       | 
| --days | The number of days after which cron job should be repeated      | 
| --stop-cron | Flag which if set stops all the currently running cron jobs|

A sample command for cron job is as follows
` python cron-jobs.py --input-file /Users/daniyalusmani/aalto/cgi/data.csv  --input-delimiter ';' --batch-size 25 --output-file /Users/daniyalusmani/aalto/cgi/res.csv  --output-delimiter ';' --repeat true --day 1 --cron-user daniyalusmani`