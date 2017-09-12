#!/bin/zsh

#a program to convert a base 4 number to DNA

while read line; do
	echo $line | sed -e 's/0/a/g' -e 's/1/c/g' -e 's/2/g/g' -e 's/3/t/g';
done
