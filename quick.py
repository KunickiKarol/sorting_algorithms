from tools import eprint


def quick_sort(array, comp, compare, changes, left, right):
    if(right > left):
        i = left - 1
        j = right + 1
        
        pivot = array[ (left + right) // 2 ]
        if comp == ">=":
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
        else:
                while (1):
                    i+=1
                    compare.append(str(pivot) + " < " + str(array[i]) + "?")
                    eprint(compare[-1])              
                    while(pivot < array[i]):
                        i += 1
                        compare.append(str(pivot) + " < " + 
                                       str(array[i]) + "?")
                        eprint(compare[-1])                  
                    j -= 1
                    compare.append(str(pivot) + " > " + str(array[j]) + "?")
                    eprint(compare[-1])   
                    while(pivot > array[j]):
                        j -= 1
                        compare.append(str(pivot) + " > " + 
                                       str(array[j]) + "?")
                        eprint(compare[-1])
                    if (i <= j):
                        changes.append(str(array[i]) + " swap " + 
                                       str(array[j]))
                        changes.append(str(array[j]) + " swap " + 
                                       str(array[i]))
                        eprint(changes[-1])                
                        array[i], array[j] = array[j], array[i]
                    else:
                        break
            
        if (j > left): quick_sort(array, comp, compare, changes, left, j)
        if (i < right): quick_sort(array, comp, compare, changes, i, right)
        
def quick_sort_test(array, left, right):
    compare = changes = 0
    if(right > left):
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

        new_compare = new_changes = 0
        if (j > left): 
            new_compare, new_changes = quick_sort_test(array, left, j)
            compare += new_compare
            changes += new_changes
        if (i < right): 
            new_compare, new_changes = quick_sort_test(array, i, right)  
            compare += new_compare
            changes += new_changes         
    return compare, changes