#!/bin/bash
val1=11
val2=12

if [ $val1 -gt 5 ]
then 
    echo "the test value val1 is greater than 5"
fi

if [ $val1 -eq $val2 ]
then 
    echo "the values are equal"
else
    echo "the values are diff"
fi
