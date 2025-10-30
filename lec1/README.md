
---

##Numerical Methods in Python

This first lesson teaches you **how numbers actually work inside a computer** — especially how **Python handles floating-point numbers (decimal numbers)**.
You’ll see how computers sometimes make **tiny mistakes** with decimal numbers because of how they’re stored in binary form (0s and 1s).

---

## Table of Contents

1. [Basic Operations](#basic-operations)
2. [Explore Floating Point Precision](#explore-floating-point-precision)
3. [Precision Spacing](#precision-spacing)
4. [Cumulative Rounding Error](#cumulative-rounding-error)

---

##  1. Basic Operations (File: `Basic_Operations.py`)

### ➤ import math

This brings in Python’s **math module** — it contains many math functions like `sqrt()`, `cos()`, `pi`, etc.

You could explore it using:

```python
help(math)   # Shows documentation
dir(math)    # Shows all functions inside math
```

### ➤ Simple arithmetic

```python
print("2 + 3 =", 2 + 3)     # 5
print("2 * 3 =", 2 * 3)     # 6
print("2 ** 3 =", 2**3)     # 8 (power)
print("20 - 3 =", 20 - 3)   # 17
print("20 / 3 =", 20 / 3)   # 6.6666...
```

These are the basic math operations in Python.

### ➤ Order of operations

```python
print("(3 * 4) / (2**2 + 4/2) =", (3 * 4) / (2**2 + 4/2))
```

Here parentheses decide the order:

* ( (3×4) = 12 )
* ( 2^2 + 4/2 = 4 + 2 = 6 )
* ( 12 ÷ 6 = 2.0 )

---

### ➤ Using `math` module

```python
print("Square root of 9 =", math.sqrt(9))           # 3.0
print("cos(pi/3) =", math.cos(math.pi / 3))         # 0.5
print("e^log(10) =", math.exp(math.log(10)))        # 10.0
print("e^log10(10) =", math.exp(math.log(10, 10)))  # 2.718...
```

 Notes:

* `math.sqrt(9)` → √9 = 3
* `math.cos(math.pi / 3)` → cos(60°) = 0.5
* `math.exp(math.log(10))` → ( e^{\ln(10)} = 10 )
* `math.log(10, 10)` = log base 10 of 10 = 1 → ( e^1 = 2.718... )

---

### ➤ Infinity and NaN

```python
print("1 / infinity =", 1 / math.inf)         # 0.0
print("2 * infinity =", 2 * math.inf)         # inf
print("infinity / infinity =", math.inf / math.inf) # nan
```



* `inf` = infinity
* `nan` = Not a Number (undefined result)

---

### ➤ Complex numbers

```python
print("2 + 5j =", 2 + 5j)
print("complex(2, 5) =", complex(2, 5))
```

Two ways to write the same complex number:
( 2 + 5i ) → real part = 2, imaginary part = 5

---

## 2. Explore Floating Point Precision (File: `Explore_Floating_Point_Precision.py`)

### ➤ import sys, numpy

Used for checking system information and doing numerical operations.

```python
print(sys.float_info)
```

This gives details like:

* **max** – largest float value
* **min** – smallest positive float
* **epsilon** – the smallest difference that Python can detect between 1.0 and the next representable number
* **digits** – how many digits can be stored accurately

**Meaning:**
Computers can’t store *every possible decimal number* exactly — only those that fit into their binary format.
That’s why precision has a limit.

---

##  3. Precision Spacing (File: `Precision_Spacing.py`)

### ➤ Floating-point problem

```python
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3?", (0.1 + 0.2) == 0.3)
```

You might expect 0.3, but the result is:

```
0.1 + 0.2 = 0.30000000000000004
0.1 + 0.2 == 0.3? False
```

 Why?
Because 0.1 and 0.2 cannot be perfectly represented in binary — the computer stores an *approximation*, so tiny errors appear.

---

### ➤ Machine epsilon at 1.0

```python
gap_at_one = np.spacing(1)
print("Gap at 1.0:", gap_at_one)
```

Machine epsilon is the **smallest possible difference** between two numbers near 1.0 that the computer can distinguish.

Then we test:

```python
1.0 == (1.0 + gap_at_one/2)  # True
1.0 == (1.0 + gap_at_one)    # False
```

That means:

* Adding half of epsilon → still same number
* Adding full epsilon → becomes different number

---

### ➤ Machine epsilon for big numbers

```python
num = 1e9
gap = np.spacing(num)
print("Gap at 1e9:", gap)
```

The “gap” increases as the number gets bigger.
So for very large numbers, small differences are ignored — **precision decreases**.

---

## 4. Cumulative Rounding Error (File: `Cumulative_Rounding_Error.py`)

### ➤ Function definition

```python
def add_and_subtract(iterations):
    result = 1
    for i in range(iterations):
        result += 1 / 3
    for i in range(iterations):
        result -= 1 / 3
    return result
```

Mathematically, after adding and subtracting the same amount many times, result should be exactly 1.
But in computers, rounding errors build up little by little.

### ➤ Test it

```python
print(add_and_subtract(100))
print(add_and_subtract(1000))
print(add_and_subtract(10000))
```

As you increase iterations, result slightly moves away from 1.0 — this is **cumulative rounding error**.

---

##  Key Takeaways (Easy Version)

| Concept                                    | Meaning                                                            |
| ------------------------------------------ | ------------------------------------------------------------------ |
| **Floating-point arithmetic is not exact** | Computers can’t store all decimals exactly (e.g., 0.1 + 0.2 ≠ 0.3) |
| **Precision decreases for big numbers**    | Big numbers have larger gaps between representable values          |
| **Cumulative rounding error**              | Tiny errors add up in repeated operations                          |
| **Never use `==` to compare floats**       | Use a small tolerance like: `abs(a - b) < 1e-9`                    |
| **Understand limitations**                 | Helps in writing accurate numerical programs                       |

---


