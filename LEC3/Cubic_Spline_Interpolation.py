import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Step 1: Make sure these are NumPy arrays
x_data = np.array([1, 3, 5, 8])
y_data = np.array([2, 3, 9, 10])

# Step 2: Create cubic spline interpolation
cs = CubicSpline(x_data, y_data)

# Step 3: Prepare smooth X values
x_smooth = np.linspace(x_data.min(), x_data.max(), 100)
y_smooth = cs(x_smooth)

# Step 4: Plot the curve and points
plt.plot(x_smooth, y_smooth, c="green", label="Cubic Spline Interpolation")
plt.plot(x_data, y_data, "ro", ms=5, label="Data Points")
plt.title("Cubic Spline Interpolation")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid()
plt.show()

# Step 5: Find interpolated value at X=4
x = 4
y = cs(x)
print(f"Interpolated Value at {x} is : {y:.4f}")

   

