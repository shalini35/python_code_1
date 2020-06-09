
class Node: 
	# node class 
	def __init__(self, data): 
		self.data = data
		self.left = None
		self.right = None

# Finds the distance from root node to given root of the tree. 
# Stores the distance in a list distance[], returns true if distance 
# exists otherwise false 
def findDistance( root, distance, k): 

	# Baes Case 
	if root is None: 
		return False

	# Store this node is distance vector. The node will be 
	# removed if not in distance from root to k 
	distance.append(root.data) 

	# See if the k is same as root's key 
	if root.data == k : 
		return True

	# Check if k is found in left or right sub-tree 
	if ((root.left != None and findDistance(root.left, distance, k)) or
			(root.right!= None and findDistance(root.right, distance, k))): 
		return True

	# If not present in subtree rooted with root, remove 
	# root from distance and return False 
	
	distance.pop() 
	return False

# Returns Common_parents if node n1 , n2 are present in the given 
# binary tre otherwise return -1 
def find_common_parents(root, n1, n2): 

	# To store distances to n1 and n2 fromthe root 
    distance1 = [] 
    distance2 = [] 

	# Find distances from root to n1 and root to n2. 
	# If either n1 or n2 is not present , return -1 
    if (not findDistance(root, distance1, n1) or not findDistance(root, distance2, n2)): 
        return -1

    common_parents = []
    for i in range(len(distance1)):
        if distance1[i] in distance2:
            if distance1[i] not in [n1,n2]:
                common_parents.append(distance1[i])
        
    return common_parents[-2:]

root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)

print("Common_parents(4, 5) = ", find_common_parents(root, 1, 5,)) 
print("Common_parents(4, 6) = ",find_common_parents(root, 3, 6)) 
print("Common_parents(3, 4) = ",find_common_parents(root,4,6)) 


