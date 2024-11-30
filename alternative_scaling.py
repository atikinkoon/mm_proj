import numpy as np
import matplotlib.pyplot as plt
# Heights from 1.4 m to 2.0 m
heights = np.linspace(1.4, 2.0, 100)

# Alternative muscle strength scaling exponent
exponent = 1.8

# Recalculate torque and angular acceleration
torque_alt = heights ** exponent * heights  # τ ∝ L^{1.8} * L
angular_acceleration_alt = torque_alt / heights ** 5  # α ∝ τ / I

# Normalize for comparison
angular_acceleration_alt = angular_acceleration_alt / np.max(angular_acceleration_alt)

plt.figure(figsize=(8, 6))
plt.plot(heights, angular_acceleration_alt, label='Angular Acceleration (Alternative Scaling)', color='purple')
plt.xlabel('Height (m)')
plt.ylabel('Normalized Angular Acceleration')
plt.title('Angular Acceleration with Alternative Muscle Scaling vs. Height')
plt.legend()
plt.grid(True)
plt.show()
