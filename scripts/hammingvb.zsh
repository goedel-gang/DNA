#!/bin/zsh

#run an ascii string from command line arguments, which defaults to abcdefg, through the whole lot

echo ${1:=abcdefg} | python ../hamming/ascii_to_binary.py | python ../hamming/SEC_encode.py | python ../hamming/make_error.py | python ../hamming/SEC_decode.py | python ../hamming/binary_to_ascii.py
