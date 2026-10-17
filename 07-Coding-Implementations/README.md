# 07 - Coding Implementations

Centralized, language-specific codebases organizing pure, reusable implementations of core Data Structures, Algorithms, and utility helpers across Python, C++, and Java.

---

## Directory Organization

```text
07-Coding-Implementations/
├── README.md
├── python/
│   ├── data-structures/       # DynamicArray, LinkedList, BinaryHeap, Trie, Graph
│   ├── algorithms/            # Sorting, BinarySearch, Dijkstra, TopologicalSort
│   └── utilities/             # Timer decorators, random array generators, tree printers
├── cpp/
│   ├── data-structures/       # Template headers (.hpp) and implementations
│   ├── algorithms/            # STL-compatible algorithms
│   └── utilities/             # Benchmark harness, fast I/O setup, pretty printers
└── java/
    ├── data-structures/       # Generic data structure classes
    ├── algorithms/            # Static algorithm utility classes
    └── utilities/             # Matrix visualizer, test case generators
```

---

## Language Specifications & Standards

| Language | Target Standard | Compiler / Runtime | Package / Module Style |
| :--- | :--- | :--- | :--- |
| **Python** | Python 3.10+ | CPython | Type hints (`typing`), snake_case |
| **C++** | C++17 / C++20 | GCC / Clang / MSVC | STL style, header guards, namespaces |
| **Java** | Java 17+ (LTS) | OpenJDK 17+ | Standard packages, PascalCase classes |

---

## What to Write in Each File
- Clean, production-style code without competitive programming hacks (avoid `#define int long long` here).
- Full docstrings / Javadoc / Doxygen comments specifying preconditions, parameters, returns, and complexities.
- Unit tests co-located or linked.
