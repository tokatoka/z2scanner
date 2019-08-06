#!/usr/bin/python
import argparse
import hashlib
import sys,os
from datetime import datetime

version = "0.0.1"
bad_md5 = '26cd7ef06f358bdb5bf20f109f41aead'

def check_hash(path):
    m = hashlib.md5()
    with open(path,'rb') as f:
        while True:
            data = f.read()
            if not data:
                break
            m.update(data)
    hashvalue = m.hexdigest()
    if hashvalue == bad_md5:
        return True,None
    else:
        return False,None

def print_output(path,result):
    cur = datetime.today().strftime("%Y-%m-%d %H-%M-%S")
    output="target path:%s\tscanner version:%s\tscan date:%s\tis malicious:%s\treason method:%s" % (path,version,cur,result[0],'' if result[1] is None else result[1])
    print(output)

def analyze(args):
    if args.d == True:
        for subdir,dirs,files in os.walk(args.fname):
            for f in files:
                filepath = subdir + os.sep + f
                print_output(filepath,check_hash(filepath))
    else:
        print_output(args.fname,check_hash(args.fname))

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fname',help='file to analyze')
    parser.add_argument('-d',help='directory to analyze',action='store_true')
    args=parser.parse_args()
    analyze(args)

