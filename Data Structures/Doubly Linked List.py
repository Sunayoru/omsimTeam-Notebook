class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
        self.prev = None  
    def get_data(self):
        return self.data
class Sentinel_DLL:
    def __init__(self):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
    def first_node(self):
        if self.sentinel.next == self.sentinel:
            return None
        else:
            return self.sentinel.next
    def insert_after(self, x, data):
        y = Node(data)  
        y.prev = x
        y.next = x.next
        x.next = y
        y.next.prev = y
    def append(self, data):
        last_node = self.sentinel.prev
        self.insert_after(last_node, data)
    def prepend(self, data):
        self.insert_after(self.sentinel, data)
    def delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
    def find(self, data):
        self.sentinel.data = data
        x = self.first_node()
        while x.data != data:
            x = x.next
        self.sentinel.data = None
        if x == self.sentinel:
            return None 
        else:
            return x   
    def __str__(self):
        s = "["
        x = self.sentinel.next
        while x != self.sentinel:  
            if type(x.data) == str:
                s += "'"
            s += str(x.data)  
            if type(x.data) == str:
                s += "'"
            if x.next != self.sentinel:
                s += ", "
            x = x.next

        s += "]"
        return s
#test
llist = Sentinel_DLL()
llist.append(5)
llist.append(6)
llist.append(2)
llist.prepend(19)
print(llist)
#insert_after = insert a new node with data after node x
#append = insert new node at end of list
#prepend = insert a new node at the start of the list
#delete = delete node x
#find = finds x (note: O(n) )
