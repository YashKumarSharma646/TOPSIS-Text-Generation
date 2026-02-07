import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from src.topsis import normalize_matrix, apply_weights, calculate_ideal_solutions, calculate_scores
from src.utils import create_folders

# Create necessary folders
create_folders()

# Load decision matrix
df = pd.read_csv("data/decision_matrix.csv")

models = df["Model"]
criteria_data = df.drop(columns=["Model"])

matrix = criteria_data.values

# Define weights and impacts
weights = np.array([0.25, 0.25, 0.20, 0.15, 0.15])
impacts = ["-", "+", "+", "-", "-"]

# Step 1: Normalize
normalized = normalize_matrix(matrix)
normalized_df = pd.DataFrame(normalized, columns=criteria_data.columns, index=models)
normalized_df.to_csv("results/normalized_matrix.csv")

# Step 2: Apply weights
weighted = apply_weights(normalized, weights)
weighted_df = pd.DataFrame(weighted, columns=criteria_data.columns, index=models)
weighted_df.to_csv("results/weighted_matrix.csv")

# Step 3: Ideal best and worst
ideal_best, ideal_worst = calculate_ideal_solutions(weighted, impacts)

# Step 4: Calculate TOPSIS scores
scores = calculate_scores(weighted, ideal_best, ideal_worst)

df["TOPSIS Score"] = scores
df["Rank"] = df["TOPSIS Score"].rank(ascending=False)

df.to_csv("results/topsis_scores.csv", index=False)

# =============================
# Generate Plots
# =============================

# Ranking Bar Plot
plt.figure()
plt.bar(models, scores)
plt.title("TOPSIS Ranking of Text Generation Models")
plt.xlabel("Models")
plt.ylabel("TOPSIS Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/ranking_plot.png")
plt.close()

# Heatmap
plt.figure()
sns.heatmap(normalized_df, annot=True, cmap="viridis")
plt.title("Normalized Decision Matrix Heatmap")
plt.tight_layout()
plt.savefig("outputs/heatmap.png")
plt.close()

print("\nFinal Ranking:\n")
print(df.sort_values("TOPSIS Score", ascending=False))
