# Python DSA toolkit

One line per operation with its Big O. n = number of items unless it says otherwise.
Always ask "n of **what**?": the cost depends on the size of what you pass in.

---

## Big O in one table

| Big O | Name | 1,000 items | 1,000,000 items | Example |
|---|---|---|---|---|
| O(1) | constant | 1 step | 1 step | `nums[5]`, `d[key]` |
| O(log n) | logarithmic | ~10 | ~20 | binary search, heap push/pop |
| O(n) | linear | 1,000 | 1,000,000 | one loop, `min`, `x in list` |
| O(n log n) | | ~10,000 | ~20,000,000 | sorting |
| O(n²) | quadratic | 1,000,000 | 1,000,000,000,000 | loop inside a loop |

- log n = how many times you can halve n before reaching 1.
- Drop constants: n/2 steps is still O(n).
- Loop inside a loop multiplies: O(n) × O(n) = O(n²). One after the other adds: O(n) + O(n) = O(n).
- **Amortized**: one call can be slow, but averaged over all calls it's cheap (RecentCounter: each ping added once and removed once, so O(1) amortized).

---

## 1. list

Items side by side in numbered slots.

| Operation | Big O | Why |
|---|---|---|
| `nums[i]`, `nums[i] = x` | O(1) | jump straight to the slot |
| `nums.append(x)` | O(1) amortized | add at the end, nothing moves |
| `nums.pop()` | O(1) | remove from the end, nothing moves |
| `len(nums)` | O(1) | Python keeps a running count |
| `nums.pop(0)` | **O(n)** | everything shifts left to fill the gap |
| `nums.insert(0, x)` | **O(n)** | everything shifts right |
| `x in nums`, `nums.index(x)` | **O(n)** | checks slot by slot |
| `min(nums)`, `max(nums)`, `sum(nums)` | O(n) | one pass, "best so far". `min` does NOT sort |
| `nums[a:b]` (slice) | O(b − a) | builds a new list, copies the items |
| `nums.copy()`, `list(x)` | O(n) | copies every item |

- `pop()` vs `pop(0)` look the same and aren't: `pop(0)` in a loop is a classic Time Limit Exceeded.
- `[[]] * 3` makes 3 references to the **same** list. Use `[[] for _ in range(3)]`.
- `b = a` doesn't copy: both names point to the same list. Changing one changes "both".

---

## 2. dict and set

Hash table: the key goes through a hash function that gives its slot directly.

| Operation | Big O |
|---|---|
| `d[key]`, `d[key] = v`, `key in d`, `del d[key]`, `d.get(key, default)` | O(1) |
| `value in d.values()` | **O(n)**: the hash only finds keys |
| loop over `d`, `d.keys()`, `d.values()`, `d.items()` | O(n) |
| `s.add(x)`, `s.remove(x)`, `x in s` | O(1) |
| `set(nums)` | O(n) |
| `a & b`, `a \| b`, `a - b` | O(len of the sets) |

- Keys must be unchangeable: str, int, tuple. A list as a key → `TypeError: unhashable type`.
- `{}` is an empty **dict**. Empty set is `set()`.
- `d[missing]` crashes with `KeyError`. `d.get(missing, 0)` doesn't.
- `==` on dicts compares key → value pairs, not order.
- **The big pattern:** checking `x in something` inside a loop? Make it a set or dict. O(n²) → O(n).

---

## 3. deque

`from collections import deque`. Linked chunks, pointers at both ends.

| Operation | list | deque |
|---|---|---|
| add/remove at the end: `append`, `pop` | O(1) | O(1) |
| add/remove at the front: `appendleft`, `popleft` | **O(n)** | **O(1)** |
| `q[i]` in the middle | O(1) | **O(n)** |

- Use for queues (first in, first out), BFS, sliding windows. List for jumping to positions.
- `deque(maxlen=k)` keeps only the last k items, old ones fall off the left (like `tail`).
- `while q:` = while not empty.

---

## 4. defaultdict and Counter

`from collections import defaultdict, Counter`. Both are dicts: same speeds.

| Operation | Big O |
|---|---|
| `defaultdict(int)`, `(list)`, `(set)`: missing key starts as 0, `[]`, `set()` | O(1) per access |
| `Counter(iterable)` | O(n) |
| `c[x]` (missing → 0, no crash), `c[x] += 1` | O(1) |
| `Counter(a) == Counter(b)` | O(distinct keys) |
| `c.most_common(k)` | uses a heap/sort: O(n log k) |

- Counting → `Counter`. Grouping into lists → `defaultdict(list)`.
- Anagram check: `Counter(s) == Counter(t)`. Space O(1) for lowercase letters (max 26 keys).

---

## 5. heapq

`import heapq`. **Min**-heap stored in a plain list: `h[0]` is always the smallest. Parent ≤ children, tree is log n levels tall.

| Operation | Big O |
|---|---|
| `h[0]` (peek smallest) | O(1) |
| `heapq.heappush(h, x)` | O(log n) |
| `heapq.heappop(h)` | O(log n) |
| `heapq.heapify(lst)` (in place, returns None) | **O(n)** |
| `heapq.nlargest(k, x)`, `nsmallest(k, x)` | O(n log k) |
| push n then pop n (heapsort) | O(n log n) |

- **Max-heap: negate.** Push `-x`, pop and flip back with `-heappop(h)`. Build with `h = [-x for x in nums]` then `heapify(h)`. (`heapify_max` only exists from Python 3.14.)
- **Tuples** compare first item, then second on ties: push `(priority, item)`.
- Only `h[0]` is guaranteed. `h[1]` is NOT necessarily the second smallest: pop twice.
- **Top k pattern:** push, and if `len(h) > k`, pop. Heap never grows past k → O(n log k).
- Anything pushed must be comparable with `<` (numbers, strings, tuples, objects with `__lt__`).

---

## 6. bisect (binary search)

`import bisect`. List must be **sorted**. Check the middle, throw away half, repeat.

| Operation | Big O |
|---|---|
| `bisect.bisect_left(nums, x)`: where x would go, before any copies | O(log n) |
| `bisect.bisect_right(nums, x)`: after any copies | O(log n) |
| `bisect.insort(nums, x)` | **O(n)**: finding is log n, inserting shifts |
| `x in sorted_nums` | still O(n): `in` doesn't know it's sorted |

- bisect only says **where**, not **whether**. Check `i < len(nums) and nums[i] == x`.
- Count of x: `bisect_right(nums, x) - bisect_left(nums, x)`.
- Count in [lo, hi]: `bisect_right(nums, hi) - bisect_left(nums, lo)`.

Binary search by hand (O(log n) time, O(1) space):
```python
left, right = 0, len(nums) - 1
while left <= right:              # <= : one item left still needs checking
    mid = (left + right) // 2
    if target < nums[mid]:
        right = mid - 1           # mid is ruled out, so -1
    elif target > nums[mid]:
        left = mid + 1            # mid is ruled out, so +1
    else:
        return mid                # found
return left                       # not found: left is the insert position
```
Without the ±1 the range stops shrinking when one item is left → infinite loop.

---

## 7. Sorting, enumerate, zip

| Operation | Big O |
|---|---|
| `sorted(x)` (new list) | O(n log n) |
| `nums.sort()` (in place, returns None) | O(n log n) |
| loop with `enumerate(nums)` or `zip(a, b)` | O(n) |

- Only need the smallest? `min` (O(n)), not sort (O(n log n)).
- `nums = nums.sort()` makes nums `None`.
- `key=` is a function run on each item: `sorted(words, key=len)`.
- `lambda x: x[1]` = tiny inline function returning `x[1]`.
- Two sort rules: return a tuple, `key=lambda w: (len(w), w)`.
- Biggest first for one part: negate it, `key=lambda p: (-p[1], p[0])`.
- Python's sort is **stable**: ties keep their original order, NOT alphabetical.
- `enumerate(nums)` gives `(index, item)` from one list: `for i, x in enumerate(nums)`.
- `zip(a, b)` pairs item 0 with 0, 1 with 1... stops at the shorter one silently.
- `dict(zip(names, scores))` builds a dict in one line.
- Unpacking: `name, age = pair`, `for count, num in heap`.
- `max(zip(names, scores), key=lambda p: p[1])[0]` = name with the top score.

---

## 8. Recursion

A function that calls itself on a smaller version of the problem.

- Needs a **base case** (answer straight away, stop) and a **step that gets smaller**.
- Each waiting call is a box on the **call stack**. n levels deep = **O(n) space**, even with no lists.
- Code **before** the recursive call runs going down. Code **after** runs coming back up, in reverse.
- `return f(n - 1)` as the last line means nothing after it ever runs.
- Each box has its own variables: `n = 0` at the top resets in every call.
- Python's limit ≈ **1000** deep → `RecursionError`. `sys.setrecursionlimit(x)` raises it (too high can crash Python). Safer: rewrite as a loop, O(1) stack space.
- Slicing in recursion isn't free: `sum_list(nums[1:])` copies each time → O(n²) time and space. Passing an index instead keeps it O(n).
- Often the cleanest base case is "nothing left": 0, empty list, empty string.

---

## Mistakes I made (don't repeat)

- `return print(x)` returns `None`. Return the value, print outside.
- Changing the caller's data: `.sort()`, `.pop()`, or editing inner lists. Use `sorted()` and copies (`x[:]`). `sorted()` is a **shallow** copy: inner lists are still shared.
- Comprehensions are for building a list I keep, not for printing. Use a `for` loop.
- `tuple(a, b)` crashes. A tuple from separate values is just `(a, b)`.
- `if nums in seen` instead of `if num in seen`.
- Forgetting `return` at the end of a function.
- Naming: `i` for an index only. `seen`, `need`, `word`, `groups` say what the thing is. Don't name variables `max`, `list`, `dict`.
- Big O: always give time AND space, and say what n is.
