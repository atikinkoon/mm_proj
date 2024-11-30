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

fig, ax1 = plt.subplots(figsize=(8, 6))

color = 'tab:blue'
ax1.set_xlabel('Height (m)')
ax1.set_ylabel('Angular Acceleration (α)', color=color)
ax1.plot(heights, angular_acceleration, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_title('Angular Acceleration and Time to Complete Rotation vs. Height')

ax2 = ax1.twinx()

color = 'tab:red'
ax2.set_ylabel('Time to Complete Rotation (t)', color=color)
ax2.plot(heights, time_to_rotate, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.grid(True)
plt.show()
