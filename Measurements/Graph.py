#This code produces the bar graph for the measurements lab

import matplotlib.pyplot as plt

# Measurements and density values
measurements = [1, 2, 3, 4, 5]
densities = [0.995, 0.995, 0.994, 0.997, 0.993]

# Average, actual density, and uncertainty
average_density = 0.995
actual_density = 0.998
uncertainty = 0.02

# Create bar graph
plt.figure(figsize=(10, 6))

plt.bar(
    measurements,
    densities,
    width=0.65,
    yerr=uncertainty,
    capsize=5,
    label="Measured Density (±0.02 g/mL)"
)

# Add average and actual density lines
plt.axhline(
    average_density,
    linestyle="--",
    label="Average Density (0.995 g/mL)"
)

plt.axhline(
    actual_density,
    linestyle=":",
    label="Actual Water Density (0.998 g/mL)"
)

# Add title and axis labels
plt.title("The Density of Water (21°C) from a Volumetric Pipette")
plt.xlabel("Measurement")
plt.ylabel("Density (g/mL)")

# Set axis values
plt.xticks([1, 2, 3, 4, 5])
plt.ylim(0, 1.1)

# Label each bar
for x, density in zip(measurements, densities):
    plt.text(
        x,
        density + uncertainty + 0.005,
        f"{density:.3f}",
        ha="center",
        va="bottom"
    )

# Display legend
plt.legend()

# Display graph
plt.tight_layout()
plt.show()