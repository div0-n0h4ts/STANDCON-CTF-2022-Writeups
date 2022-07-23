#!/bin/bash

filename=flag
file $filename

while [ 1 ]
do
	file $filename | grep "ASCII"
	if [ "$?" -eq "0" ]
	then
		tail -c 100 $filename
		base64 -d $filename > $filename.new
		mv $filename.new $filename
	fi

	file $filename | grep "gzip"

	if [ "$?" -eq "0" ]
	then
		echo "gzip"
		mv $filename $filename.gz
		gzip -d $filename

	fi

	file $filename | grep "bzip2"
	if [ "$?" -eq "0" ]
	then
		echo "bzip2"
		bzip2 -d $filename
		mv $filename.out $filename

	fi

	file $filename | grep "Zip"
	if [ "$?" -eq "0" ]
	then
		echo "zip"
		mv $filename $filename.zip
		unzip $filename
		rm $filename.zip
	fi

	file $filename | grep "empty"
	if [ "$?" -eq "0" ]
	then
		break
	fi
done