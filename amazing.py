from tools import eprint


def amazing_sort(array, comp, compare, changes):
    if comp == ">=":
        amazing_sort_increasing(array, compare, changes, 0, len(array)-1)
    else:
        amazing_sort_descending(array, compare, changes, 0, len(array)-1)
    return


def amazing_sort_increasing(array, compare, changes, left, right):
        if left < right:
            if (right - left < 9):
                inserton_increasing(array, compare, changes, left, right + 1)
            else:
                partition_increasing(array, compare, changes, left, right)
                
                
def amazing_sort_descending(array, compare, changes, left, right):
    if left < right:
        if (right - left < 9):
            inserton_descending(array, compare, changes, left, right + 1)
        else:
            partition_descending(array, compare, changes, left, right)                
            
                        
def inserton_increasing(array, compare, changes, left, right):
        for x in range(left + 1, right):
            key = array[x]
            
            j = x - 1
            compare.append(str(key) + " < " + str(array[j]) + "?")
            eprint(compare[-1]) 
            while (j >= 0 and key < array[j]):
                changes.append(str(array[j + 1]) + " = " + str(j))   
                eprint(changes[-1])              
                array[j + 1] =array[j]
                j -=1
            changes.append(str(array[j + 1]) + " = " + str(key))   
            eprint(changes[-1])         
            array[j + 1] = key        
            
            
def inserton_descending(array, compare, changes, left, right):
        for x in range(left + 1, right):
            key = array[x]
            
            j = x - 1
            compare.append(str(key) + " > " + str(array[j]) + "?")
            eprint(compare[-1]) 
            while (j >= 0 and key > array[j]):
                changes.append(str(array[j + 1]) + " = " + str(j))   
                eprint(changes[-1])              
                array[j + 1] =array[j]
                j -=1
            changes.append(str(array[j + 1]) + " = " + str(key))   
            eprint(changes[-1])         
            array[j + 1] = key            
    
        
def partition_increasing(array, compare, changes, left, right):
    i = left - 1
    j = right + 1
        
    pivot = array[ (left + right) // 2 ]
    while (1):
        i+=1
        compare.append(str(pivot) + " > " + str(array[i]) + "?")
        eprint(compare[-1])              
        while(pivot > array[i]):
            i += 1
            compare.append(str(pivot) + " > " + str(array[i]) + "?")
            eprint(compare[-1])                  
        j -= 1
        compare.append(str(pivot) + " < " + str(array[j]) + "?")
        eprint(compare[-1])   
        while(pivot < array[j]):
            j -= 1
            compare.append(str(pivot) + " < " + str(array[j]) + "?")
            eprint(compare[-1])
        if (i <= j):
            changes.append(str(array[i]) + " swap " + str(array[j]))
            changes.append(str(array[j]) + " swap " + str(array[i]))
            eprint(changes[-1])                
            array[i], array[j] = array[j], array[i]
        else:
            break
            
    if (j > left): amazing_sort_increasing(array, compare, changes, left, j)
    if (i < right): amazing_sort_increasing(array, compare, changes, i, right)
    
    
def partition_descending(array, compare, changes, left, right):
    i = left - 1
    j = right + 1
        
    pivot = array[ (left + right) // 2 ]
    while (1):
        i+=1
        compare.append(str(pivot) + " < " + str(array[i]) + "?")
        eprint(compare[-1])              
        while(pivot < array[i]):
            i += 1
            compare.append(str(pivot) + " < " + str(array[i]) + "?")
            eprint(compare[-1])                  
            j -= 1
            compare.append(str(pivot) + " > " + str(array[j]) + "?")
            eprint(compare[-1])   
            while(pivot > array[j]):
                j -= 1
                compare.append(str(pivot) + " > " + str(array[j]) + "?")
                eprint(compare[-1])
            if (i <= j):
                changes.append(str(array[i]) + " swap " + str(array[j]))
                changes.append(str(array[j]) + " swap " + str(array[i]))
                eprint(changes[-1])                
                array[i], array[j] = array[j], array[i]
            else:
                break
            
    if (j > left): amazing_sort_descending(array, compare, changes, left, j)
    if (i < right): amazing_sort_descending(array, compare, changes, i, right)    
    
    
def amazing_sort_test(array, left, right):
    if left < right:
        if (right - left < 8):
            new_compare, new_changes = inserton_test(array, left, right + 1)
            compare = new_compare
            changes = new_changes
        else:
            new_compare, new_changes = partition_test(array, left, right)
            compare = new_compare
            changes = new_changes
    return compare, changes
            
            
def inserton_test(array, left, right):
    compare = changes = 0
    for x in range(left + 1, right):
        key = array[x]
        
        j = x - 1
        compare +=1
        while (j >= 0 and key < array[j]):
            changes +=1
            array[j + 1] =array[j]
            j -=1
        changes +=1    
        array[j + 1] = key
    return compare, changes         
        
        
def partition_test(array, left, right):
    compare = changes = 0
    i = left - 1
    j = right + 1
        
    pivot = array[ (left + right) // 2 ]
    while (1):
        i+=1
        compare += 1
        while(pivot > array[i]):
            i += 1
            compare += 1
        j -= 1
        compare += 1
        while(pivot < array[j]):
            j -= 1
            compare += 1
        if (i <= j):
            changes += 2
            array[i], array[j] = array[j], array[i]
        else:
            break
            
    if (j > left): 
        new_compare, new_changes = amazing_sort_test(array, left, j)
        compare += new_compare
        changes += new_changes
    if (i < right): 
        new_compare, new_changes = amazing_sort_test(array, i, right)  
        compare += new_compare
        changes += new_changes         
    return compare, changes       