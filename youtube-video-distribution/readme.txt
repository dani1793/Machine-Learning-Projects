There are two files parser.py and create-csv.sh

you need to numpy and pandas installed for them to work

place both the files in logs folder which is parent folder of all the logs. The directory structure should be like 

- logs
  - parser.py
  - create-csv.sh
  - friday-afternoon
  - friday-noon
  - friday-evening

you need to use create-csv.sh to create the final csv

example command for create-csv is 

./create-csv.sh friday-afternoon/India/logs/ ASIA AFT FRI

This command fetches all the log files from the directory provided and parse them. The second argument is the location, third argument is time and forth argument is day. The details about allowed values of these argument is provided in parser.py you can check what value to give from there. Once all the logs are parsed using correct argument you will have finalCSV.csv which will contain all the compiled data and we can perform analysis from it (create graphs and stuff)
