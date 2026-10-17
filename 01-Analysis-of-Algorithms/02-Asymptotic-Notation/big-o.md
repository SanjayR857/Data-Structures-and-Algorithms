# Asymptotic Notation: Big-O ($O$)

## 1. Formal Definition
Let $f(n)$ and $g(n)$ be functions mapping positive integers to positive real numbers.
We say $f(n) \in O(g(n))$ if and only if there exist positive constants $c$ and $n_0$ such that:
$$0 \le f(n) \le c \cdot g(n) \quad \text{for all } n \ge n_0$$

- **Intuition:** $O(g(n))$ represents an **asymptotic upper bound**. It guarantees that an algorithm will never take more operations than some multiple of $g(n)$ as $n$ grows large.

---

## 2. Typical Growth Hierarchy

| Notation | Name | Practical Input Size ($N$) for 1-second limit | Example Scenarios |
| :--- | :--- | :--- | :--- |
| $O(1)$ | Constant | Any $N$ | Hash map lookup, array indexing |
| $O(\log n)$ | Logarithmic | $N \le 10^{18}$ | Binary search, balanced BST search |
| $O(n)$ | Linear | $N \le 10^7 - 10^8$ | Single scan, prefix sum calculation |
| $O(n \log n)$ | Linearithmic | $N \le 10^5 - 10^6$ | Merge sort, Heap sort, standard sorting |
| $O(n^2)$ | Quadratic | $N \le 5000$ | Nested loops, bubble sort, pairwise check |
| $O(2^n)$ | Exponential | $N \le 20 - 25$ | Subsets generation, naive recursion |
| $O(n!)$ | Factorial | $N \le 10 - 12$ | Permutations generation, Traveling Salesperson |

---

## 3. How to Derive Big-O from Code

### Step 1: Identify Elementary Operations
- Arithmetic, assignments, comparisons, and memory lookups are considered $O(1)$.

### Step 2: Sum Operations across Sequential Blocks
- $T(n) = T_1(n) + T_2(n) \implies O(\max(\text{degree}(T_1), \text{degree}(T_2)))$.

### Step 3: Multiply Operations across Nested Loops
- Outer loop executes $A$ times, inner loop executes $B$ times $\implies O(A \times B)$.

---

## 4. Common Misconceptions
- **Worst-case is NOT identical to Big-O:** Big-O is an upper bound on *any* function (best, worst, or average). An algorithm can have a Big-O for its best case ($O(1)$) and a Big-O for its worst case ($O(n)$).
- **Ignoring hidden constants in real systems:** An $O(n \log n)$ algorithm with heavy constant factors can run slower than an $O(n^2)$ algorithm for small $n$.
