class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            return

        last = self.head
        while(last.next):
            last = last.next
        last.next = node

    def prepend(self,data):
        node = Node(data)

        if not self.head:
            self.head = node
            return
        
        node.next = self.head
        self.head = node

    def insert_at(self,key, data):
        node = Node(data)
        if not self.head:
            if key==0:
                self.head = node
            else:
                raise Exception("List index out of range")
            return


        if key>self.get_length():
            raise Exception("List index out of range")
        
        if key==0:
            node.next = self.head
            self.head = node
            return
        
        current = self.head
        count = 0
        while current:
            if count == key-1:
                node.next = current.next
                current.next = node
            current = current.next
            count+=1


    def bulk_append(self,lst):
        for data in lst:
            self.append(data)

    def get_length(self):
        count = 0
        last = self.head
        while(last):
            count += 1
            last = last.next
        return count
    


    def llprint(self, head):
        last = head
        while(last):
            print(last.data, end=" -> ")
            last = last.next
        print()

    def get_head(self):
        return self.head

    @staticmethod
    def reverse_list(head):
        print("reversed list")
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def remove_duplicates(self):
        print("remove duplicates")
        current = self.head
        if self.head is None:
            raise ValueError("Nothing to check")
        else:
            while current.next:
                if current.data == current.next.data:
                    current.next = current.next.next
                else:
                    current = current.next
    
    @staticmethod
    def merge_list(l1, l2):
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.data > l2.data:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next


    @staticmethod
    def intersect(l1, l2):
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.data == l2.data:
                tail.next = l1
                tail=tail.next

            l1 = l1.next
            l2 = l2.next
            

        return dummy.next

    
    def detect_cycle(self):
        hare = self.head
        tortise = self.head
        if self.head is None:
            print("List is empty")
            return

        while hare and hare.next:
            tortise = tortise.next
            hare = hare.next.next
            
            if tortise == hare:
                print("cycle detected")
                return
        
        print("no cycle detected")

    @staticmethod
    def remove_nth_node(head1,n):
        dummy = Node(0)
        dummy.next = head1
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        return dummy.next

# c    n
# 1 -> 2 -> 3 -> 4
# 1 <- 2 <- 3 <- 4


l1 = LinkedList()
l1.bulk_append([3,7,8,10,3,7])
l2 = LinkedList()
l2.bulk_append([99,1,9,10,11,13,14])
head1 = l1.get_head()
head2 = l2.get_head()

# ll.llprint(head)
# reversed_head = ll.reverse_list(head)
# ll.llprint(reversed_head)
# ll.remove_duplicates()
# merge_list = LinkedList.merge_list(head1,head2)
# intersect = LinkedList.intersect(head1,head2)
# l1.llprint(merge_list)
# l1.llprint(intersect)

# l1.head.next.next.next.next = l1.head.next.next
# print(l1.head.next.next.next.next.data)
# print(l1.head.next.next.data)
# l1.detect_cycle()
nth_node_remove = LinkedList.remove_nth_node(head2,3)
print(l1.llprint(nth_node_remove))
