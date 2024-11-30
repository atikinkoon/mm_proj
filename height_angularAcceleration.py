import numpy as np
import matplotlib.pyplot as plt

# Heights from 1.4 m to 2.0 m
heights = np.linspace(1.4, 2.0, 100)

# Constants (arbitrary units for proportionality)
k_alpha = 1  # Proportionality constant for angular acceleration

# Angular acceleration scaling
angular_acceleration = k_alpha * heights ** -2

plt.figure(figsize=(8, 6))
plt.plot(heights, angular_acceleration, label='Angular Acceleration (α)', color='blue')
plt.xlabel('Height (m)')
plt.ylabel('Angular Acceleration (relative units)')
plt.title('Angular Acceleration vs. Height')
plt.legend()
plt.grid(True)
plt.show()
