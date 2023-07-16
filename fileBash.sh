#!/bin/bash
pwd
read -p "Enter number of directories: " number
for iteration in $(seq 1 $number):
do
	mkdir Dir$iteration
done
ls
