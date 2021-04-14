from tools import eprint


def insertion_sort(array, comp, compare, changes):
    if comp == ">=":
        for i in range(1, len(array)):
     
            key = array[i]
     
            j = i-1
            
            compare.append(str(key) + " < " + str(array[j]) + "?")
            eprint(compare[-1])            
            while j >= 0 and key < array[j] :
                    changes.append(str(array[j + 1]) + " = " + str(array[j]))
                    eprint(changes[-1])
                    array[j + 1] = array[j]

                    j -= 1
                    if j >= 0:
                        compare.append(str(key) + " < " + str(array[j]) + "?")
                        eprint(compare[-1])  
            if not (array[j + 1] is key): 
                changes.append(str(array[j + 1]) + " = " + str(key))
                eprint(changes[-1])           
            array[j + 1] = key

    else:
        for i in range(1, len(array)):
     
            key = array[i]
     
            j = i-1
            
            compare.append(str(key) + " > " + str(array[j]) + "?")
            eprint(compare[-1]) 
            while j >= 0 and key > array[j] :
                    changes.append(str(array[j + 1]) + " = " + str(array[j]))
                    eprint(changes[-1])                
                    array[j + 1] = array[j]
                    j -= 1
                    if j >= 0:
                        compare.append(str(key) + " > " + str(array[j]) + "?")
                        eprint(compare[-1]) 
            if not (array[j + 1] is key): 
                changes.append(str(array[j + 1]) + " = " + str(key))
                eprint(changes[-1])                      
            array[j + 1] = key
            
def insertion_sort_test(array):
    compare = changes = 0
    
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        
        compare += 1
        while j >= 0 and key < array[j] :
                changes += 1

                array[j + 1] = array[j]

                j -= 1
                if j >= 0:
                    compare += 1

        if not (array[j + 1] is key): 
            changes += 1

        array[j + 1] = key

    return compare, changes