Binary index tree
-----------------

We are given an array of integers `arr[0 ... n-1]`.

We have two operations:

1. **Query**: Compute the sum of the first $i$ values in `arr`.
2. **Update**: For some $0 \le i \le n-1$, set `arr[i] = x`.

We would like to perform both operations in $\mathcal{O}(\log{}n)$ time.

---

The binary index tree data structure is a wrapper around an array `bin` of length $n+1$. With respect to `bin`:

`bin[0]` is a dummy element. Data is stored in the binary index tree in indices 1 up to and including $n$.

Define `array[m, n)` to be the subsequence of `array` on the half-open interval $[m,n)$.

Each element at `bin[i]` is the sum of the values in `arr[i', i)` where `i'` equals `i` with its least-significant non-zero bit flipped.

To find the least-significant bit of `x`, we take `x & -x`.

Proof: We can write a number $n$ in base-2 as $a1b$, where $b$ is a (possibly empty) string of zeroes. 
