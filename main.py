# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def makeTree(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root


def searchTree(root):
    total_sum = 0
    queue = [root]
    next_queue = []

    while queue:
        for i in queue:
            total_sum += i.val
            print(i.val, end = ' ')
            next_queue += [x for x in [i.left, i.right] if x is not None]

        queue = next_queue[:]
        next_queue = []
        print('')

    # print(total_sum)
    
def subtreeWithAllDeepest(root):
    if root is None:
        return root

    node_binaries = {root.val : ''}
    queue = [root]

    while queue:
        node = queue.pop(0)

        l = node.left
        r = node.right 

        if l is not None:
            node_binaries[l.val] = node_binaries.get(node.val) + '0'
            queue.append(l)
        
        if r is not None:
            node_binaries[r.val] = node_binaries.get(node.val) + '1'
            queue.append(r)
        
    max_depth = max(list(map(len,node_binaries.values())))
    max_depth_binaries = [b for b in node_binaries.values() if len(b) == max_depth]


    first_diverse = 0
    for i in range(max_depth):
        values = set([b[i] for b in max_depth_binaries])

        if len(values) != 1:
            first_diverse = i
            break
    
    if len(max_depth_binaries) == 1:
        first_diverse = len(max_depth_binaries[0])

    search_node = root
    example_binary = max_depth_binaries[0]

    for i in range(first_diverse):
        
        if example_binary[i] == '0':
            search_node = search_node.left
        else:
            search_node = search_node.right

    return search_node
        




     

treeList = '[0,1,3,null,2]'
root = makeTree(treeList)
# searchTree(root)

subtree_node = subtreeWithAllDeepest(root)
searchTree(subtree_node)

######################################################################################################

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listNodeMaker(list):
    if len(list) == 0:
        return None
    
    root = ListNode(list[0])
    traveler = root

    for i in list[1:]:
        traveler.next = ListNode(i)
        traveler = traveler.next
    
    return root

def printListNode(root : ListNode):
    while root:
        print(root.val, end = ' ')
        root = root.next
    print('')

input_ListNode = [1,2,4]
# head = listNodeMaker(input_ListNode)
