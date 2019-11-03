import re #for regex implementation
import numpy as np #to convert log files into matrix for better understanding
import argparse # argument parser
import pandas as pd
import os

parser = argparse.ArgumentParser(description='Parsing of log file')
parser.add_argument('--logfile', help='path for file to log')
parser.add_argument('--location', help='possible location values are USA, ASIA, EUROPE')
parser.add_argument('--time', help='possible times are NOON, AFT, EVE')
parser.add_argument('--day', help='possible day values are MON, TUE, WED, THUR, FRI, SAT, SUN')


args = parser.parse_args()


class PytomoLogParser():
    finalArr = np.array([['','','','','','','','','true']]);


    # properties to store for each crawled url
    resolvedIPs = []
    downloadRates = []
    caches= []
    interruptNum = 0
    error = False
    currentRound = 0
    maxRounds = 100
    currentUrl = ''

    # Regex combinations for extraction
    roundsRegex = r"(Round\s\d+\sstarted)"
    #roundsRegex = r"^#(#*)#"
    crawlRegex = r"(Crawl\sof\surl#\s\d+:\s(?<=).*$)"
    cacheFound = r"(Cache\surl\sfound:)"
    resolvedIP = r"((RTT stats found for ip: (\d+.\d+.\d+.\d+)))"
    downloadRateRegex = r"(^\[download\]*.*)(Inst_thp (\d+.\d+[a-zA-Z][a-zA-Z]))"
    interruptionNumRegex = r"(nb\sof\sinterruptions:\s(\d+))"
    errorRegex = r"(ERROR*.*(HTTP Error 429: unknown))"
    urlErrorRegex = r"(trouble message: ERROR)"
    codeErrorRegex = r"(HTTPError: HTTP Error 403: Forbidden)"

    def __init__(self, location, time, day, fileName):
        # Metadata for log file
        self.location = location;
        self.time = time;
        self.day = day;
        self.fileName = fileName;
        self.iterateLog(self.fileName);


    def addDataToTableAndClean(self, currentUrl):
        # TODO: add to table
        print('<================ information about URL ====================>')
        arr = np.array([])
        if  self.error:
            print('Error detected')
            arr = np.array([['','','',currentUrl,'','','','','true']])
        else:
            arr = np.array([[
                self.location,
                self.day,
                self.time,
                currentUrl,    
                ','.join(self.caches),
                ','.join(self.resolvedIPs),
                ','.join(self.downloadRates),
                str(self.interruptNum),
                'false'
                ]])
            print('Caches :: %s'%(','.join(self.caches)))
            print('resolvedIPs :: %s'%(','.join(self.resolvedIPs)))
            print('downloadingRates :: %s'%(','.join(self.downloadRates)))
            print('interruptions in download :: %s'%(self.interruptNum))

        self.finalArr = np.append(self.finalArr, arr, axis=0);

        # clear arrays for new iteration
        self.resolvedIPs = []
        self.downloadRates = []
        self.caches = []
        self.interruptNum = 0
        self.error = False

    def generateDataFrame(self):
        df = pd.DataFrame(self.finalArr, columns=['location', 'day', 'time', 'url', 'caches', 'resolvedIPs', 'downloadingRates', 'interruptions', 'error']);
        if os.path.isfile('./finalCSV.csv'):
            dfFinal = pd.read_csv('finalCSV.csv')
            df = dfFinal.append(df, ignore_index=True)
        print(df)
        df.to_csv('finalCSV.csv', index=False)

    def iterateLog(self, fileName):
        with open(fileName, 'r') as file:
            for line in file:
                # get regex for rounds
                rounds = re.search(self.roundsRegex, line, re.MULTILINE | re.IGNORECASE)
                if rounds:
                    # print(rounds.group());
                    self.currentRound = self.currentRound + 1
                    print('round No :: %s'%(self.currentRound))
                crawl = re.search(self.crawlRegex, line, re.MULTILINE | re.IGNORECASE)
                if crawl:
                    if self.currentUrl != '':
                        # why the number is not incrementing ?? Have to find
                        self.addDataToTableAndClean(self.currentUrl) 
                    self.currentUrl = crawl.group()
                    print('crawling :: %s'%(crawl.group()))
                cache = re.search(self.cacheFound, line, re.MULTILINE | re.IGNORECASE)
                if cache:
                    self.caches.append(cache.group())
                    # print('Cache found for this this URL')
                resolved = re.search(self.resolvedIP, line, re.MULTILINE)
                if resolved:
                    self.resolvedIPs.append(resolved.groups()[2])
                    # print('Resolved IP :: %s'%(resolved.groups()[2]))
                downloadRate = re.search(self.downloadRateRegex, line, re.MULTILINE)
                if downloadRate:
                    self.downloadRates.append(downloadRate.groups()[2])
                    # print('downloadRate :: %s'%(downloadRate.groups()[2]))
                interruptionNum = re.search(self.interruptionNumRegex, line, re.MULTILINE)
                if interruptionNum:
                    self.interruptNum = self.interruptNum + int(interruptionNum.groups()[1])
                    # print('interruptions during download :: %s'%(interruptionNum.groups()[1]))
                errorStr = re.search(self.errorRegex, line, re.MULTILINE)
                urlErrorStr = re.search(self.urlErrorRegex, line, re.MULTILINE)
                codeErrorStr = re.search(self.codeErrorRegex, line, re.MULTILINE)
                if codeErrorStr:
                    print('Error in code')
                    self.error = True
                if urlErrorStr:
                    print('URL error found')
                    self.error = True
                if errorStr:
                    self.error = True
                    break;
        self.generateDataFrame();


# get path to file
print(args.logfile)

if args.logfile and args.time and args.day and args.location:
    parser = PytomoLogParser(args.location, args.time, args.day, args.logfile)

else:
    raise Exception('path to logfile not provided')
