
---

## Numerical Methods in Python 

This project shows **how computers make small mistakes** when doing math — not because they’re wrong, but because they can’t use infinite numbers or perfect measurements.
We’ll see **two types of errors** 

---

## Taylor’s Series Truncation Error

### What are we trying to do?

We want to calculate **sin(x)** — like **sin(90°)** — but instead of using the ready-made formula,
we’ll try to **approximate** it using a mathematical series called the **Taylor Series**.

---

### What is Taylor Series?

It’s like breaking a hard formula into **many smaller parts** (terms) that are easy to calculate.
For example:

[
\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots
]

Each part (term) makes the answer more and more accurate.
If you stop early (take only a few terms), your answer will be **close** but not **perfect** — that’s called **truncation error**.

---

### How the Python program works step by step

#### Step 1: Import tools

```python
import math
import numpy as np
```

* `math` → helps with formulas like sin() and factorial()
* `numpy` → gives us π (pi = 3.14159...)

---

#### Step 2: Make a function to calculate sin(x)

```python
def taylor_approximation(x_value, num_terms):
    approx_val = 0
    for n in range(num_terms):
        term = (((-1) ** n) * (x_value ** (2 * n + 1))) / math.factorial(2 * n + 1)
        approx_val += term
    return approx_val
```

What it does:

* It adds each piece of the series one by one.
* `(-1)**n` makes the sign change (+, −, +, −, …).
* `x_value ** (2*n+1)` means x¹, x³, x⁵, etc.
* `math.factorial(2*n+1)` divides by 1!, 3!, 5!, etc.
* Adds all these up to get an **approximate sin(x)**.

---

#### Step 3: Choose a value for x

```python
x_point = np.pi / 2
```

That means ( x = \pi/2 = 1.57 ) radians (same as **90 degrees**).

The **true sin(90°)** is exactly **1**.

---

#### Step 4: Check how good our approximation is

```python
num_term_list = [1, 3, 5, 7, 9]
for terms in num_term_list:
    approx_sin_val = taylor_approximation(x_point, terms)
    truc_error = abs(true_sin_val - approx_sin_val)
    print(f"Approximation With {terms} terms: {approx_sin_val:.8f}, Truncation Error: {truc_error:.8f}")
```

This means:

* Try using 1 term, then 3, 5, 7, and 9 terms.
* For each, calculate how close it is to the **true value** (1).
* Show the **difference** (the error).

---

### Example Result

| Number of Terms | Approximation | Error  |
| --------------- | ------------- | ------ |
| 1 term          | 1.5708        | 0.5708 |
| 3 terms         | 0.9248        | 0.0752 |
| 5 terms         | 1.0045        | 0.0045 |
| 7 terms         | 0.9998        | 0.0002 |
| 9 terms         | 1.0000        | 0.0000 |

So the more terms we use, the smaller the error gets —
that’s why it’s called a **truncation error** (because we cut the series short).

---

### Summary for Taylor Example

* We tried to calculate sin(90°) using a series.
* We used only a few parts of it, not the infinite ones.
* That caused a **small difference** from the true value → **Truncation Error**.
* More terms = **less error**

---

## Inherent Error (Input Error)

Now let’s talk about **real-life measurement mistakes**.

---

### What are we doing?

We want to find the **area of a square** using a **length** we measured.

But — our measuring instrument is not perfect.
So our **measured length** is a little off from the **true length**.

---

### Step-by-Step in Code

#### Step 1: Given values

```python
true_length = 10.12345
measured_length = 10.12
```

* True length = exact value (we imagine it’s perfect).
* Measured length = what we actually got with a ruler (rounded).

So the **difference = 0.00345 m**.

---

#### Step 2: Calculate areas

```python
true_area = true_length**2
measured_area = measured_length**2
```

* True area = ( 10.12345^2 = 102.484... )
* Measured area = ( 10.12^2 = 102.4144 )

Even though the length was off by just **0.00345**,
the area error is **much larger** because we squared it!

---

#### Step 3: Find the error

```python
inherent_error_in_area = abs(true_area - measured_area)
```

This gives the **difference between true area and measured area.**

That’s the **inherent (input) error** that got bigger during calculation.

---

#### Step 4: Show the results

```python
print(f"True Area: {true_area:.8f} m^2")
print(f"Measured Area: {measured_area:.8f} m^2")
print(f"Error in Area due to Inherent Error: {inherent_error_in_area:.8f}")
```

Output looks like:

```
True Area: 102.48458 m^2
Measured Area: 102.41440 m^2
Error in Area due to Inherent Error: 0.07018
```

---

###  Summary for Inherent Error

* Real-life measurements are **never perfect**.
* Even a tiny input mistake (like 0.003 m) can cause **big output mistakes** (like 0.07 m²).
* This is called **inherent error** or **input error** — it’s already there before calculation.

---

##  Final Summary (Both Together)

| Type of Error        | Where It Comes From               | Example                | How to Reduce It       |
| -------------------- | --------------------------------- | ---------------------- | ---------------------- |
| **Truncation Error** | From cutting a long series short  | sin(x) using few terms | Use more terms         |
| **Inherent Error**   | From inexact input or measurement | Measuring length       | Use better instruments |

---


