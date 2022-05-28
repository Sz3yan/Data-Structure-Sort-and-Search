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

class TreeNode(object): 
    def __init__(self, _val): 
        self.val = _val 
        self.left = None
        self.right = None
        self.height = 1
                
class AVL_Tree(object): 
    def insert(self, root, val):  
        #Simple Bst Insertion:
        if not root: 
            return TreeNode(val) 
        elif val < root.val: 
            root.left = self.insert(root.left, val) 
        else: 
            root.right = self.insert(root.right, val)
    
        # 2)modify the height      
        root.height = 1 + max(self.Height(root.left), self.Height(root.right)) 
        # 3)Get the Balancing Factor
        balance = self.check_Avl(root) 
        # 4)Balance The tree using required set of rotation
        
        #RR Rotation as tree is Left Skewed
        if balance > 1 and val < root.left.val: 
            return self.RR(root) 

        #LL Rotation as tree is Right Skewed
        if balance < -1 and val > root.right.val: 
            return self.LL(root) 
        #RL Rotation as tree is Left then Right Skewed
        if balance > 1 and val > root.left.val: 
            root.left = self.LL(root.left) 
            return self.RR(root) 
        #LR Rotation as tree is Right then Left Skewed
        if balance < -1 and val < root.right.val: 
            root.right = self.RR(root.right) 
            return self.LL(root) 

        return root 

    #LL Rotation
    def LL(self, node): 
        p = node.right 
        t = p.left
        #Rotations:
        p.left = node 
        node.right = t 
        #modify the heights: 
        node.height = 1 + max(self.Height(node.left), self.Height(node.right)) 
        p.height = 1 + max(self.Height(p.left), self.Height(p.right)) 

        return p 

    #LL Rotation
    def RR(self, node): 
        p = node.left 
        t = p.right
        #Rotations:
        p.right = node
        node.left = t 
        #modify the heights:
        node.height = 1 + max(self.Height(node.left), self.Height(node.right)) 
        p.height = 1 + max(self.Height(p.left), self.Height(p.right)) 
        return p 

    #Getting the Height
    def Height(self, root): 
        if not root: 
            return 0

        return root.height 

    #Getting the Balancing Factor
    def check_Avl(self, root): 
        if not root: 
            return 0

        return self.Height(root.left) - self.Height(root.right) 

    def preOrder(self, root): 
        if not root: 
            return

        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 

def insert_data(_data):
    mytree = AVL_Tree()
    root = None

    for i in _data:
        root = mytree.insert(root,i)

    print("Preorder Traversal of constructed AVL tree is:")
    mytree.preOrder(root)

    return root

def Search(root,val):
    if (root is None):
        return False

    elif (root.val == val):
        return True

    elif(root.val < val):
        return Search(root.right,val)

    return Search(root.left,val)