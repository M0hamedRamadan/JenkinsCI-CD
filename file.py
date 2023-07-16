#!/bin/python3.10
import subprocess
print("Hi, This is a script.py to create number of Dirs that user entered")
subprocess.run(['pwd'])
number=int(input("Enter number of Directories: "))
start=1
for loop in range (start,number+1):
    print (f"entered loop number: {loop}")
    subprocess.run(['mkdir', f'Dir{loop}'])
subprocess.run(['ls'])
