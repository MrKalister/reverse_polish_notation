OPERATIONS = {
    '+': lambda num_1, num_2: num_1 + num_2,
    '*': lambda num_1, num_2: num_1 * num_2,
    '/': lambda num_1, num_2: num_1 // num_2,
    '-': lambda num_1, num_2: num_1 - num_2,
}


class Stack:
    """Implementation of the stack data structure."""

    def __init__(self) -> None:
        """Initialize a list."""
        self._items = []

    def push(self, item: str) -> None:
        """Added item in the List."""
        self._items.append(item)

    def pop(self) -> int:
        """Return the last item in the list."""
        return self._items.pop()


def reverse_polish_notation(object: Stack, char: str) -> int:
    """Pass the object and symbol in a calculator.

    Сalculations of mathematical expressions,
    in the form of reverse Polish notation.
    """
    rpn = Stack()
    for char in input().strip().split():
        if char in OPERATIONS:
            num_2 = Stack.pop()
            num_1 = Stack.pop()
            Stack.push(OPERATIONS[char](num_1, num_2))
        else:
            Stack.push(int(char))
    print(rpn.pop())


if __name__ == '__main__':
    reverse_polish_notation()
