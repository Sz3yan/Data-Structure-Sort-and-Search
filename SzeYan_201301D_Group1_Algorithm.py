

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
        if theSeq[i].get_customer_name().upper() == value:
            theSeq[i].set_customer_name(new_name)


def binary_search( theValues, target, new_name ):
    low = 0
    high = len(theValues) - 1

    while low <= high:
        mid = int(high + low) // 2

        if target == theValues[mid].get_package_name().upper():
            theValues[mid].set_package_name(new_name)

        elif target < theValues[mid].get_package_name().upper():
            high = mid - 1

        else:
            low = mid + 1

    return theValues[mid]

# Bonus Feature

# AVL Tree
# Height Balance Binary Tree. 
# AVL tree prevents it from becoming skewed. 
# Because when a binary tree becomes skewed, it is the worst case (O (n)) for all the operations. 
# By using the balance factor, AVL tree imposes a limit on the binary tree and thus keeps all the operations at O(log n).

# It helps it system to minise the time complexity, which enables them to manage the records better. 
# references: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/ 
#             https://www.youtube.com/watch?v=jDM6_TnYIqE 

# always check from the root. if node > root, go right. if node < root, go left.
# Balance factor = height of left subtree - height of right subtree = {-1,0,1}

# if balance factor is not -1,0,1, then tree is unbalanced. we need to balance it by doing rotation
# perform 2 rotations if balance factor is -2 or 2 (LR or RL)
# rotation only occurs on 3 nodes

# for example: if we have a tree like this: 
#       x   (take longest distance of left and right = 2 - 2 = 0)     y   (3 - 1 = 2) -> imbalance
#     / \                                                            / \
#    x  x  (1 - 0 = 1) ; (1 - 1 = 0)                                y  y
#   /  /                                                             \
#  x   x   (0 - 0 = 0) ; (0 - 0 = 0)                                 y
#                                                                   /                                                    
#                                                                  y


#  initially we have:                                                               After LL Rotation:
#      30     then insert 10, we have:   30 (2) (left of left LL imbalance)             20
#     /                                 /                                              /  \
#   20                                20 (1)                                         10   30
#                                    /
#                                  10 (0)


#  initially we have:                                                               After LR Rotation:
#      30     then insert 20, we have:   30 (2)     (LR imbalance)                 30               20
#     /                                 /                                         /                /  \
#   10                                10 (-1)                                   20        =>     10   30
#                                       \                                      /
#                                       20 (0)                                10
#
# for LR imbalance, we need to do a LR rotation => directly move C to the root then move root to right 


#  initially we have:                                                               After RR Rotation:
#      10     then insert 30, we have:   10 (-2)     (RR imbalance)                  20              
#        \                                 \                                        /  \            
#        20                                 20 (-1)                               10   30  
#                                            \                                      
#                                             30 (0)                                
# 
# 
#  initially we have:                                                               After RL Rotation:
#      10     then insert 20, we have:   10 (-2)     (RL imbalance)                 10               20
#        \                                 \                                          \             /  \
#        30                                30 (1)                                     20     =>    10   30
#                                         /                                            \
#                                       20 (0)                                         30
# for RL imbalance, we need to do a RL rotation => directly move C to the root then move root to left 


# Suppose that we have a tree like this: 
# where l = left child. r= right child. we dk the number 
#
#                 A            then there's a LL insertion, making it unbalanced:
#               /  \           to balance it, we need to do a LL rotation =>            B
#              B    Ar                                                                /    \
#             / |                                                                    C      A
#            C  Br                                                                  / \     / \
#           / \                                                                    Cl  Cr  Bl  Ar
#          Cl  Cr
# 
# 

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

    def Height(self, root): 
        if not root: 
            return 0

        return root.height 

    #Getting the Balancing Factor
    def check_Avl(self, root): 
        if not root: 
            return 0

        return self.Height(root.left) - self.Height(root.right) 

def insert_data(_data):
    mytree = AVL_Tree()
    root = None

    for i in _data:
        root = mytree.insert(root,i)

    return root

def Search(root,val):
    if (root is None):
        return False

    elif (root.val == val):
        return True

    elif(root.val < val):
        return Search(root.right,val)

    return Search(root.left,val)