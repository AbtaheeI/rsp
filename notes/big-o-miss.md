# Big O misses (CTCI VI, 17 Nov 2026)

## Examples I didn't get

| Example | What confused me | The fix |
|---|---|---|
| isPrime | Thought O(√n) simplifies to O(n) | √n is n^½, a different growth rate. Only multiplied constants and smaller added terms get dropped. log n < √n < n |
| 11 factorial | Thought computing n! means n! work | Only 1 recursive call per level, so it's a straight line of n calls. O(n) time, O(n) space |
| 12 permutations | Whole thing | n! leaves, at most n × n! calls in total, O(n) string work per call. Multiply to get O(n² × n!) |
| 14 allFib | Why it's not O(n × 2ⁿ) | fib(i) costs 2ⁱ and i grows: 2 + 4 + ... + 2ⁿ is under 2 × 2ⁿ, so O(2ⁿ). Same doubling sum as list append |

## Additional problems

| Q | I said | Answer | Why I was off |
|---|---|---|---|
| VI.1 | O(n) | O(b) | Used n when the inputs were a and b |
| VI.2 | O(n) | O(b) | Same as VI.1 |
| VI.4 | O(1) | O(a/b) | The while loop runs a variable number of times. Adds b until it passes a, so about a/b times |
| VI.5 | O(n) | O(log n) | Range gets halved each call, not reduced by 1 |
| VI.7 | O(2ⁿ) | O(n) | BST search goes one way at each node, so branches^depth doesn't apply. Worst unbalanced tree is a chain n deep |
| VI.8 | needed help | O(n) | No ordering rule means you can't skip anything, so you check every node |
| VI.10 | O(10√n), then O(n) | O(log n) | n is divided by 10 each pass, so it runs once per digit. Log base doesn't matter in Big O |
| VI.11 | c!, then kCc | O(k × cᵏ) | Letters can repeat, so each of the k slots has c choices: cᵏ strings, O(k) check each |
| VI.12 | O(n log n), then O(b log b × a log b) | O(b log b + a log b) | Two arrays need two variables. Sort runs once, then the loop runs, so add, don't multiply |

## Patterns to watch

- Two inputs means two variables. Never default to n.
- Check how the loop variable changes: minus 1 gives n, divided by 2 or 10 gives log n, squared against n gives √n.
- Recursion: count calls in the body. 1 call is a line, 2+ calls branch.
- "Then" means add, "for each" means multiply.
- When the cost per iteration changes, add up the real costs instead of multiplying by the worst one.