# 01 - Analysis of Algorithms

This section contains mathematical foundations for evaluating algorithmic efficiency: time bounds, space overhead, recurrence analysis, and correctness proofs.

## Folder Contents & Structure

```text
01-Analysis-of-Algorithms/
├── README.md
├── 01-Algorithm-Fundamentals/
│   └── README.md                    # What is an algorithm, pseudo-code standards, loop invariants
├── 02-Asymptotic-Notation/
│   ├── README.md
│   ├── big-o.md                     # Upper bound definition, formal math, proofs, examples
│   ├── big-omega.md                 # Lower bound definition and formal math
│   ├── big-theta.md                 # Tight bound definition and conditions
│   └── asymptotic-comparison.md     # Ordering standard functions (1, log n, n, n log n, n^2, 2^n, n!)
├── 03-Time-Complexity/
│   ├── constant-logarithmic-linear.md
│   ├── polynomial-complexity.md
│   ├── nested-loops.md
│   └── best-average-worst-case.md
├── 04-Space-Complexity/
│   └── README.md                    # Stack frames, auxiliary vs total space, in-place definition
├── 05-Recurrence-Relations/
│   └── README.md                    # Substitution method, recursion tree method
├── 06-Master-Theorem/
│   └── README.md                    # Standard Master Theorem cases and limitations
├── 07-Amortized-Analysis/
│   └── README.md                    # Aggregate method, accounting method, potential method
├── 08-Algorithm-Correctness/
│   └── README.md                    # Loop invariants, termination proofs, inductive proofs
└── 09-Complexity-Analysis-Exercises/
    └── README.md                    # 20+ loop analysis drills and recurrence problems
```

## What to Write in Each File
- **Formal Definition:** Mathematical formulation ($f(n) \le c \cdot g(n)$ for $n \ge n_0$).
- **Intuition:** Plain English analogy without heavy math.
- **Common Code Snippets:** Loop patterns that produce this complexity.
- **Visuals / Graphs:** ASCII or SVG plots showing function growth rates.
