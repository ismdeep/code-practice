#!/bin/bash
min=1
max=100
while [ $min -le $max ]
do
    # echo $min
    python3 random-generator.py $min | python3 cross-cnt-diff.py
    min=`expr $min + 1`
done
