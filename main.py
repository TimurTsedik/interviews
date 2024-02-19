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


def balanced_brackets(string: str) -> str:
    s = Stack()
    for char in string:
        if char in '({[':
            s.push(char)
        elif char in ')}]':
            if s.is_empty():
                output = 'Несбалансированно'
                return output
            if char == ')' and s.peek() != '(':
                output = 'Несбалансированно'
                return output
            if char == '}' and s.peek() != '{':
                output = 'Несбалансированно'
                return output
            if char == ']' and s.peek() != '[':
                output = 'Несбалансированно'
                return output
            s.pop()
    if s.is_empty():
        output = 'Сбалансированно'
    else:
        output = 'Несбалансированно'
    return output


print(balanced_brackets('(((([{}]))))'))
print(balanced_brackets('[([])((([[[]]])))]'))
print(balanced_brackets('[({)]}'))
