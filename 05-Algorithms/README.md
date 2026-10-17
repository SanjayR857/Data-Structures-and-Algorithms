# 05 - Algorithms

Algorithm paradigms, analysis, multi-language implementations, and correctness proofs.

## Subdirectories

```text
05-Algorithms/
├── README.md
├── 01-Searching/                     # Linear search, binary search, search on answer space
├── 02-Sorting/                       # Bubble, insertion, merge, quick, heap, counting/radix sort
├── 03-Divide-and-Conquer/            # Master theorem applications, Karatsuba, closest pair
├── 04-Greedy/                        # Activity selection, fractional knapsack, Huffman coding
├── 05-Backtracking/                  # N-Queens, Sudoku solver, subsets, permutations
├── 06-Dynamic-Programming/           # 1D DP, grid DP, knapsack 0/1, LCS, LIS, tree DP
├── 07-Graph-Algorithms/              # BFS, DFS, Dijkstra, Bellman-Ford, Kruskal, Prim, Topo sort
├── 08-String-Algorithms/             # KMP, Rabin-Karp, Z-algorithm, rolling hash
└── 09-Advanced-Algorithms/           # Convex hull, FFT, Max Flow / Ford-Fulkerson
```

---

## Standard Algorithm Template

Every algorithm folder follows the multi-language strategy demonstrated in [`02-Sorting/merge-sort/`](file:///c:/Users/User/Projects/repos/Python/Data-Structures-and-Algorithms/05-Algorithms/02-Sorting/merge-sort):
- **`explanation.md`**: Language-independent intuition, steps, recursion tree, and correctness proof.
- **`complexity.md`**: Best, average, worst-case derivations and auxiliary space requirements.
- **`examples.md`**: Worked dry-run traces with step-by-step array state diagrams.
- **`python.py` / `cpp.cpp` / `java.java`**: Idiomatic implementations in Python, C++, and Java.
- **`tests/`**: Unit tests covering empty inputs, single elements, duplicates, already sorted, and reversed inputs.
