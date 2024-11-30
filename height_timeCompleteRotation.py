import numpy as np
import matplotlib.pyplot as plt

# Heights from 1.4 m to 2.0 m
heights = np.linspace(1.4, 2.0, 100)

# Constants (arbitrary units for proportionality)
k_alpha = 1  # Proportionality constant for angular acceleration

# Angular acceleration scaling
angular_acceleration = k_alpha * heights ** -2

# Assuming θ (angular displacement) is constant
theta = np.pi  # 180 degrees in radians

# Time to complete rotation
time_to_rotate = np.sqrt((2 * theta) / angular_acceleration)

plt.figure(figsize=(8, 6))
plt.plot(heights, time_to_rotate, label='Time to Complete Rotation (t)', color='red')
plt.xlabel('Height (m)')
plt.ylabel('Time (relative units)')
plt.title('Time to Complete Rotation vs. Height')
plt.legend()
plt.grid(True)
plt.show()
