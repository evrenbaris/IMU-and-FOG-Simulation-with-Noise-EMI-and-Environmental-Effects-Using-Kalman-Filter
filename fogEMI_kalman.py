# Apply Kalman filter to FOG data with EMI and environmental effects
filtered_fog_with_environment = kalman_filter(fog_with_environment, process_variance=0.01, measurement_variance=1.0)

# Plot filtered data
plt.figure(figsize=(12, 6))

# Raw FOG data with noise
plt.plot(time, fog_with_environment, label="Noisy FOG Data (With EMI and Environmental Effects)", color="red")

# Filtered FOG data
plt.plot(time, filtered_fog_with_environment, label="Filtered FOG Data", linestyle="--", color="green")

plt.title("Filtered FOG Data After EMI and Environmental Effects")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (deg/s)")
plt.legend()
plt.grid()
plt.show()
