import numpy as np
import matplotlib.pyplot as plt

# Time parameters
time = np.linspace(0, 10, 1000)  # 10 seconds, 1000 data points

# Simulated gyroscope data
gyro_z = 30 * np.cos(2 * np.pi * 0.2 * time)  # Gyroscope data (Z-axis)

# Simulated Fiber Optic Gyroscope (FOG) data with additional noise
fog_z = gyro_z + np.random.normal(0, 1.0, size=time.shape)  # FOG data with noise

# Kalman filter implementation
def kalman_filter(measurements, process_variance, measurement_variance, initial_estimate=0):
    estimates = []  # List to store filtered estimates
    estimate = initial_estimate  # Initial state estimate
    error = 1.0  # Initial estimation error (P)

    for measurement in measurements:
        # Prediction step
        kalman_gain = error / (error + measurement_variance)  # Compute Kalman gain

        # Update step
        estimate = estimate + kalman_gain * (measurement - estimate)  # Update estimate
        estimates.append(estimate)  # Store the estimate

        # Update error covariance
        error = (1 - kalman_gain) * error + process_variance  # Update error for next iteration

    return estimates

# Apply Kalman filter to FOG data
filtered_fog = kalman_filter(fog_z, process_variance=0.01, measurement_variance=1.0)

# Apply Kalman filter to Gyroscope data
filtered_gyro = kalman_filter(gyro_z, process_variance=0.01, measurement_variance=0.5)

# Plot the filtered data
plt.figure(figsize=(12, 6))

# Plot raw FOG data
plt.plot(time, fog_z, label="Noisy FOG Data", color="red", linewidth=1.5)

# Plot filtered FOG data
plt.plot(time, filtered_fog, label="Filtered FOG Data", linestyle="--", color="green", linewidth=2)

# Plot raw Gyroscope data
plt.plot(time, gyro_z, label="Noisy Gyroscope Data", linestyle="--", color="blue")

# Plot filtered Gyroscope data
plt.plot(time, filtered_gyro, label="Filtered Gyroscope Data", color="orange", linewidth=2)

plt.title("Kalman Filter Applied to FOG and Gyroscope Data")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (deg/s)")
plt.legend()
plt.grid()
plt.show()
