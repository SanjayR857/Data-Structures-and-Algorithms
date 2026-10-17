# 09 - Competitive Programming

Speed-optimized routines, advanced mathematical algorithms, fast I/O boilerplate, and contest post-mortems for platforms like Codeforces, AtCoder, and CodeChef.

---

## Directory Organization

```text
09-Competitive-Programming/
├── README.md
├── number-theory/             # Fast exponentiation, Sieve, Extended GCD, Euler Totient
├── combinatorics/             # Precomputed factorials, inverse factorials, Lucas theorem
├── advanced-data-structures/  # Fenwick Tree, Segment Tree (Lazy), Treap, Sparse Table
├── contest-templates/         # Fast I/O snippets, macro headers for C++, Python, Java
├── contest-solutions/         # Grouped by contest ID (e.g., cf-div2-950/)
└── editorials-and-learnings/  # Post-contest retrospectives and upsloved problems
```

---

## Guidelines for Competitive Programming
1. **Contest Templates:** Keep templates lightweight and clean. For C++, always disable stream synchronization:
   ```cpp
   std::ios_base::sync_with_stdio(false);
   std::cin.tie(NULL);
   ```
2. **Upsolving Discipline:** After every contest, solve at least 1 problem beyond what you solved during the contest. Document the editorial insight in `editorials-and-learnings/`.
