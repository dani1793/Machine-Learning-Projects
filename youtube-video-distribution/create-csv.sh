#!/bin/bash

#regexp = "(*.pytomo.log)"
for entry in `ls $1`; do
 # echo $entry
  case $entry in
   *[0-91:e].pytomo.log)
   python parser.py --logfile $1$entry --location $2 --time $3 --day $4
    ;;
  *)
    # echo "match not found"
    ;;
esac
done

exit

python parser.py --logfile Monday-noon/India/logs/ip-172-31-38-252.ap-south-1.compute.internal.youtube.2019-10-21.11_08_34.pytomo.log --location ASIA --time NOON --day MON

# Friday afternoon
python parser.py --logfile friday-afternoon/California/ip-172-31-6-182.us-west-1.compute.internal.youtube.2019-10-18.13_21_10.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/California/ip-172-31-6-182.us-west-1.compute.internal.youtube.2019-10-18.13_16_58.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/California/ip-172-31-6-182.us-west-1.compute.internal.youtube.2019-10-18.13_12_40.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/California/ip-172-31-6-182.us-west-1.compute.internal.youtube.2019-10-18.13_07_46.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/California/ip-172-31-6-182.us-west-1.compute.internal.youtube.2019-10-18.13_01_44.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/California/ip-172-31-6-182.us-west-1.compute.internal.youtube.2019-10-18.13_01_44.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/India/logs/ip-172-31-41-197.ap-south-1.compute.internal.youtube.2019-10-18.13_01_46.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/India/logs/ip-172-31-41-197.ap-south-1.compute.internal.youtube.2019-10-18.13_01_46.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/India/logs/ip-172-31-41-197.ap-south-1.compute.internal.youtube.2019-10-18.13_07_43.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/India/logs/ip-172-31-41-197.ap-south-1.compute.internal.youtube.2019-10-18.13_18_50.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/India/logs/ip-172-31-41-197.ap-south-1.compute.internal.youtube.2019-10-18.13_18_50.pytomo.log --location USA --time AFT --day FRI


python parser.py --logfile friday-afternoon/london/logs/ip-172-31-28-168.eu-west-2.compute.internal.youtube.2019-10-18.13_01_40.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/london/logs/ip-172-31-28-168.eu-west-2.compute.internal.youtube.2019-10-18.13_07_49.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/london/logs/ip-172-31-28-168.eu-west-2.compute.internal.youtube.2019-10-18.13_12_54.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/london/logs/ip-172-31-28-168.eu-west-2.compute.internal.youtube.2019-10-18.13_17_01.pytomo.log --location USA --time AFT --day FRI

python parser.py --logfile friday-afternoon/london/logs/ip-172-31-28-168.eu-west-2.compute.internal.youtube.2019-10-18.13_21_13.pytomo.log --location USA --time AFT --day FRI
