# 03 - Programming Fundamentals

Core computational thinking prerequisites: recursion patterns, discrete mathematics for computer science, bitwise operations, memory allocation, and language idioms.

## Folder Structure

```text
03-Programming-Fundamentals/
├── README.md
├── 01-Recursion/
│   ├── base-case-and-call-stack.md    # Call stack visualization, activation records, stack overflow
│   ├── recursion-trees.md             # Visualizing branching recursion (Fibonacci, subsets)
│   └── tail-recursion.md              # Tail call optimization across languages
├── 02-Mathematics/
│   ├── gcd-lcm/                       # Euclidean algorithm and Extended Euclidean
│   ├── prime-numbers/                 # Trial division, Sieve of Eratosthenes, Miller-Rabin
│   ├── modular-arithmetic/            # Modular inverse, Fermat's Little Theorem, modulo 10^9+7
│   └── combinatorics/                 # Factorials, nCr, Catalan numbers, Pigeonhole principle
├── 03-Bit-Manipulation/
│   ├── bitwise-operators.md           # AND, OR, XOR, NOT, left/right shifts
│   ├── common-bit-tricks.md           # Check parity, clear lowest set bit (n & (n - 1)), power of two
│   └── bitmasking-subsets.md          # Representing states and subsets via integers
├── 04-Iteration-and-Invariants/
│   └── loop-invariants.md             # Proving correctness of loops
├── 05-Memory-and-References/
│   ├── pass-by-value-vs-reference.md  # How Python, C++, and Java handle object passing
│   ├── pointers-and-addresses.md      # C++ pointers, references, smart pointers
│   └── garbage-collection.md          # Java JVM GC, Python reference counting & cyclic GC
└── 06-Language-Fundamentals/
    ├── python/                        # Generators, list comprehensions, decorators, memory model
    ├── cpp/                           # Values, references, RAII, templates, operator overloading
    └── java/                          # Primitive vs Wrapper types, equals() vs ==, generics
```

## What to Write in Each Subfolder
1. **Mathematical Concepts:** Formula, derivation, proof of correctness, and implementation in all 3 languages.
2. **Bit Manipulation:** Exact bit tricks with a small 8-bit binary worked trace.
3. **Memory Models:** Diagram showing Stack vs Heap for Python names, C++ variables, and Java references.
