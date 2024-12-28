vibration_effect = 0.3 * np.sin(2 * np.pi * 5 * time)  # High-frequency vibration
fog_with_vibration = fog_with_environment + vibration_effect

plt.figure(figsize=(12, 8))

# Original FOG data
plt.plot(time, fog_z, label="Original FOG Data", linestyle="--", color="blue")

# FOG with EMI
plt.plot(time, fog_with_emi, label="FOG with EMI", color="red")

# FOG with environmental effects
plt.plot(time, fog_with_environment, label="FOG with EMI + Environmental Effects", color="green")

# FOG with vibration
plt.plot(time, fog_with_vibration, label="FOG with EMI + Environmental + Vibration", color="orange")

# Filtered data
plt.plot(time, filtered_fog_with_environment, label="Filtered FOG Data", linestyle="--", color="purple")

plt.title("Comparison of FOG Data Under Different Conditions")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (deg/s)")
plt.legend()
plt.grid()
plt.show()
