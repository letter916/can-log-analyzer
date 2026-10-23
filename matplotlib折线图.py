plt.figure(figsize=(8, 5))
plt.plot(
    days,
    hours,
    marker="o",
    linewidth=2,
    color="#DD8452",
    label="Study Hours"
)

plt.title("Study Hours per Day")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()

plt.savefig("plot.png", dpi=150, bbox_inches="tight")
plt.show()