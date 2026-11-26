## Question 6.1

### 1. Correctness

The algorithm **is correct**.

Use the following loop invariant for the outer loop:

> **Invariant \(I(i)\):** After the \(i\)-th iteration of the outer loop, the prefix \(A[1..i]\) is sorted in nondecreasing order, and \(A[i]\) is the maximum element of the whole array.

**Initialization.** For \(i=0\), the prefix is empty, so the invariant holds trivially.

**Maintenance.** Assume \(I(i-1)\) holds. At the beginning of iteration \(i\), \(A[1..i-1]\) is sorted. The inner loop compares \(A[i]\) with every \(A[j]\). Whenever \(A[i]<A[j]\), it swaps them. This has two effects:

- The elements \(A[1..i-1]\) together with the original \(A[i]\) are rearranged into sorted order in \(A[1..i]\).
- The maximum element of the entire array is moved into position \(A[i]\).

Thus after iteration \(i\), \(A[1..i]\) is sorted and \(A[i]\) is the global maximum, so \(I(i)\) holds.

**Termination.** When \(i=n\), the invariant says \(A[1..n]\) is sorted. Hence the algorithm sorts correctly.

### 2. Runtime

There are two nested loops, each running \(n\) times. The comparison and possible exchange take constant time. Hence the runtime is

\[
\Theta(n^2).
\]

---

## Question 6.2

The array is

\[
A=[12,10,4,2,9,6,5,25,8].
\]

Its sorted order is

\[
2,4,5,6,8,9,10,12,25.
\]

Thus the ranks are:

\[
\begin{array}{c|ccccccccc}
\text{element} & 2 & 4 & 5 & 6 & 8 & 9 & 10 & 12 & 25\\
\hline
\text{rank} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9
\end{array}
\]

In randomized quicksort, for two elements with ranks \(r_x\) and \(r_y\),

\[
\Pr(x\text{ and }y\text{ are compared})
=
\frac{2}{|r_x-r_y|+1}.
\]

1. \(A[2]=10\) has rank \(7\), \(A[3]=4\) has rank \(2\):

\[
\Pr=\frac{2}{|7-2|+1}=\frac{2}{6}=\boxed{\frac13}.
\]

2. \(A[1]=12\) has rank \(8\), \(A[8]=25\) has rank \(9\):

\[
\Pr=\frac{2}{|8-9|+1}=\frac{2}{2}=\boxed{1}.
\]

3. \(A[4]=2\) has rank \(1\), \(A[8]=25\) has rank \(9\):

\[
\Pr=\frac{2}{|1-9|+1}=\frac{2}{9}.
\]

\[
\boxed{\frac29}
\]

4. \(A[2]=10\) has rank \(7\), \(A[7]=5\) has rank \(3\):

\[
\Pr=\frac{2}{|7-3|+1}=\frac{2}{5}.
\]

\[
\boxed{\frac25}
\]

---

## Question 6.3

Let \(C\) be the number of comparisons made by randomized quicksort. For two elements with ranks \(i<j\), the probability that they are compared is

\[
\frac{2}{j-i+1}.
\]

Therefore

\[
\mathbb E[C]
=
\sum_{1\le i<j\le n}\frac{2}{j-i+1}.
\]

Set \(d=j-i\). For each \(d=1,\dots,n-1\), there are \(n-d\) pairs with distance \(d\). Hence

\[
\mathbb E[C]
=
\sum_{d=1}^{n-1}(n-d)\frac{2}{d+1}.
\]

Now restrict to the first \(\lfloor n/2\rfloor\) terms. For \(1\le d\le \lfloor n/2\rfloor\), we have \(n-d\ge n/2\). Thus

\[
\mathbb E[C]
\ge
\frac n2\sum_{d=1}^{\lfloor n/2\rfloor}\frac{2}{d+1}
=
n\sum_{d=1}^{\lfloor n/2\rfloor}\frac{1}{d+1}
=
\Omega(n\log n).
\]

Since the runtime is proportional to the number of comparisons, the expected runtime of randomized quicksort is

\[
\boxed{\Omega(n\log n)}.
\]

---

## Question 6.4

For \(n=3\), let the initial array be \([a,b,c]\). Selection sort first compares \(b<a\), then compares \(c\) with the smaller of \(a,b\), and finally compares the last two remaining elements after the first swap.

A decision tree is:

```text
b < a?
├── yes: c < b?
│   ├── yes: c < b < a        leaf: [c,b,a]
│   └── no : b < c < a        leaf: [b,c,a]
└── no : c < a?
    ├── yes: c < a < b        leaf: [c,a,b]
    └── no : a < c?
        ├── yes: a < c < b    leaf: [a,c,b]
        └── no : a < b < c    leaf: [a,b,c]
```

The sixth permutation \(b<a<c\) is obtained on the branch \(b<a\) is false, \(c<a\) is false, and then the final comparison of the remaining two elements distinguishes \(a<b<c\) from \(b<a<c\). Including that final comparison explicitly gives the full tree with six leaves, one for each permutation:

\[
[a,b,c],\ [a,c,b],\ [b,a,c],\ [b,c,a],\ [c,a,b],\ [c,b,a].
\]

Each internal node is a comparison; each leaf is a possible input permutation.

---

## Question 6.5

The smallest possible depth of a leaf in a decision tree for a comparison sort is

\[
\boxed{n-1}.
\]

Reason: to determine the total order of \(n\) distinct elements, the comparison graph must be connected. A connected graph on \(n\) vertices has at least \(n-1\) edges, so at least \(n-1\) comparisons are necessary. This bound is achieved, for example, by insertion sort on an already sorted input, which performs exactly \(n-1\) comparisons. Hence the minimum possible leaf depth is \(n-1\).