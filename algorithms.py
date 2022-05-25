def bubble_sort( theSeq ):
    for x in range(len(theSeq)):
        for y in range(len(theSeq) - 1):
            if theSeq[y].get_customer_name() > theSeq[y + 1].get_customer_name():
                theSeq[y], theSeq[y + 1] = theSeq[y + 1], theSeq[y]


def selection_sort( theSeq ): 
    n = len( theSeq ) 
 
    for i in range(n - 1): 
        # Assume the ith element is the smallest. 
        smallNdx = i 
        # Determine if any other element contains a smaller value. 
        for j in range(i+1, n): 
            if theSeq[j].get_package_name() < theSeq[smallNdx].get_package_name(): 
                smallNdx = j 
 
        # Swap the ith value and smallNdx value only if the 
        # smallest value is not already in its proper position. 
        if smallNdx != i: 
            tmp = theSeq[i] 
            theSeq[i] = theSeq[smallNdx] 
            theSeq[smallNdx] = tmp 


def insertion_sort( theSeq ): 
    n = len( theSeq ) 
 
    # Starts with the first item as the only sorted entry. 
    for i in range(1, n): 
        # Save the value to be positioned 
        value = theSeq[i]
 
        # Find the position where value fits in the 
        # ordered part of the list. 
        pos = i 
        while pos > 0 and value.get_package_cost_per_pax() < theSeq[pos - 1].get_package_cost_per_pax(): 
            # Shift the items to the right during the search 
            theSeq[pos] = theSeq[pos-1] 
            pos -= 1 
 
        # Put the saved value into the open slot. 
        theSeq[pos] = value 

def linear_search( theSeq, value ):
    for i in range(len(theSeq)):
        if theSeq[i] == value:
            return i
    return -1


def binary_search( theSeq, value ):
    low = 0
    high = len(theSeq) - 1
    while low <= high:
        mid = (low + high) // 2
        if theSeq[mid] == value:
            return mid
        elif theSeq[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
