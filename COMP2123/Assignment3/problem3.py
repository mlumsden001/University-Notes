#This algorithm is designed to find the median of two sorted AVL trees containing only positive integers.
#The function find_node has a worst case time of O(log(n)) and the function median has a worst case time complexity of O(log(n)^2)
#Both algorithms assume that both AVL trees maintain AVL form via self-balancing techniques.

def find_node(k):
    count = 0
    if root == None:
        return "Empty tree"
    if root.left != None:
        return root.left
    count += 1

    if count == k:
        return root
    return find_node(root.right, k)


def median(A, B):
    median_point = (A.root.subtree_value + B.root.subtree_value + 1) / 2
    start = 0

    if A.root.subtree_value < B.root.subtree_value:
        while True:
            end = A.root.subtree_value
            partitionA = (end + start) / 2
            partitionB = median_point - partitionA

            if (A.find_node(partitionA - 1) <= B.find_node(partitionB)) and (B.find_node(partitionB - 1) <= A.find_node(partitionA)):
                return max(A.find_node(partitionA - 1), B.find_node(partitionB - 1))
            elif A.find_node(partitionA - 1) > B.find_node(partitionB):
                start = partitionA - 1
            else:
                start = partitionA + 1

    else:
        while True:
            end = B.root.subtree_value
            partitionB = (end + start) / 2
            partitionA = median_point - partitionB
            if (B.find_node(partitionB - 1) <= A.find_node(partitionA)) and (A.find_node(partitionA - 1) <= B.find_node(partitionB)):
                return max(A.find_node(partitionA - 1), B.find_node(partitionB - 1))
            elif B.find_node(partitionB - 1) > A.find_node(partitionA):
                start = partitionB - 1
            else:
                start = partitionB + 1