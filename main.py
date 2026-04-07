from src.stat_engine import StatEngine  ## importing the module inorder to access the function that is definied inside the module.

data = [10, 12, 12, 13, 14, 100]
engine = StatEngine(data)

print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Variance (sample):", engine.get_variance(is_sample=True))
print("Standard Deviation (sample):", engine.get_standard_deviation(is_sample=True))
print("Outliers:", engine.get_outliers(threshold=2))

# Part 2: Monte Carlo Simulation
print("\n=== Part 2: Monte Carlo Simulation ===")
from src.monte_carlo import simulate_crashes  # importing the module inorder to access the function that is definied inside the module.
days_list = [30, 100, 1000, 10000]
for days in days_list:
    crash_prob=simulate_crashes(days)
    print(f"Estimated crash probability over {days} days: {crash_prob:.4f}")    