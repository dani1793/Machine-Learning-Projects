# Analysis of youtube video distribution

## Introduction
This repository contain scripts for crawling and analysis of youtube videos. pytomo tool was used to extract logs for selected youtube videos. The logs from the crawling process where than crawled again and analysed using scripts in this repository. 

## Usage

**aws.sh** is a script which is uploaded to EC2 Linux instance and makes it ready to crawl youtube videos. Once the instance is ready a modified version of pytomo is uploaded to EC2 instance. Pytomo is modified to run on new youtube configurations and to allow input urls to crawl. The modified version of pytomo could be found [here](https://github.com/dani1793/Machine-Learning-Projects/tree/master/youtube-video-distribution/pytomo-https). The command used for crawling the url is as follows. `r means maximum number of round possible`, `D represents total download time`, `l represents the loop flag` and finally `S is for delay between the request`

```
python start_crawl.py -r 10 -D 1000 -l -S 20 https://www.youtube.com/watch?v=RyNFOnJdQNs https://www.youtube.com/watch?v=JUVyb5w6thI https://www.youtube.com/watch?v=VuWIiJmczOo https://www.youtube.com/watch?v=f8e42B8biAw https://www.youtube.com/watch?v=gg7qSHJL25I https://www.youtube.com/watch?v=EC6GZdVIWDE https://www.youtube.com/watch?v=2durG-6RPF8 https://www.youtube.com/watch?v=GgIl0-_oCUo
```

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

