
"""
def print_items(n):
    for i in range(n):
        for j in range(n):
        
            print (i,j)

    for k in range(n):
        print(k)
       

print_items(10)
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList : 
    def __init__(self,value):
        new_node =Node(value)
        self.head = new_node
        self.tail = new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node= Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail=new_node
        self.length += 1   

    def pop(self):
        
        if self.length ==0 :
            return None
        
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp=temp.next
        self.tail = pre   
        self.tail.next = None 

        self.length -= 1

        if self.length == 0 :
            self.head = None 
            self.tail = None 
        return temp.value
    
    def prepend(self,value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else :
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True     
    
    def pop_first(self):

        if self.length == 0 :
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next == None 
        self.length -= 1

        if self.length == 0 :
            self.tail = None

        return temp   
     
    def get(self,index):
        if index < 0 or index >= self.length :
            return None
        
        temp = self.head 
        for _ in range (index) :
            temp = temp.next 

        return temp  
    
    def set (self, index , value ):
        
        temp = self.get(index)
        if temp:
            temp.value = value 
            return True 
        return False 
    
    def insert (self , index,value ) :

        if index == 0:
            return self.prepend(value)
        
        if index == self.length :
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)

        new_node.next = temp.next
        temp.next = new_node

        self.length =+ 1

        return True
    
    def remove(self,index):

        if index < 0 or index >= self.length :
            return None
        
        if index == 0 :
            return self.pop_first()
        
        if index == self.length :
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None
        self.length -= 1

        return temp.value
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range (self.length):
            after = temp.next
            temp.next = before 
            before = temp
            temp = after 

    def find_middle_node(self):
        fast = self.head
        slow = self.head

        while fast and fast.next :
            slow = slow.next
            fast= fast.next.next

        return slow.value   

    def has_loop(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast :
                return True

        return False   
    
    def find_kth_from_end(ll, k):
        slow = ll.head
        fast = ll.head
# Step 1: Move fast k steps ahead
        for _ in range(k):

            if not fast:
                return None  # k is larger than the number of nodes
            fast = fast.next

            

            
         # Step 2: Move slow and fast together until fast reaches the end   
        while  fast:
            slow = slow.next  
            fast = fast.next

        return slow    
    
    def binary_to_decimal(self):
        decimal = 0
        current = self.head
        while current:
            decimal = decimal * 2 + current.value
            current = current.next
        return decimal
    
    def partition_list(self, x):
        if not self.head:
            return

        # d1: dummy head for "less than x" list
        # d2: dummy head for "greater or equal to x" list
        d1 = Node(0)
        d2 = Node(0)
        prev1 = d1
        prev2 = d2

        current = self.head

        while current:
            if current.value < x:
                prev1.next = current
                prev1 = prev1.next
            else:
                prev2.next = current
                prev2 = prev2.next
            current = current.next

        # Important: End the second list properly
        prev2.next = None
        # Connect the two parts
        prev1.next = d2.next
        # Update the head
        self.head = d1.next
    




        

        
my_linked_list = LinkedList(1)  

my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

my_linked_list.find_middle_node()

print(my_linked_list.find_middle_node())

my_linked_list.print_list()


