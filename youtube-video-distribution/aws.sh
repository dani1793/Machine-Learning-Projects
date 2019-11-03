#!/bin/bash

yum -y update

yum -y install python-pip rrdtool python-rrdtool gcc

pip install web.py==0.40 pytomo 


