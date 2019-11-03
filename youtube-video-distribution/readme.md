# Analysis of youtube video distribution

## Introduction
This repository contain scripts for crawling and analysis of youtube videos. pytomo tool was used to extract logs for selected youtube videos. The logs from the crawling process where than crawled again and analysed using scripts in this repository. 

## Usage
There are two files script files namely **parser.py** and **create-csv.sh**. **parser.py** contains code to analyse the log files and extract important data from them. **create-csv.sh** is a bash script which finds all the pytomo log files in the said folder and create an csv file with all the desired extracted data. The CSV is than fed into **statistics.rmd** to create useful illustrations.

Both scrip files should be palaced in logs folder which is parent folder of all the logs. The directory structure should be like 

- logs
  - parser.py // script file
  - create-csv.sh // script file
  - friday-afternoon // log directory for specific time and day
  - friday-noon // log directory for specific time and day
  - friday-evening // log directory for specific time and day

The syntax to use create-csv is as follows

```
./create-csv.sh <directory-path> <location from which video were crawled> <time of day for video crawl> <day at which video was crawled>
```

A sample create-csv commands looks like as follows:

```
./create-csv.sh friday-afternoon/India/logs/ ASIA AFT FRI
```

