def bubble_sort( theSeq ):
    for x in range(len(theSeq)):
        for y in range(len(theSeq) - 1):
            if theSeq[y].get_customer_name() > theSeq[y + 1].get_customer_name():
                theSeq[y], theSeq[y + 1] = theSeq[y + 1], theSeq[y]


def selection_sort( theSeq ): 
    n = len( theSeq ) 
 
    for i in range(n - 1): 
        smallNdx = i 

        for j in range(i+1, n): 
            if theSeq[j].get_package_name() < theSeq[smallNdx].get_package_name(): 
                smallNdx = j 
 
        if smallNdx != i: 
            tmp = theSeq[i] 
            theSeq[i] = theSeq[smallNdx] 
            theSeq[smallNdx] = tmp 


def insertion_sort( theSeq ): 
    n = len( theSeq ) 
 
    for i in range(1, n): 
        value = theSeq[i]
 
        pos = i 
        while pos > 0 and value.get_package_cost_per_pax() < theSeq[pos - 1].get_package_cost_per_pax(): 
            theSeq[pos] = theSeq[pos-1] 
            pos -= 1 
 
        theSeq[pos] = value 

def linear_search( theSeq, value, new_name ):
    for i in range(len(theSeq)):
        if theSeq[i].get_customer_name() == value:
            theSeq[i].set_customer_name(new_name)

            print(theSeq[i])

def binary_search( theValues, target, new_name ):
    low = 0
    high = len(theValues) - 1

    while low <= high:
        mid = int(high + low) // 2

        if target == theValues[mid].get_package_name():
            theValues[mid].set_package_name(new_name)

        elif target < theValues[mid].get_package_name():
            high = mid - 1

        else:
            low = mid + 1

    return theValues[mid]
