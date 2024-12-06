class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    
class CicularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            last = self.head
            while(last.next!=self.head):
                last = last.next
            last.next = node
            node.next = self.head

        
    def prepend(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            last = self.head
            while(last.next != self.head):
                last = last.next

            last.next = node
            node.next = self.head
            self.head = node


    @staticmethod
    def cll_print(head):
        if head is None:
            return
        else:
            current = head
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == head:
                    break
            print('\n')


    def count_occurance(self, value):
        count = 0
        if self.head is None:
            return count
        else:
            last = self.head
            while True:
                if last.data == value:
                    count +=1
                last = last.next
                if last == self.head:
                    break

            return count

    
    def get_head(self):
        if self.head is None:
            return
        else:
            return self.head

    @staticmethod
    def merge_lists(head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        
        if head1 is None or head2 is None:
            return
        else:
            one, two = head1, head2
            while one.next!=head1:
                one = one.next
            one.next = None

            while two.next!=head2:
                two = two.next
            two.next = None

            dummy = Node(0)
            temp = dummy

            p1,p2 = head1,head2

            while p1 and p2:
                if p1.data < p2.data:
                    temp.next = p1
                    p1 = p1.next
                else:
                    temp.next = p2
                    p2 = p2.next
                temp = temp.next

            temp.next = p1 if p1 else p2


            new_head = dummy.next
            temp = new_head
            while temp.next:
                temp = temp.next
            temp.next = new_head
            return new_head

    def sorted_list(self):
        if self.head is None or self.head.next == self.head:
            return True
        temp = self.head
        while True:
            if temp.data > temp.next.data:
                return False
            temp = temp.next
            if temp == self.head:
                break
        return True
            

    def find_largest(self):
        if self.head is None:
            return None
        else:
            largest = self.head.data
            temp = self.head
            while True:
                if temp.data > largest:
                    largest = temp.data
                temp = temp.next
                if temp == self.head:
                    break
            return largest

    def get_length(self, head):
        count = 0
        if head is None:
            return 0 
        else:
            last = head
            while True:
                count += 1
                last = last.next
                if last == head:
                    break
            return count

    def check_identical(self, head1, head2):
        if head1 is None and head2 is None:
            return True
        if head1 is None or head2 is None:
            return False
        p1, p2 = head1, head2

        p1_len = self.get_length(head1)
        p2_len = self.get_length(head2)

        if p1_len!=p2_len:
            return False
        else:
            while True:
                if p1.data != p2.data:
                    return False
                p1 = p1.next
                p2 = p2.next
                if p1 == head1 and p2 == head2:
                    break
            return True

    def insert_node(self, head ,data, position):
        new_node = Node(data) 
        if head is None:
            new_node.next = new_node
            return new_node
        elif position == 1:
            temp = head
            while(temp.next!=head):
                temp = temp.next

            temp.next = new_node
            new_node.next = head
            return new_node
        else:
            temp = head
            i=1
            while(i<position):
                if i==position-1:
                    new_node.next = temp.next
                    temp.next = new_node
                    return head
                temp = temp.next
                i+=1

            temp.next = new_node
            new_node.next = head
            return head

        
        
        
    def delete_node(self, head, position):
        if head is None:
            return None
        elif position==1:
            current = head
            while current.next!=head:
                current = current.next
            current.next = head.next
            head = current.next
            return head
        else:
            current = head
            i = 1
            while current and i<position:
                if i == position-1:
                    current.next = current.next.next
                current = current.next
                i += 1
            return head
        



c1 = CicularLinkedList()
c1.append(1)
c1.append(2)
c1_head = c1.get_head()

c2 = CicularLinkedList() 
c2.append(1)
c2.append(2)
c2.append(3)
c2.append(4)
c2.append(1)
c2_head = c2.get_head()


# print("is_identical : ", c1.check_identical(c1_head, c2_head))
# CicularLinkedList.cll_print(c1_head)


# new_head = c2.insert_node(c2_head,6,12)
# CicularLinkedList.cll_print(new_head)

# new_head = c2.delete_node(c2_head,1)
# CicularLinkedList.cll_print(new_head)


norepeat_head = c2.print_norepeat(c2_head)
CicularLinkedList.cll_print(norepeat_head)