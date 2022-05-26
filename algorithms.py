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

def linear_search( theSeq, value, new_name ):
    for i in range(len(theSeq)):
        if theSeq[i].get_customer_name() == value:
            theSeq[i].set_customer_name(new_name)

            print(theSeq[i])

def binary_search( theValues, target, new_name ):
    # Start with the entire sequence of elements
    low = 0
    high = len(theValues) - 1

    # Repeatedly subdivide the sequence in half
    # until the target is found
    while low <= high:
        # Find the midpoint of the sequence
        mid = int(high + low) // 2

        # Does the midpoint contain the target?
        # If yes, return midpoint (i.e. index of the list)
        if target == theValues[mid].get_package_name():
            theValues[mid].set_package_name(new_name)

        # Or is the target before the midpoint?
        elif target < theValues[mid].get_package_name():
            high = mid - 1

        # Or is the target after the midpoint?
        else:
            low = mid + 1

    # If the sequence cannot be subdivided further,
    # target is not in the list of values
    return theValues[mid]
