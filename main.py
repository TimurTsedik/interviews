class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    # '(((([{}]))))'
    # '[([])((([[[]]])))]'
    # '{()}'
    # '{{[()]}}'
    # '}{}'
    # '{{[(])]}}'
    # '[[{())}]'


def balanced_brackets(string: str) -> bool:
    s = Stack()
    for char in string:
        if char in '({[':
            s.push(char)
        elif char in ')}]':
            if s.is_empty():
                return False
            if char == ')' and s.peek() != '(':
                return False
            if char == '}' and s.peek() != '{':
                return False
            if char == ']' and s.peek() != '[':
                return False
            s.pop()
    return s.is_empty()


print(balanced_brackets('(((([{}]))))'))
print(balanced_brackets('[([])((([[[]]])))]'))
print(balanced_brackets('[({)]}'))
