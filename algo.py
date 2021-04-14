from __future__ import print_function
import sys, argparse, time
from dual import dual_pivot_sort
from amazing import amazing_sort
from insertion import  insertion_sort
from merge import merge_sort
from quick import quick_sort
from research import research   
from tools import eprint, safe_cast

def main(stat, kind, comp):   
    if stat:
        research(stat[0], stat[1])
    else:        
        if comp != '<=' and comp != '>=': sys.exit("sth wrong comp")
        if (kind == 'insert' or kind == 'merge' or kind =='quick' or
                kind == 'dual'or kind == 'amazing'):
            ask(kind, comp)
        else:
            sys.exit("sth wrong donna know kind")
   
               
def ask(kind, comp): 
    compare = []
    changes = []
    n = safe_cast(input ())
    if n < 1: sys.exit("sth wrong less than 1 n")

    array = input ()
    array = array.split(" ")
    if  len(array) != n: sys.exit("sth wrong len")
    print("Is is str/int? (Write str or int)")
    how = input ()
    if how == "int":
        array = [safe_cast(x) for x in array]
    old_array = array.copy()

    
    if kind == "insert":
        start = time.time()
        insertion_sort(array, comp, compare, changes)
    elif kind == "quick":
        start = time.time()
        quick_sort(array, comp, compare, changes, 0, len(array)-1)
    elif kind == "dual":
        start = time.time()
        dual_pivot_sort(array, comp, compare, changes)
    elif kind == "amazing":
        start = time.time()
        amazing_sort(array, comp, compare, changes)          
    else:
        start = time.time()
        merge_sort(array, comp, compare, changes)
    end = time.time()
    clock = end-start    
    print("*" * 40)
    eprint("Compared " + str(len(compare)))
    eprint("Changed " + str(len(changes))  )
    eprint("Total time " + str(clock))
    print("Old one")
    print(old_array)
    print("New one " + comp)
    print(array)
    if comp == ">=" and array == sorted(old_array): 
        print("Well sorted")
    elif comp=="<="and array ==sorted(old_array, reverse=True):
        print("Well sorted")
    else:
        print("Wrongly sorted")


if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument('--type', action="store", type=str)
   parser.add_argument('--comp', action="store", type=str)
   parser.add_argument('--stat', nargs=2)

   args = parser.parse_args()
   main(args.stat, args.type, args.comp)
   
   
