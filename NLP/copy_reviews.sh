!/bin/bash

clear

echo "starting copy of files from $1 to $2"
for file in $1; do cp -r $file $2; done 
echo "copy complete"
