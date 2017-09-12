#!/bin/zsh

#sieve in zsh, outputting only dna barcoded in a specified range of temperatures from oligotm. not in use, see dna/oligotm/oracle.py

while read line; do
	temp=$(oligotm "$line")

	if [[ ( $temp -gt $1 ) && ( $temp -lt $2 ) ]]; then
		echo "$line" $temp;
	fi

done
