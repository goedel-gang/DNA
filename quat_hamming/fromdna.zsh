#!/bin/zsh

#a program to convert a base 4 number to DNA

while read line; do
	echo $line | sed -e 's/a/0/g' -e 's/c/1/g' -e 's/g/2/g' -e 's/t/3/g';
done
