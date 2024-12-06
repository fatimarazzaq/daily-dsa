class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0

    def find_middle(self):
        if not self.is_empty():
            n = len(self.stack)
            if n%2!=0:
                return self.stack[len(self.stack)//2]
            else:
                return self.stack[len(self.stack)//2 - 1], self.stack[len(self.stack)//2]
        else:
            return "Stack is empty"

    def print(self):
        print(self.stack) 

def brackets_validator(string):
    stack = []
    brackets = {'(':')','{':'}','[':']'}

    for bracket in string:
        if bracket in brackets:
            stack.append(bracket)
        elif bracket in brackets.values():
            if not stack or brackets[stack.pop()] != bracket:
                return False
        else:
            continue
    
    return not stack


def string_reverse(string):
    stack = []
    for i in string:
        stack.append(i)

    reversed_string = ""
    while stack:
        reversed_string+=stack.pop()
    return reversed_string


def sort_stack(mystack):
    sorted_stack=sorted(mystack)
    return sorted_stack


def reverse_stack_with_auxiliary(original_stack):
    auxiliary_stack = []
    while original_stack:
        auxiliary_stack.append(original_stack.pop())
    return auxiliary_stack
    

def insert_at_bottom(stack, item):
    if not stack:
        return stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack,item)
        stack.append(temp)

def reverse_stack_using_recurrsion(stack):
    if stack:
        temp = stack.pop()
        reverse_stack_using_recurrsion(stack)
        insert_at_bottom(stack,temp)


def check_palidrome(string):
    str_stack = list(string)
    print(str_stack)
    new_stack = []
    while str_stack:
        new_stack.append(str_stack.pop())
    return new_stack == list(string)



# stack = [1,2,3,4,5]
# reverse_stack_using_recurrsion(stack)
# print(stack)

print(check_palidrome("fatima"))


# print(brackets_validator("(){}[]"))  # True
# print(brackets_validator("({[)]}"))  # False

# print(string_reverse("hello"))

# s = Stack()

# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.push(6)
# s.print()

# print(s.find_middle())
    

# print(sort_stack([3, 5, 1, 4, 2]))

