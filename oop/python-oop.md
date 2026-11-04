# Python OOP

Practice files: `oop/bank_account.py`, `oop/employees.py`, `oop/shapes.py`, `oop/stack.py`.

---

## 1. Classes and objects

A **class** is the blueprint. An **object** (instance) is one thing made from it.

```python
class Dog:
    species = "canine"              # class attribute: shared by every Dog

    def __init__(self, name, age):  # runs automatically when a Dog is made
        self.name = name            # instance attribute: each Dog has its own
        self.age = age

    def bark(self):
        return f"{self.name} says woof"

rex = Dog("Rex", 3)                 # calls __init__(rex, "Rex", 3)
rex.bark()                          # "Rex says woof"
Dog.species                         # "canine"
```

### self

`self` is **the object the method is being called on**.
`rex.bark()` is really `Dog.bark(rex)`, so inside `bark`, `self` is `rex`.

- Every method takes `self` as its first parameter. You never pass it yourself.
- `self.name = name` means "store this on this particular object".
- Forget `self.` and it's just a local variable that disappears when the method ends.

### Class vs instance attributes

| | Defined | Belongs to | Use for |
|---|---|---|---|
| class attribute | in the class body | the class, shared | constants, counters across all objects |
| instance attribute | `self.x = ...` in a method | one object | each object's own data |

Changing a class attribute through `self.x = ...` doesn't change it for everyone. It creates a new instance attribute that hides it. To change the shared one, use `ClassName.x = ...`.

---

## 2. Private by convention

Python has no `private` keyword. It uses naming conventions:

| Name | Meaning |
|---|---|
| `balance` | public |
| `_balance` | "internal, don't touch from outside". Only a convention, still accessible |
| `__balance` | name-mangled to `_ClassName__balance`, harder to reach by accident. Rarely needed |

Use `_name` for the stored value behind a property.

---

## 3. @property (getters and setters)

A property lets `obj.balance` look like a plain attribute, while actually running a method.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance          # goes THROUGH the setter, so it's validated too

    @property
    def balance(self):                  # getter: runs on obj.balance
        return self._balance

    @balance.setter
    def balance(self, value):           # setter: runs on obj.balance = something
        if value < 0:
            raise ValueError("balance can't be negative")
        self._balance = value           # the real value is stored in _balance
```

```python
acc = BankAccount("Bob", 100)
acc.balance          # getter → 100
acc.balance = 50     # setter, value = 50
acc.balance = -5     # setter → ValueError
```

How it works:
- `value` is whatever is on the right of the `=` in `obj.balance = ...`.
- The setter runs on **every** `obj.balance = ...`, **including the one in `__init__`**. That's why `__init__` writes `self.balance`, not `self._balance`: so the starting value is checked too.
- Store in `self._balance`. Writing `self.balance = value` inside the setter would call the setter again, forever.

### Read-only property

Getter only, no setter:
```python
@property
def area(self):
    return self.width * self.height
```
`obj.area = 5` raises `AttributeError`.

### When does it need a getter or a setter?

| Situation | What to use |
|---|---|
| Any value is fine, no rules | plain attribute `self.name = name` |
| Value has rules (no negatives, must be valid email) | property + setter that validates |
| Calculated from other values (area, full name) | read-only property, no setter |
| Must never change after creation (id) | read-only property backed by `_id` |

Don't add properties "just in case". A plain attribute can become a property later without changing any code that uses it.

---

## 4. Inheritance

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name} earns {self.salary}"

class Manager(Employee):                     # Manager IS AN Employee
    def __init__(self, name, salary, reports):
        super().__init__(name, salary)       # let Employee set up its part
        self.reports = reports               # then add Manager's own part

    def describe(self):                      # overriding: replaces the parent version
        return super().describe() + f" and manages {len(self.reports)} people"
```

- `class Child(Parent)` = Child gets every method and attribute of Parent.
- **Overriding**: define a method with the same name in the child. The child's version wins.
- `super()` = "the parent class". `super().__init__(...)` runs the parent's setup so you don't copy it.
- If the child has no `__init__`, the parent's is used automatically.

---

## 5. Abstract classes (ABC)

An abstract class is a blueprint for other classes. It can't be used directly.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):          # every subclass MUST write this
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2
```

- `Shape()` → `TypeError`: can't instantiate an abstract class.
- A subclass that **forgets** `area` also errors, but only **when you try to create one**, not when the class is defined.
- Similar to a Java interface/abstract class: it forces every shape to have `area()`.

```python
def largest(shapes):
    return max(shapes, key=lambda s: s.area())
```
Works for any mix of shapes, because they all promise `area()`.

---

## 6. Duck typing

"If it walks like a duck and quacks like a duck, it's a duck."
Python doesn't check an object's type, only whether it has the method you call.

```python
class Duck:
    def speak(self): return "quack"

class Robot:
    def speak(self): return "beep"

for thing in [Duck(), Robot()]:
    print(thing.speak())     # works: no shared parent needed
```

In Java they'd need a shared interface. In Python they just need the method. ABCs are for when you **want** the rule enforced.

---

## 7. Dunder (magic) methods

"Dunder" = double underscore. Python calls these for you when you use built-in syntax.

| You write | Python calls |
|---|---|
| `print(obj)`, `str(obj)` | `__str__` |
| the shell, lists, debugging | `__repr__` |
| `a == b` | `__eq__` |
| `a < b`, `sorted(...)` | `__lt__` |
| `len(obj)` | `__len__` |
| `x in obj` | `__contains__` |
| `for x in obj` | `__iter__` |

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, x):
        self._items.append(x)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)

    def __contains__(self, x):
        return x in self._items

    def __iter__(self):
        return iter(self._items)

    def __eq__(self, other):
        if not isinstance(other, Stack):
            return NotImplemented
        return self._items == other._items

    def __repr__(self):
        return f"Stack({self._items})"

    def __str__(self):
        return f"Stack with {len(self)} items"
```

### __str__ vs __repr__

| | For | Style |
|---|---|---|
| `__str__` | people (`print`) | friendly: `Stack with 3 items` |
| `__repr__` | developers (debugging) | exact, ideally looks like code to recreate it: `Stack([1, 2, 3])` |

If there's no `__str__`, `print` falls back to `__repr__`. If neither exists you get `<__main__.Stack object at 0x...>`. So if you only write one, write `__repr__`.

### __eq__

Without it, `==` checks "are these the **same object** in memory", like Java's `==`. Two stacks with the same items would be "not equal". With it, you decide what equal means.

### __lt__

Defines `<`. Once it exists, `sorted()`, `min()` and `max()` work on your objects.

---

## 8. @classmethod and @staticmethod

```python
class Date:
    def __init__(self, day, month, year):
        self.day, self.month, self.year = day, month, year

    @classmethod
    def from_string(cls, text):          # cls = the class itself
        d, m, y = map(int, text.split("/"))
        return cls(d, m, y)              # build and return a new object

    @staticmethod
    def is_leap(year):                   # no self, no cls: just a helper
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

Date.from_string("04/11/2026")
Date.is_leap(2028)
```

| | First parameter | Use for |
|---|---|---|
| normal method | `self` (the object) | anything using one object's data |
| `@classmethod` | `cls` (the class) | other ways to create objects ("alternative constructors") |
| `@staticmethod` | none | a helper that belongs with the class but needs no object or class data |

---

## 9. Type hints

```python
def area(width: float, height: float) -> float:
    return width * height

items: list[int] = []
```

Hints are notes for people and tools (VS Code, linters). Python **doesn't enforce them** at runtime: `area("a", 2)` still runs (and breaks).

---

## 10. @dataclass

For classes that are mostly just data. Python writes `__init__`, `__repr__` and `__eq__` for you.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int = 0          # default value

p = Point(3, 4)
print(p)                # Point(x=3, y=4)
Point(3, 4) == p        # True
```

- The type hints are **required** here. They're how dataclass knows which fields exist.
- Fields with defaults have to come after fields without.
- `@dataclass(order=True)` also writes `<`, `>` etc. so they can be sorted.
- `@dataclass(frozen=True)` makes objects read-only after creation.

---

## 11. Java → Python cheat sheet

| Java | Python |
|---|---|
| constructor `Dog(...)` | `__init__(self, ...)` |
| `this` | `self` (written explicitly) |
| `private int x` | `self._x` (convention only) |
| `getX()` / `setX()` | `@property` / `@x.setter` |
| `extends` | `class Child(Parent)` |
| `super(...)` | `super().__init__(...)` |
| `interface`, `abstract` | `ABC` + `@abstractmethod` |
| `toString()` | `__str__` / `__repr__` |
| `equals()` | `__eq__` |
| `compareTo()` | `__lt__` |
| `static` method | `@staticmethod` (or `@classmethod`) |
| `new Dog()` | `Dog()` (no `new`) |