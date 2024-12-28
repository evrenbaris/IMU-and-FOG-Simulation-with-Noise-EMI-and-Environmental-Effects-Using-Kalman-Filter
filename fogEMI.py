# Add dynamic EMI noise
emi_noise = np.random.normal(0, 0.5, size=time.shape)  # EMI with standard deviation 0.5
fog_with_emi = fog_z + emi_noise

# Add temperature-based noise to simulate environmental effects
temperature_effect = 0.2 * np.sin(2 * np.pi * 0.1 * time)  # Sine wave to simulate temperature variation
fog_with_environment = fog_with_emi + temperature_effect

# Plot FOG data with EMI and environmental effects
plt.figure(figsize=(12, 6))

# Raw FOG data
plt.plot(time, fog_z, label="Original FOG Data", linestyle="--", color="blue")

# FOG data with EMI
plt.plot(time, fog_with_emi, label="FOG with EMI", color="red")

# FOG data with EMI and environmental effects
plt.plot(time, fog_with_environment, label="FOG with EMI and Environmental Effects", color="green")

plt.title("FOG Data with EMI and Environmental Effects")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (deg/s)")
plt.legend()
plt.grid()
plt.show()
