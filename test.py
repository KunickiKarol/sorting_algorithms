from __future__ import print_function
import sys, os, argparse, time

def main(stat):   
    print(stat[1])
    

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument('--state', nargs=2)
   parser.add_argument('--stat', nargs=2)

   args = parser.parse_args()
   main(args.stat)