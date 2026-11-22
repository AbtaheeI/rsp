# ADM Chapter 1, sections 1.1 to 1.4

## Key terms

- **Algorithm:** always gives the correct answer
- **Heuristic:** usually does OK, no guarantee
- **Counterexample:** one input where an algorithm gives the wrong answer. One is enough to prove it wrong
- **Induction:** base case + assume smaller cases work + show n works. Proves an algorithm right

## 1.1 Robot tour (TSP)

Visit every point and return, shortest total path.

| Approach | Result | Breaks on |
|---|---|---|
| Nearest neighbour | Wrong | Points on a line: -21, -5, -1, 0, 1, 3, 11. Zig-zags across 0 |
| Closest pair | Wrong | Two rows slightly closer together (1 - e) than points within a row (1 + e). Over 20% too long |
| Try every ordering | Correct | Too slow: n! orderings |

No known algorithm is both correct and fast for TSP.

## 1.2 Movie scheduling

Pick the most jobs with no overlaps.

| Approach | Result | Breaks on |
|---|---|---|
| Earliest start | Wrong | (1,10), (2,3), (4,5), (6,7). Long job starts first, blocks 3 short ones |
| Shortest job | Wrong | (1,5), (4,7), (6,11). Short job blocks 2 long ones |
| Fewest overlaps | Wrong | Fig 1.7. Stacks on the end jobs make a bad middle job look safest |
| Try every subset | Correct | Too slow: 2^n subsets |
| **Earliest end** | **Correct and fast** | O(n log n): sort by end time, one pass |

Why earliest end works: the job that ends first frees you up soonest. Swapping it into any best schedule keeps the schedule valid with the same number of jobs, so taking it never costs anything.

```python
def overlaps(a, b):
    return not (b[0] >= a[1] or a[0] >= b[1])

def optimal_scheduling(jobs):
    accepted = []
    for j in sorted(jobs, key=lambda x: x[1]):     # sort by end time
        if not accepted or not overlaps(accepted[-1], j):
            accepted.append(j)
    return accepted
```

## 1.3 Reasoning about correctness

**Problem spec has two parts:** allowed inputs, and what the output must satisfy. Fuzzy problem means you can't prove anything. Watch for inputs that are too broad, vague goals ("best route"), and compound goals ("shortest with fewest turns").

**Writing algorithms:** English, pseudocode or code. Use whatever shows the idea most clearly. Don't use pseudocode to dress up a vague idea.

**Good counterexamples are** verifiable (you can show the algorithm's answer and a better one) and simple.

**Tactics for finding counterexamples:**

| Tactic | Idea |
|---|---|
| Think small | Failures show up on tiny inputs |
| Think exhaustively | Try every arrangement for small n. Two intervals: apart, overlapping, nested |
| Hunt for the weakness | For "always take the biggest/smallest", ask when that's the wrong move |
| Go for a tie | Make everything equal so the rule has nothing to decide on |
| Seek extremes | Huge vs tiny, near vs far |

## 1.4 Induction and recursion

| Induction | Recursion |
|---|---|
| Base case | `if n <= 1: return` |
| Assume smaller cases work | Call on a smaller input, trust it |
| Show n works | Use that result to finish |

**Insertion sort proof:** 1 element is sorted. Assume first n - 1 sorted. Insert x into its one correct spot, so n are sorted.

**Increment(y) proof:** even y returns y + 1. Odd y = 2m + 1 returns 2 * Increment(m) = 2(m + 1) = y + 1. Because m is about half of y, assume it works for **all** smaller numbers, not just n - 1 (strong induction).

**Where induction goes wrong:** bad base case or boundaries, and assuming one more item just extends the n - 1 answer. Fig 1.8: adding one job can change the whole best schedule.

## Takeaways

- Reasonable-looking algorithms are often wrong. "It's obvious" is not a proof
- Counterexamples prove algorithms wrong, induction proves them right
- Sometimes a correct and fast algorithm exists (scheduling), sometimes it doesn't (TSP)