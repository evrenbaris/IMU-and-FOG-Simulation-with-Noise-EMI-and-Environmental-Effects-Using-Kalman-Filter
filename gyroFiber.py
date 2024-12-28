import numpy as np
import matplotlib.pyplot as plt

# Time parameters
time = np.linspace(0, 10, 1000)  # 10 seconds, 1000 data points

# Simulated gyroscope data
gyro_z = 30 * np.cos(2 * np.pi * 0.2 * time)  # Gyroscope data (Z-axis)

# Simulated Fiber Optic Gyroscope (FOG) data with additional noise
fog_z = gyro_z + np.random.normal(0, 1.0, size=time.shape)  # FOG data with noise

# Plot gyroscope and FOG data
plt.figure(figsize=(12, 6))

# Plot gyroscope data (blue dashed line)
plt.plot(time, gyro_z, label="Gyroscope (Z-axis)", linestyle="--", color="blue", linewidth=2)

# Plot FOG data (red solid line)
plt.plot(time, fog_z, label="Fiber Optic Gyroscope (Z-axis)", color="red", linewidth=1.5)

# Graph labels and title
plt.title("Gyroscope vs Fiber Optic Gyroscope Data")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (deg/s)")
plt.legend()
plt.grid()

# Show the plot
plt.show()
