import numpy as np
import time, json
from tools import safe_cast
from amazing import amazing_sort_test
from insertion import  insertion_sort_test
from merge import merge_sort_test
from quick import quick_sort_test
from dual import  dual_pivot_sort_test


def research(file_name, repeat):
    repeat =safe_cast(repeat)
    all_results = []
    compare = 0
    changes = 0   
    for n in range(100, 10100, 100):
        print(n)
        for k in range(repeat):
            testing_array = np.random.randint(0, 1000, n)
            
            array_copy = testing_array.copy()
            compare = 0
            changes = 0
            start = time.time()
            compare, changes = insertion_sort_test(array_copy)
            end = time.time()
            clock = end-start 
            results = {"name": "insert",
                       "amount": n,
                       "compare": compare,
                       "changes": changes,
                       "time": clock
                       }
            all_results.append(results)
            
            array_copy = testing_array.copy()
            compare = 0
            changes = 0
            start = time.time()
            compare, changes = merge_sort_test(array_copy)
            end = time.time()
            clock = end-start 
            results = {"name": "merge",
                       "amount": n,
                       "compare": compare,
                       "changes": changes,
                       "compare": compare,
                       "changes": changes,
                       "time": clock
                       }
            all_results.append(results)
            
            array_copy = testing_array.copy()                
            compare = 0
            changes = 0
            start = time.time()
            compare, changes = quick_sort_test(array_copy, 0 , 
                                               len(testing_array)-1)
            end = time.time()
            clock = end-start 
            results = {"name": "quick",
                       "amount": n,
                       "compare": compare,
                       "changes": changes,
                       "time": clock
                       }
            all_results.append(results)
            
            array_copy = testing_array.copy()
            compare = 0
            changes = 0
            start = time.time()
            compare, changes = dual_pivot_sort_test(array_copy, 0 , 
                                                    len(testing_array)-1)
            end = time.time()
            clock = end-start 
            results = {"name": "dual",
                       "amount": n,
                       "compare": compare,
                       "changes": changes,
                       "time": clock
                       }
            all_results.append(results)
            
            array_copy = testing_array.copy()
            compare = 0
            changes = 0
            start = time.time()
            compare, changes = amazing_sort_test(array_copy, 0 , 
                                                 len(testing_array)-1)
            end = time.time()
            clock = end-start 
            results = {"name": "amazing",
                       "amount": n,
                       "compare": compare,
                       "changes": changes,
                       "time": clock
                       }
            all_results.append(results) 
    try:
        file = open(file_name, "w")
        json.dump(all_results, file, indent=4) 
    except IOError:
        pass
    finally:
        file.close()                         
