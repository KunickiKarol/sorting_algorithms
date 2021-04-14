from tools import eprint

def dual_pivot_sort(array, comp, compare, changes):
    if comp == ">=":
        dual_pivot_sort_increasing(array, compare, changes, 0, len(array)-1)
    else:
        dual_pivot_sort_descending(array, compare, changes, 0, len(array)-1)
    return
    

def dual_pivot_sort_increasing(array, compare, changes, left, right):
    if right <= left:
        return
    compare.append(str(array[right]) + " < " + str(array[left]) + "?")
    eprint(compare[-1])
    if array[right] < array[left]:
        changes.append(str(array[left]) + " swap " + str(array[right]))
        changes.append(str(array[left]) + " swap " + str(array[right])) 
        eprint(changes[-1])
        array[right], array[left] = array[left], array[right]
    p = array[left]
    q = array[right]
    i = left + 1
    k = right - 1
    j = i
    d = 0
    while j <= k:
        eprint(j, k)
        if d >= 0:
            compare.append(str(array[j]) + " < " + str(p) + "?")
            eprint(compare[-1])
            if array[j] < p:
                changes.append(str(array[i]) + " swap " + str(array[j]))
                changes.append(str(array[i]) + " swap " + str(array[j]))   
                eprint(changes[-1])                
                array[i], array[j] = array[j], array[i]
                i += 1
                j += 1
                d += 1
            else:
                compare.append(str(array[j]) + " < " + str(q) + "?")
                eprint(compare[-1])
                if array[j] < q:
                    j+= 1
                else:
                    changes.append(str(array[j]) + " swap " + str(array[k]))
                    changes.append(str(array[j]) + " swap " + str(array[k]))
                    eprint(changes[-1])
                    array[j], array[k] = array[k], array[j]
                    k -= 1
                    d -= 1
        else:
            compare.append(str(array[k]) + " > " + str(q) + "?")
            eprint(compare[-1])
            if array[k] > q:
                k -= 1
                d -= 1
            else:
                compare.append(str(array[k]) + " < " + str(p) + "?")
                eprint(compare[-1])
                if array[k] < p:

                    changes.append("rot3 left " + str(array[k]) + " <- " + 
                                       str(array[j]) + " <- " + 
                                       str(array[i]) + " <-")
                    changes.append("rot3 left " + str(array[k]) + " <- " + 
                                       str(array[j]) + " <- " + 
                                       str(array[i])  + " <-")
                    changes.append("rot3 left " + str(array[k]) + " <- " + 
                                       str(array[j]) + " <- " + 
                                       str(array[i]) + " <-")
                    eprint(changes[-1])                    
                    array[k], array[j], array[i] = array[j], array[i], array[k]
                    i += 1
                    d += 1
                else:
                    changes.append(str(array[j]) + " swap " + str(array[k]))
                    changes.append(str(array[j]) + " swap " + str(array[k]))
                    eprint(changes[-1])                    
                    array[j], array[k] = array[k], array[j]
                j += 1
                
    changes.append(str(array[left]) + " swap " + str(array[i - 1]))
    changes.append(str(array[left]) + " swap " + str(array[i - 1]))
    eprint(changes[-1])
    changes.append(str(array[right]) + " swap " + str(array[k + 1]))
    changes.append(str(array[right]) + " swap " + str(array[k + 1]))
    eprint(changes[-1])
              
    array[left], array[i - 1] = array[i - 1], array[left]
    array[right], array[k + 1] = array[k + 1], array[right]
    dual_pivot_sort_increasing(array, compare, changes, left, i-2)
    dual_pivot_sort_increasing(array, compare, changes, i, k)
    dual_pivot_sort_increasing(array, compare, changes, k + 2, right)
    
    
def dual_pivot_sort_descending(array, compare, changes, left, right):
    if right <= left:
        return
    compare.append(str(array[right]) + " > " + str(array[left]) + "?")
    eprint(compare[-1])
    if array[right] > array[left]:
        changes.append(str(array[left]) + " swap " + str(array[right]))
        changes.append(str(array[left]) + " swap " + str(array[right])) 
        eprint(changes[-1])
        array[right], array[left] = array[left], array[right]
    p = array[left]
    q = array[right]
    k = left + 1
    i = right - 1
    j = i
    d = 0
    while j >= k:
        if d >= 0:
            compare.append(str(array[j]) + " < " + str(q) + "?")
            eprint(compare[-1])
            if array[j] < q:
                changes.append(str(array[i]) + " swap " + str(array[j]))
                changes.append(str(array[i]) + " swap " + str(array[j]))   
                eprint(changes[-1])                
                array[i], array[j] = array[j], array[i]
                i -= 1
                j -= 1
                d += 1
            else:
                compare.append(str(array[j]) + " < " + str(p) + "?")
                eprint(compare[-1])
                if array[j] < p:
                    j-= 1
                else:
                    changes.append(str(array[j]) + " swap " + str(array[k]))
                    changes.append(str(array[j]) + " swap " + str(array[k]))
                    eprint(changes[-1])
                    array[j], array[k] = array[k], array[j]
                    k += 1
                    d -= 1
        else:
            compare.append(str(array[k]) + " < " + str(p) + "?")
            eprint(compare[-1])
            if array[k] > p:
                k += 1
                d -= 1
            else:
                compare.append(str(array[k]) + " > " + str(p) + "?")
                eprint(compare[-1])
                if array[k] < q:

                    changes.append("rot3 left " + str(array[k]) + " <- " + 
                                       str(array[j]) + " <- " + 
                                       str(array[i]) + " <-")
                    changes.append("rot3 left " + str(array[k]) + " <- " + 
                                       str(array[j]) + " <- " + 
                                       str(array[i])  + " <-")
                    changes.append("rot3 left " + str(array[k]) + " <- " + 
                                       str(array[j]) + " <- " + 
                                       str(array[i]) + " <-")
                    eprint(changes[-1])                    
                    array[k], array[j], array[i] = array[j], array[i], array[k]
                    i -= 1
                    d += 1
                else:
                    changes.append(str(array[j]) + " swap " + str(array[k]))
                    changes.append(str(array[j]) + " swap " + str(array[k]))
                    eprint(changes[-1])                    
                    array[j], array[k] = array[k], array[j]
                j -= 1
                
    changes.append(str(array[right]) + " swap " + str(array[i + 1]))
    changes.append(str(array[right]) + " swap " + str(array[i + 1]))
    eprint(changes[-1])
    changes.append(str(array[left]) + " swap " + str(array[k - 1]))
    changes.append(str(array[left]) + " swap " + str(array[k - 1]))
    eprint(changes[-1])
              
    array[right], array[i + 1] = array[i + 1], array[right]
    array[left], array[k - 1] = array[k - 1], array[left]
    dual_pivot_sort_descending(array, compare, changes, left, k-2)
    dual_pivot_sort_descending(array, compare, changes, k, i)
    dual_pivot_sort_descending(array, compare, changes, i + 2, right)
     
    
def dual_pivot_sort_test(array, left, right):
    if right <= left:
        return 0, 0
    
    compare = changes = 0
    compare += 1
    if array[right] < array[left]:
        changes += 2
        array[right], array[left] = array[left], array[right]
        
    p = array[left]
    q = array[right]
    i = left + 1
    k = right - 1
    j = i
    d = 0
    while j <= k:
        if d >= 0:
            compare += 1
            if array[j] < p:
                changes += 2
                array[i], array[j] = array[j], array[i]
                i += 1
                j += 1
                d += 1
            else:
                compare += 1
                if array[j] < q:
                    j+= 1
                else:
                    changes += 2
                    array[j], array[k] = array[k], array[j]
                    k -= 1
                    d -= 1
        else:
            compare += 1
            if array[k] > q:
                k -= 1
                d -= 1
            else:
                compare += 1
                if array[k] < p:
                    changes += 3
                    array[k], array[j], array[i] = array[j], array[i], array[k]
                    i += 1
                    d += 1
                else:
                    changes += 2
                    array[j], array[k] = array[k], array[j]
                j += 1
                
    changes += 2
    array[left], array[i - 1] = array[i - 1], array[left]
    changes += 2
    array[right], array[k + 1] = array[k + 1], array[right]
    
    new_compare = new_changes = 0  
    
    new_compare, new_changes = dual_pivot_sort_test(array, left, i-2)
    compare += new_compare
    changes += new_changes
    
    new_compare, new_changes = dual_pivot_sort_test(array, i, k)
    compare += new_compare
    changes += new_changes
    
    new_compare, new_changes = dual_pivot_sort_test(array, k + 2, right)    
    compare += new_compare
    changes += new_changes 
    
    return compare, changes