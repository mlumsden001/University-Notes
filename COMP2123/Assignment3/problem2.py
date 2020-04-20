class Node:
    def __init__(self, linked_list):
        self.linked_list = linked_list
        count = 0
        for i in self.linked_list:
            count = count + 1
        self.key = count

#n = k(key)

class ArrayHeap:
    def __init__(self, k):
        self.k = k
        self.lists = []
        self.size = len(self.lists)
        self.n = 0

    #Left child = 2i + 1
    #Right child = 2i + 2
    #Parent = [(i-1) // 2]

    def insert(self, l):
        if self.size == self.k:
            return "No more space"
        else:
            node = Node(l)
            self.lists.append(node)
            self.n += node.key
            i = self.size - 1
            #Upheap
            while i != 0 and (self.lists[(i-1)//2]).key > (self.lists[i]).key:
                temp = self.lists[(i-1)//2]
                self.lists[(i-1)//2] = self.lists[i]
                self.lists[i] = temp
                i = (i-1) // 2

    def remove_min(self):
        root = self.lists[0]
        if self.size == 0:
            return "Empty heap"
        i = 0
        #Downheap the root and then remove it
        while self.lists[2*i+1] != None or self.lists[2*i+2] != None:
            #Left Child Check
            if (self.lists[2*i+1] != None and (self.lists[2*i+1]).key < root.key) or (self.lists[2*1+1]).key < (self.lists[2*i+2]).key:
                temp = self.lists[2*i+1]
                self.lists[2*i+1] = root
                self.lists[(i-1)//2] = temp
                i = 2*i+1
            #Right Child Check
            elif (self.lists[2*i+2] != None and (self.lists[2*i+2]).key < root.key) or (self.lists[2*1+2]).key < (self.lists[2*i+1]).key:
                temp = self.lists[2*i+2]
                self.lists[2*i+2] = root
                self.lists[(i-1)//2] = temp
                i = 2*i+2
        temp2 = self.list[-1]
        self.list[i] = temp2
        root = self.list[-1]
        self.lists.pop()
        return root

    def remove_max(self):
        if self.size == 0:
            return "Empty heap"
        else:
            max_node = self.lists[self.size // 2]
            for i in range(1 + self.size//2), self.size):
                max_node = max(max_node, self.lists[i])
            self.lists.remove(max_node)
            return max_node





tree = ArrayHeap(5)
A = [1, 2, 3, 4]
tree.insert(A)
print(tree.print_data)
tree.remove_min()
print(tree.print_data())