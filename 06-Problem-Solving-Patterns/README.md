# 06 - Problem-Solving Patterns

Algorithmic patterns are reusable meta-strategies for decomposing complex interview problems into standard, recognizable mechanics.

---

## Pattern Directory Map

```text
06-Problem-Solving-Patterns/
├── README.md
├── 01-Two-Pointers/                # Left-right converge, slow-fast runner, two sorted inputs
├── 02-Sliding-Window/              # Fixed size, dynamic shrinking, minimum window
├── 03-Prefix-Sum/                  # 1D prefix sum, 2D matrix sum, prefix XOR
├── 04-Fast-and-Slow-Pointers/      # Floyd's cycle detection, middle of linked list, happy number
├── 05-Monotonic-Stack-and-Queue/   # Next greater element, largest rectangle in histogram
├── 06-Intervals/                   # Merge intervals, insert interval, non-overlapping intervals
├── 07-Binary-Search-Patterns/      # Exact search, lower/upper bounds, search on answer domain
├── 08-BFS-and-DFS/                 # Shortest path in unweighted graph, connected components
├── 09-Backtracking-Patterns/       # Subsets (choose/explore/unchoose), permutations, pruning
├── 10-Dynamic-Programming-Patterns/# 0/1 Knapsack, Unbounded Knapsack, LCS, LIS, Interval DP
├── 11-Top-K-Elements/              # Min-heap for K largest, Max-heap for K smallest, Quickselect
├── 12-Union-Find/                  # Redundant connection, accounts merge, number of islands II
└── 13-Bitmasking/                  # Subsets generation, Travelling Salesperson DP, bit tricks
```

---

## Pattern Template (What to Write in Each Pattern Folder)
1. **Identification Clues:** Verbal keywords in problem descriptions that trigger this pattern.
2. **Mental Model:** Conceptual visualization (e.g., an expanding and contracting caterpillar).
3. **Canonical Code Template:** Generic boilerplate in Python, C++, and Java.
4. **Variations & Edge Cases:** Fixed vs variable window, empty input, negative numbers.
5. **Canonical Benchmark Problems:** 3 to 5 classic problems showcasing the pattern.
