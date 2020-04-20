class Node:
    def __init__(self, linked_list, key):
        self.linked_list = linked_list
        self.key = key
        self.head = linked_list.head
        self.tail = linked_list.tail

class Min_Max_Heaps:
    def __init__(self):
        self.lists = []
        self.list_heads = [] #Min Heap
        self.list_tails = [] #Max Heap

    def insert(self, l):
        node = Node(l, len(self.lists))
        self.lists.append(l)
        self.list_heads.append(l.head)
        self.list_tails.append(l.tail)

        i = len(self.list_heads) - 1
        while i != 0 and (self.list_heads[(i-1) // 2]) > self.list_heads[i]:
            temp = self.list_heads[(i-1) // 2]
            self.heads[(i-1)//2] = self.list_heads[i]
            self.list_heads[i] = temp
            i = (i-1) // 2

        j = len(self.list_tails) - 1
        while i != 0 and self.list_tails[(i-1) // 2] < self.list_tails[i]:
            temp = self.list_heads[(i-1) // 2]
            self.heads[(i-1)//2] = self.list_heads[i]
            self.list_heads[i] = temp
            i = (i-1) // 2

    def remove_min(self):
        root = self.list_heads[0]
        if len(self.list_heads) == 0:
            return "Empty heap"
        i = 0
        #Downheap the root and then remove it
        while self.list_heads[2*i+1] != None or self.list_heads[2*i+2] != None:
            #Left Child Check
            if (self.list_heads[2*i+1] != None and self.list_heads[2*i+1] < root) or self.lists[2*1+1] < self.lists[2*i+2]:
                temp = self.list_heads[2*i+1]
                self.list_heads[2*i+1] = root
                self.list_heads[(i-1)//2] = temp
                i = 2*i+1
            #Right Child Check
            elif (self.list_heads[2*i+2] != None and self.list_heads[2*i+2] < root) or self.list_heads[2*1+2] < self.list_heads[2*i+1]:
                temp = self.list_heads[2*i+2]
                self.list_heads[2*i+2] = root
                self.list_heads[(i-1)//2] = temp
                i = 2*i+2
        
        temp2 = self.list[-1]
        self.list[i] = temp2
        root = self.list[-1]
        self.lists.pop()
        return root