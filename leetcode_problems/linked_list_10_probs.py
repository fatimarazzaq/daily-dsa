class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(data)
        
    def insert(self, data, position):
        node = Node(data)
        if self.head is None:
            return None
        else:
            current = self.head
            if position < 0:
                return None
            elif position == 0:
                node.next = self.head
                self.head = node
            else:
                for i in range(position-1):
                    if current.next is None:
                        return None
                    current = current.next
                node.next = current.next
                current.next = node
            return self.head


    @staticmethod
    def remove_ocurrences(head,value):
        if head is None:
            return None
        else:
            if head is not None and head.data == value:
                head = head.next
            current = head
            while current is not None and current.next is not None:
                if current.next.data == value:
                    current.next = current.next.next
                else:
                    current = current.next
            return head



    @staticmethod
    def reverse_list(head):
        if head is None:
            return None
        else:
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

    
    @staticmethod
    def remove_duplicates(head):
        if head is None:
            return None
        else:
            current = head
            while current.next:
                if current.data == current.next.data:
                    current.next = current.next.next
                else:
                    current = current.next

            return head

    @staticmethod
    def find_middle(head):
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    @staticmethod
    def merge_sort(head1, head2):
        dummy = Node(0)
        tail = dummy

        p1,p2 = head1,head2
        while p1 and p2:
            if p1.data > p2.data:
                tail.next = p2
                p2 = p2.next
            else:
                tail.next = p1
                p1 = p1.next
            tail = tail.next

        tail.next = p1 if p1 else p2
        return dummy.next

    @staticmethod
    def get_length(head):
        count = 0 
        if head is None:
            return 0
        else:
            last = head
            while last:
                count += 1
                last = last.next
            return count

    @staticmethod
    def remove_head(head):
        if head is None:
            return None
        else:
            head = head.next
            return head

    @staticmethod
    def remove_last(head):
        if head is None:
            return None
        elif head.next is None:
            return None
        else:
            last = head
            while last.next and last.next.next:
                last = last.next
            last.next = None
            return head

    @staticmethod
    def get_nth_node(head,n):
        if head is None:
            return None
        else:
            current = head
            if n < LinkedList.get_length(head):
                for i in range(n):
                    current = current.next
                return current.data
            else:
                return None

    @staticmethod
    def get_nth_from_end(head,n):
        # Create a dummy node to handle edge cases such as removing the head
        dummy = Node(0)
        dummy.next = head
        slow, fast = dummy, dummy

        # Move fast pointer n+1 steps ahead to maintain a gap of n between slow and fast
        for _ in range(n + 1):
            if fast is None:
                return None  # If n is larger than the length of the list
            fast = fast.next

        # Move both slow and fast pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Now slow is just before the node we need to remove
        return slow.next.data

    @staticmethod
    def find_max(head):
        if head is None:
            return None
        else:
            current = head
            max = current.data
            while(current):
                if current.data > max:
                    max = current.data
                current = current.next
            return max

    @staticmethod
    def find_min(head):
        if head is None:
            return None
        else:
            current = head
            mini = current.data
            while(current):
                if current.data < mini:
                    mini = current.data
                current = current.next
            return mini

    @staticmethod
    def count_nodes(head):
        if head is None:
            return 0
        else:
            current = head
            count = 0
            while(current):
                count+=1
                current=current.next
            return count


    @staticmethod
    def get_n_from_end(head,n):
        if head is None:
            return None
        else:
            slow, fast = head, head
            for _ in range(n):
                if fast is None:
                    return None
                fast = fast.next

            while(fast):
                slow = slow.next
                fast = fast.next

            return slow.data

    @staticmethod
    def delete_last(head):
        if head is None:
            return None
        elif head.next == None:
            return None
        else:
            current = head
            while current.next and current.next.next:
                current = current.next
            current.next =  None
            return head

    def get_head(self):
        return self.head
    
    def __len__(self):
        count = 0 
        if self.head is None:
            return 0
        else:
            last = self.head
            while last:
                count += 1
                last = last.next
            return count
        
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next

        return " -> ".join(values)



ll = LinkedList()
ll.append(2)
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(2)
print(ll)


l2 = LinkedList()
l2.append(1)
l2.append(3)
l2.append(4)
# print(l2)



# a  = LinkedList.reverse_list(ll_head)
# ll.head = a

# ll.head = LinkedList.remove_duplicates(ll.head)

# ll.head = LinkedList.find_middle(ll.head)

# ll.head = LinkedList.merge_sort(ll.head,l2.head)

# ll.head = LinkedList.remove_head(ll.head)

# ll.head = LinkedList.remove_last(ll.head)

# print(LinkedList.get_nth_node(ll.head,4))

# print(LinkedList.get_nth_from_end(ll.head,6))

# ll.insert(3,2)



# ll.head = LinkedList.remove_ocurrences(ll.head,2)


# maxi = LinkedList.find_max(ll.head)
# mini = LinkedList.find_min(ll.head)
# count = LinkedList.count_nodes(ll.head)
# print(LinkedList.get_n_from_end(ll.head,8))
ll.head = LinkedList.delete_last(ll.head)

# print("maximum" , maxi)
# print("minimum" ,mini)
# print("count" ,count)
print(ll)