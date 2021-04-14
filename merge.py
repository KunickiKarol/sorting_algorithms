from tools import eprint


def merge_sort(array, comp, compare, changes):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        R = array[r:]

        merge_sort(L, comp, compare, changes)
        merge_sort(R, comp, compare, changes)

        i = j = k = 0

        if comp ==">=":
            while i < len(L) and j < len(R):
                compare.append(str(L[i]) + " < " + str(R[j]) + "?")
                eprint(compare[-1]) 
                if L[i] < R[j]:
                    changes.append(str(array[k]) + " = " + str(L[i]))
                    eprint(changes[-1])                      
                    array[k] = L[i]
                    i += 1
                else:
                    changes.append(str(array[k]) + " = " + str(R[j]))
                    eprint(changes[-1])                       
                    array[k] = R[j]
                    j += 1
                k += 1
        else:
            while i < len(L) and j < len(R):
                compare.append(str(L[i]) + " > " + str(R[j]) + "?")
                eprint(compare[-1]) 
                if L[i] > R[j]:
                    changes.append(str(array[k]) + " = " + str(L[i]))
                    eprint(changes[-1])                       
                    array[k] = L[i]
                    i += 1
                else:
                    changes.append(str(array[k]) + " = " + str(R[j]))
                    eprint(changes[-1])                       
                    array[k] = R[j]
                    j += 1
                k += 1                

        while i < len(L):
            changes.append(str(array[k]) + " = " + str(L[i]))
            eprint(changes[-1])               
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            changes.append(str(array[k]) + " = " + str(R[j]))
            eprint(changes[-1])                
            array[k] = R[j]
            j += 1
            k += 1  

def merge_sort_test(array):
    compare = changes = 0

    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        R = array[r:]

        new_compare, new_changes = merge_sort_test(L)
        compare += new_compare
        changes += new_changes
        new_compare ,new_changes = merge_sort_test(R)
        compare += new_compare
        changes += new_changes        

        i = j = k = 0

        while i < len(L) and j < len(R):
            compare += 1
            if L[i] < R[j]:
                changes +=1                      
                array[k] = L[i]
                i += 1
            else:
                changes +=1                      
                array[k] = R[j]
                j += 1
            k += 1
             

        while i < len(L):
            changes+=1              
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            changes+=1                
            array[k] = R[j]
            j += 1
            k += 1             
    return compare, changes