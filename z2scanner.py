#!/usr/bin/python
import argparse
import sys,os
from datetime import datetime

version = "0.0.1"

def check_md5(path):
    with open(path,'r') as f:
        value = f.read()
    f.close()
    if value[0:32] == '26cd7ef06f358bdb5bf20f109f41aead':
        return 'False',None
    else:
        return 'True',None

def print_output(path,result):
    cur = datetime.today().strftime("%Y-%m-%d %H-%M-%S")
    output="target path:%s\tscanner version:%s\tscan date:%s\tis malicious:%s\treason method:%s" % (path,version,cur,result[0],'' if result[1] is None else result[1])
    print(output)

def analyze(path):
    for subdir,dirs,files in os.walk(path):
        for f in files:
            filepath = subdir + os.sep + f
            print_output(filepath,check_md5(filepath))

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d',help='directory to analyze')
    args=parser.parse_args()
    analyze(args.d)

