class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next = new_node
            new_node.prev = last

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    @staticmethod
    def dll_print(head):
        result = []
        if head is None:
            return None
        else:
            last = head
            while(last):
                result.append(str(last.data))
                last = last.next
            print(" <-> ".join(result))
        print()

    def get_head(self):
        if self.head is None:
            return None
        else:
            return self.head 
    
    @staticmethod
    def display_reverse(head):
        last = head
        while(last.next):
            last = last.next
        
        first = last
        while(first):
            print(first.data, end=" ")
            first = first.prev
        print()
    
    def delete(self, key):
        temp = self.head
        if self.head is None:
            return 
        elif self.head.data == key:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        while temp:
            if temp.data == key:
                if temp.next:
                    temp.next.prev = temp.prev
                elif temp.prev:
                    temp.prev.next = temp.next
                return
            temp = temp.next


    def get_length(self):
        count = 0
        if self.head is None:
            return 0
        else:
            last = self.head
            while(last):
                count+=1
                last = last.next
            return count


    def insertAtPosition(self,position, value):
        new_node = Node(value)
        
        if position==0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        
        else:
            current = self.head  
            for i in range(1, self.get_length()):
                if i <position:
                    if i == position-1:
                        new_node.next = current.next
                        new_node.prev = current

                    if current.next:
                        current.next.prev = new_node
                    
                    current.next = new_node
                    return
                current = current.next
            return self.head

    def findAndDelete(self, value):
        if self.head is None:
            return
        elif self.head.data == value:
            self.head.prev = None
            self.head = self.head.next
            return self.head
        else:
            temp = self.head
            while(temp):
                if temp.data == value:
                    prev_node = temp.prev
                    next_node = temp.next

                    if prev_node:
                        prev_node.next = next_node
                    if next_node:
                        next_node.prev = prev_node
                temp = temp.next
            return self.head

        
    
    def sort_list(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            temp = self.head
            swapped = False
            while temp and temp.next:
                if  temp.data > temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data
                    swapped = True
                temp = temp.next
        return self.head


    def remove_duplicates(self):
        if self.head is None:
            return 

        temp = self.head
        while temp and temp.next:
            if temp.data != temp.next.data:
                temp = temp.next
            else:
                temp.next = temp.next.next
                if temp.next:
                    temp.next.prev = temp
        return self.head


    def insertNodeInSortedOrder(self, value):
        new_node = Node(value)
        if self.head is None:
            return
        elif self.head.data > value:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next and temp.next.data < value:
                temp = temp.next

            new_node.next = temp.next
            if temp.next:
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp

    
    def is_palindrome(self, head):
        if head is None:
            return True

        else:
            tail = head
            while tail.next:
                tail = tail.next


            while head != tail and head.prev != tail:
                if head.data !=  tail.data:
                    return False
    
                head = head.next
                tail= tail.prev
            return True


    @staticmethod
    def rotate_doubly_linked_list(head, N):
        # No rotation needed
        if not head or not head.next or N==0:
            return head

        #  find length
        length = 1
        tail = head
        while tail.next:
            length+=1
            tail = tail.next
          
        N = N%length
        if N==0:  # N==0 then no rotation needed
            return head


        # Rotation part

        new_head = head
        for _ in range(N-1):
            new_head = new_head.next

        new_tail = new_head
        new_head = new_head.next

        new_head.prev = None
        new_tail.next = None

        tail.next = head
        head.prev = tail

        return new_head

    def two_halves(self):
        first_half = Node(0)
        second_half = Node(0)
        dummy = first_half
        dummy2 = second_half
        if self.head is None:
            return

        # find length
        length = 1
        tail = self.head
        while tail.next:
            length += 1
            tail = tail.next

        midpoint = length //2
        temp = self.head
        for _ in range(midpoint-1):
            temp = temp.next

        second_half = temp.next
        temp.next = None
        if second_half:
            second_half.prev = None


        self.dll_print(self.head)
        self.dll_print(second_half)

        


        
        
                    

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(5)
dll.append(6)
dll.append(9)
dll.append(2)
dll.append(1)


head = dll.get_head()


print("Original List")
DoublyLinkedList.dll_print(head)

# print("After insertion List")
# n_head = dll.insertAtPosition(1,3)
# DoublyLinkedList.dll_print(n_head)

# print("Find and delete")
# d_head = dll.findAndDelete(2)

# DoublyLinkedList.dll_print(d_head)

# print("Sort List")
# n_head = dll.sort_list()
# DoublyLinkedList.dll_print(n_head)

# print("Remove Duplicates List")
# r_head = dll.remove_duplicates()
# DoublyLinkedList.dll_print(r_head)


# print("Insert Node in sorted order")
# dll.insertNodeInSortedOrder(value=0)
# dll.insertNodeInSortedOrder(value=3)
# dll.insertNodeInSortedOrder(value=6)
# dll.insertNodeInSortedOrder(value=8)
# dll.insertNodeInSortedOrder(value=7)
# DoublyLinkedList.dll_print(dll.get_head())

# is_palindrome = dll.is_palindrome(dll.get_head())
# print("Is Palindrome : ", is_palindrome)

# print("After Rotation")
# new_head = dll.rotate_doubly_linked_list(head,2)
# dll.dll_print(new_head)

print("two halves")
dll.two_halves()
# dll.dll_print(head)