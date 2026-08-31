class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node=Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

        return True

    def pop(self):
        if self.length == 0:  #no item in list
            return None

        temp = self.head
        pre = self.head  # assign pre and temp to first(head)

        while(temp.next):  # while tem.next is not None
            pre = temp    # point to same 
            temp = temp.next  # move forward

        self.tail = pre            #set tail to pre
        self.tail.next = None      # set tail.next to none to pop
        self.length -= 1           # decrement length

        if self.length == 0:        # post decrement , if only 1 node was there , remove head and tail
            self.head = None
            self.tail = None

        return temp
            
    def prepend(self,value):
        new_node=Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp= self.head
        self.head = self.head.next
        temp.next = None

        self.length -= 1

        if self.length == 0:
            self.tail= None
            self.head= None

        

        return temp

    def get(self,index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp=temp.next

        return temp

    def set_value(self,index,value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True

        return False

    def insert(self,index,value):
        if index<0 or index > self.length:
            return False

        if index == 0 :
            return self.prepend(value)

        if index == self.length :
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self,index):

        if index < 0 or index >= self.length:
            return False

        if index == 0:
            return self.pop_first()

        if index == self.length -1:
            return self.pop()

        prev= self.get(index-1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None

        self.length -=1
        return temp

    def find_max(self):
        if self.head == None:   # empty list
            return None

        maximum = self.head
        temp = self.head.next   # first node already counted

        while temp is not None:
            if temp.value > maximum:
                maximum = temp.value

            temp = temp.next

        return maximum

    def find_min(self):

        if self.head is None:
            return None

        minimum = self.head
        temp = self.head.next

        while temp is not None:
            if temp.value < minimum:
                minimum = temp.value

            temp = temp.next

        return minimum

    def count_occurance(self,value):
        count = 0
        temp = self.head
        while temp is not None:
            if temp.value == value:
                count += 1

            temp = temp.next

        return count

    def insert_after(self, target, value):
        temp = self.head
        while temp is not None and temp.value != target:
            temp = temp.next

        if temp is None :
            return False

        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node

        if temp.next == self.tail:
            self.tail == new_node

        self.length +=1
        return True

    def delete_occurances(self,value):
        while self.head is not None and self.head.value == value:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1

        if self.head is None:
            self.tail = None
            return

        prev = self.head 
        temp = self.head.next

        while temp is not None:
            if temp.value == value:
                prev.next = temp.next
                temp.next = None
                self.length -= 1
                temp = prev.next
            else:
                prev = temp
                temp =temp.next

        self.tail = prev


    def reverse(self):

        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before 
            before = temp
            temp = after

    def find_middle_node(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def has_loop(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def find_kth_from_end(self,k):

        slow = self.head
        fast = self.head

        for _ in range(k):

            if not fast:
                return None

            fast=fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow

    def find_kth_from_beginning(self,k):
        if k < 0 or k > self.length:
            return None

        temp = self.head
        for _ in range(k-1):
            temp = temp.next

        return temp

    


    

