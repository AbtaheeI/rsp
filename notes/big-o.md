# Big O (CTCI Chapter VI, part 1)

## 1. Time and space

- Big O = how runtime or memory grows as the input gets big. Not exact seconds.
- Best, worst and expected case are a separate idea from O/Θ/Ω. Interviews usually want worst or expected case.
- Space counts extra memory you use, including recursive calls sitting on the call stack.

```python
def total(arr):          # O(n) time, O(1) space
    s = 0
    for x in arr:
        s += x
    return s

def copy(arr):           # O(n) time, O(n) space (new list)
    return [x for x in arr]
```

## 2. Drop constants and non-dominant terms

- O(2n) is O(n). Constants don't change how it grows.
- Keep only the term that grows fastest: O(n² + n) is O(n²).
- Growth order: log n < n < n log n < n² < 2ⁿ < n!
- Can't drop terms with different variables: O(b² + a) stays as is.

```python
def min_and_max(arr):    # two passes = O(2n) = O(n)
    lo = min(arr)
    hi = max(arr)
    return lo, hi
```

## 3. Add vs multiply

- One loop, then another loop = add: O(a + b)
- One loop inside another = multiply: O(a * b)
- Two different inputs means two different variables. Don't call both of them n.

```python
def print_both(a, b):    # O(a + b)
    for x in a:
        print(x)
    for y in b:
        print(y)

def print_pairs(a, b):   # O(a * b)
    for x in a:
        for y in b:
            print(x, y)
```

## 4. Amortized time

- A list doubles its capacity when it fills up, which means copying everything over.
- Copies happen at sizes 1, 2, 4, 8, ... n. Total copied = 1 + 2 + 4 + ... + n, which is under 2n.
- So n appends cost O(n) in total, which is O(1) per append on average.
- A single append can still be O(n). Amortized is the average over many operations.

```python
nums = []
for i in range(n):       # O(n) total, O(1) amortized per append
    nums.append(i)
```

## 5. Log n runtimes

- If the problem gets halved every step, it takes log n steps to get down to 1.
- Binary search is the main example.

```python
def binary_search(arr, target):   # O(log n) time, O(1) space
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

## 6. Recursive runtimes

- Time is usually branches ^ depth. A function that calls itself twice, n levels deep, is O(2ⁿ).
- Space is the max depth of the call stack, not the total number of calls.
- The calls run one after another. A call finishes and frees its memory before the next one starts, so only one path from top to bottom is on the stack at any time.

```python
def f(n):                # O(2^n) time, O(n) space
    if n <= 1:
        return 1
    return f(n - 1) + f(n - 1)
```