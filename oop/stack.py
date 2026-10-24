class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if len(self._items)== 0:
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self):
        if len(self._items) == 0:
            raise IndexError("Stack is empty")
        return self._items[-1]

    @property
    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        return iter(reversed(self._items))

    def __repr__(self):
        return f"{type(self).__name__}({self._items})"

    def __eq__(self, other):
        return self._items == other._items

s = Stack()
assert s.is_empty
assert len(s) == 0

s.push(1)
s.push(2)
s.push(3)

assert not s.is_empty
assert len(s) == 3
assert 2 in s
assert 9 not in s
assert s.peek() == 3
assert len(s) == 3              # peek didn't remove anything
assert list(s) == [3, 2, 1]     # top to bottom
assert repr(s) == "Stack([1, 2, 3])"

other = Stack()
for x in [1, 2, 3]:
    other.push(x)
assert s == other

assert s.pop() == 3
assert len(s) == 2
assert s != other

s.pop()
s.pop()
assert s.is_empty

for method in (s.pop, s.peek):
    try:
        method()
        assert False, f"{method.__name__} should have raised"
    except IndexError:
        pass

print("All tests passed")