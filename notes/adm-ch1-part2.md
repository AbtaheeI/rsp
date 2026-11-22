# ADM Chapter 1, sections 1.5 to 1.9

## 1.5 Modelling the problem

Restate a real problem in terms of a standard structure, then look up what's known about it. Modelling is the most important single step towards a solution.

- Some real details won't fit the model. Ignore them for a moment and check if they actually matter
- The same problem can be modelled several ways, some much better than others

### 1.5.1 Combinatorial objects

| Object | What it is | Clue words |
|---|---|---|
| Permutation | an ordering, order matters | arrangement, tour, ordering, sequence |
| Subset | a selection, order doesn't matter | group, collection, committee, selection |
| Tree | a hierarchy | hierarchy, ancestor/descendant, taxonomy |
| Graph | connections between pairs | network, circuit, web, relationship |
| Point | a location | sites, positions, locations, data records |
| Polygon | a region or shape | shapes, regions, boundaries |
| String | a sequence of characters | text, characters, patterns, labels |

Robot tour = permutation. Movie scheduling = subset.

### 1.5.2 Recursive objects

Big things made of smaller things of the same type. Remove a piece and you still have the same kind of object:

- Permutation: drop the first element, get a permutation of n - 1
- Subset: drop element n, get a subset of {1, ..., n - 1}
- Tree: drop the root, get smaller trees
- Graph: drop a vertex or cut it in two, get smaller graphs
- Points / polygons: split with a line, get two smaller ones
- String: drop the first character, get a shorter string

That's why recursion fits so many problems.

## 1.6 Proof by contradiction

1. Assume the opposite of what you want to prove
2. Follow the logic
3. Hit something impossible
4. So the original claim is true

**Infinitely many primes:** assume the list p1, ..., pn is complete. Let m = (p1 x ... x pn) + 1. Dividing m by any listed prime leaves remainder 1, so none divide it. So m is a new prime, or has a prime factor not on the list. Either way the list wasn't complete. Contradiction.

Example: list = 2, 3, 5. m = 31, which is prime and not on the list.

The contradiction has to be clearly, obviously false, and it has to follow logically from the assumption.

| Induction | Contradiction |
|---|---|
| Build up from the smallest case | Assume false, show that breaks |
| "True for every n", recursive algorithms | "This can't exist", "there's no limit" |

## 1.7 and 1.8 War story: psychic modelling

**Problem:** psychic picks 15 numbers and promises at least 4 will win. Tickets have 6 numbers, a prize needs 3 matches. Find the fewest tickets that guarantee a prize.

**Wrong model:** cover every group of 3 from the 15. Correct but needed far too many tickets.

**What they missed:** 4 winners contain four groups of 3. You only need a ticket covering one of them.

**Small version:** numbers 1 to 5, 3 per ticket, need 2 matches. Covering every pair takes 4 tickets. With 3 guaranteed winners, {1,2,3} and {1,4,5} are enough.

**Moral:** check your model on a tiny example by hand, and with the client, before writing code. Building from clean general pieces made the fix quick.

## 1.9 Estimation

Principled guessing. Two methods:

- **Principled calculation:** work it out from things you know, can look up, or can confidently guess
- **Analogy:** compare to something similar you've seen

**Coin jar (real answer 1879):**
- Volume: about 1962
- Weight: 10 lb x 181 pennies per lb = 1810
- Analogy with penny rolls: about 1000

**Best practice:** estimate the same thing 2 or 3 different ways and check they roughly agree, within a factor of 2 to 10. The reasoning matters more than the exact number.

## Takeaways

- Model the problem as a standard structure before solving it
- Most standard structures are recursive, which is why recursion is everywhere
- Contradiction: assume false, show it breaks
- Test your model on a small hand example before coding
- Estimate several ways and compare