# HeapSort

**Idea**: Find the largest/smallest elements

a heap on an array:

child: $i$

parent: $\lfloor \frac{i}{2} \rfloor$

Heap properties:

- Max-heap property: $A[parent(i)] > A[i]$
- the root stores a largest element;

## Procedures

1. Build Max Heap
2. Max-Heapify
3. HeapSort

Max-Heapify: for every element, if $LargestChild > Parent$, replace them. Then go to the next layer.
- Runtime: $O(log n)$

#### Correctness:**Recurrence Invariant**

Build Max Heap: **from bottom to top, max heapify the elements.**

Note: there are at most $\lceil \frac{x}{2^{n + 1}} \rceil$ nodes of height $h$.


