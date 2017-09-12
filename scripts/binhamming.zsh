#!/bin/zsh

#run a binary string from command line arguments, which defaults to 0101, through the encoder, error generator, and decoder

echo ${1:=0101} | python ../hamming/SEC_encode.py | python ../hamming/make_error.py | python ../hamming/SEC_decode.py
