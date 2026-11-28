# CTCI VII–VIII: Technical Questions, The Offer and Beyond

## Chapter VII: Technical Questions

### The must-know list (p. 61)

| Data structures | Algorithms | Concepts |
|---|---|---|
| Linked lists | Breadth-first search | Bit manipulation |
| Trees, tries and graphs | Depth-first search | Memory (stack vs heap) |
| Stacks and queues | Binary search | Recursion |
| Heaps | Merge sort | Dynamic programming |
| Vectors / ArrayLists | Quick sort | Big O time and space |
| Hash tables | | |

What each one is, in one line:

- **Linked list:** a chain where each item points to the next. Fast at the ends, slow to find things in the middle
- **Trees / tries / graphs:** hierarchies / trees of letters for words / things connected in any pattern
- **Stack / queue:** last in, first out (a pile of plates) / first in, first out (a line at a shop)
- **Heap:** a tree that keeps the smallest (or biggest) item on top for fast access
- **Vector / ArrayList:** an array that grows by doubling. Python's `list`
- **Hash table:** key-to-value lookup in O(1). Python's `dict`
- **BFS / DFS:** explore a graph level by level / as deep as possible first
- **Binary search:** halve a sorted list each step, O(log n)
- **Merge sort:** split, sort the halves, merge, O(n log n)
- **Quick sort:** pick a pivot, smaller on the left and bigger on the right, repeat. O(n log n) on average
- **Bit manipulation:** working with a number's 1s and 0s directly
- **Stack vs heap memory:** the call stack holds function calls, the heap holds longer-lived objects
- **Dynamic programming:** recursion that saves answers so nothing is recomputed

For each data structure: know how to **implement** it, how to **use** it, and its **Big O** for each operation.

### Powers of 2

| Power | Exact | Roughly | Memory |
|---|---|---|---|
| 2^7 | 128 | | |
| 2^8 | 256 | | |
| 2^10 | 1,024 | 1 thousand | 1 KB |
| 2^16 | 65,536 | | 64 KB |
| 2^20 | 1,048,576 | 1 million | 1 MB |
| 2^30 | 1,073,741,824 | 1 billion | 1 GB |
| 2^32 | 4,294,967,296 | | 4 GB |
| 2^40 | 1,099,511,627,776 | 1 trillion | 1 TB |

Every 10 powers of 2 is about 1,000x.

### The 7-step method

| Step | Do this |
|---|---|
| 1. Listen | catch every detail. "Sorted", "unique" or "fits in memory" are usually clues |
| 2. Example | make your own: big enough, and not a special case |
| 3. Brute force | say the slow, obvious solution and its Big O straight away |
| 4. Optimise | BUD and the techniques below |
| 5. Walk through | get the whole approach clear before writing code |
| 6. Implement | clean, modular code with good names |
| 7. Test | trace it by hand, then fix bugs carefully (find the cause, don't guess) |

### BUD

| | Look for | Example |
|---|---|---|
| **B**ottlenecks | the slowest step, which sets the overall Big O | an O(n log n) sort makes speeding up an O(n) loop pointless |
| **U**nnecessary work | things you compute but don't need | carrying on after the answer is found |
| **D**uplicated work | the same thing computed over and over | recursive Fibonacci, fixed with memoisation |

### Other optimisation techniques

| Technique | Idea |
|---|---|
| **DIY** | solve a big example by hand, notice what you naturally did, and turn that into the algorithm. Example: finding permutations of `s` in `b`, where by hand you slide a window and compare letter counts instead of generating every permutation |
| **Simplify and generalise** | solve an easier version first, then adapt it |
| **Base case and build** | solve n = 1, then n = 2, and build up (induction thinking) |
| **Data structure brainstorm** | go through the must-know list: would a hash table help? A heap? |
| **BCR** | see below |

### Best Conceivable Runtime (BCR)

The fastest **any** solution could possibly be. Usually that's "you have to look at every input at least once".

- Unsorted list of n, any item could matter: O(n)
- Two arrays A and B: O(A + B)
- Searching a sorted list: O(log n)

**BCR is not best case.** Best case is one algorithm on a lucky input. BCR is the floor for the problem itself.

How it helps:
1. **Your solution matches the BCR:** time can't improve, so stop (and improve space if you want)
2. **It hints at the shape:** O(n) means one or two passes, so think hash tables or two pointers, not nested loops
3. **Anything at or below the BCR is free:** extra O(n) passes don't hurt an O(n) solution

Example: common elements in two sorted arrays. BCR O(A + B). Brute force O(A x B), then binary search O(A log B), then a hash set O(A + B) (matches, uses space), then walking both sorted arrays together O(A + B) with no extra space.

### Testing on paper

In interviews you often can't run code, so trace it by hand.

| Kind | Example inputs |
|---|---|
| General case | a normal input, like `[3, 7, 2]` |
| Base case | smallest inputs: empty, one item, zero |
| Error case | bad input: `None`, negatives, wrong type |
| Edge cases | duplicates, all the same, already sorted, all negative, answer at the start or end |

Write the variable values down as you go. On LeetCode, trace one normal, one tiny and one weird input **before** pressing Run.

### Error checks

Code that guards against bad input. To save time in an interview, leave a `# TODO` where they'd go and **say out loud** what you'd check. It shows you thought about it, and the interviewer can ask you to add them.

### What good code looks like

Correct, efficient, simple, readable, maintainable. Use good data structures, reuse code, keep it modular, make it flexible, and include error checks.

### Other advice

- **Heard the question before?** Say so. Hiding it is dishonest
- **Don't give up** on hard questions. Showing how you tackle them is the point
- **Mistakes are normal.** Interviewers judge you relative to other candidates on the same question

---

## Chapter VIII: The Offer and Beyond

### Rejection

- It's common, and doesn't mean you're bad. Interviews are noisy
- You can usually reapply after 6 to 12 months

### Offer deadlines

- Ask for more time if you need it, especially to line up other interviews

### Evaluating an offer

- **Money:** base salary, signing bonus, relocation, bonuses, stock. Cost of living matters
- **Career growth:** what you'll learn, how the role builds your resume
- **Company stability:** how established and secure it is
- **Happiness:** the team, the manager, the product, the hours

### Negotiating

- Always do it, politely. It rarely costs you the offer
- Having another offer gives you leverage
- Be specific about what you want
- Ask for more than you expect

### On the job

- Have a career plan and a timeline
- Build strong relationships with your manager and team
- Ask for what you want
- Keep interviewing occasionally, so you know your options
