#!/usr/bin/env python

import sys, getopt
import random

def main(argv):
    inputfile = 'wordlist.txt'
    num = 2
    n = 1
    try:
        opts, args = getopt.getopt(argv,"i:n:",["numwords="])
    except getopt.GetoptError:
        print('password.py -i <word list> -n <number of passwords> --numwords <number of words per password>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "--numwords":
            num = int(arg)
        elif opt == "-i":
            inputfile = arg
        elif opt == "-n":
            n = int(arg)

    list = open(inputfile,"r").read().split('\n')
    symbols = ["!","@","#","$","%","&","?"] 
    for n in range(n):
        password = ""
        for i in range(num):
            cap = random.randrange(0,num)
            idx = random.randrange(0,len(list))
            if random.choice([True, False]) or cap == i:
                password += list[idx].capitalize()
            else:
                password += list[idx]
            if i != num-1 or num == 1:
                number = random.randrange(100,1000)
                password += str(number)
        password += random.choice(symbols)
        print(password)

main(sys.argv[1:])
