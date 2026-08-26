import numpy as np
import pandas as pd
from scipy import stats

# ============================================================
# Curing Regime Statistical Analysis
# Published: Next Research, Elsevier (September 2025)
# Author: Muhammad Aamir
# ============================================================

# Compressive strength data (MPa) at 28 days
# Four curing regimes: Ambient, Water, Jute, SAP
data = {
    "Ambient" : [28.1, 27.4, 28.8, 27.9, 28.3],
    "Water"   : [31.2, 31.8, 30.9, 31.5, 31.1],
    "Jute"    : [29.5, 30.1, 29.8, 30.3, 29.7],
    "SAP"     : [27.8, 28.4, 27.5, 28.1, 27.9],
}

df = pd.DataFrame(data)

def cohens_d(group1, group2):
    """Calculate Cohen's d effect size between two groups."""
    mean_diff = np.mean(group2) - np.mean(group1)
    pooled_std = np.sqrt(
        (np.std(group1, ddof=1)**2 + np.std(group2, ddof=1)**2) / 2
    )
    return mean_diff / pooled_std


def run_analysis(df):
    print("=" * 50)
    print("   CONCRETE CURING — STATISTICAL ANALYSIS")
    print("=" * 50)

    # Descriptive stats
    print("\n📊 Descriptive Statistics (28-day strength, MPa):\n")
    print(df.describe().round(3))

    # One-way ANOVA
    f_stat, p_value = stats.f_oneway(*[df[col] for col in df.columns])
    print(f"\n📐 One-Way ANOVA:")
    print(f"   F-statistic : {f_stat:.4f}")
    print(f"   p-value     : {p_value:.6f}")
    if p_value < 0.05:
        print("   ✅ Significant difference between curing regimes (p < 0.05)")
    else:
        print("   ❌ No significant difference detected")

    # Cohen's d vs Ambient (control)
    print(f"\n📏 Cohen's d Effect Size (vs Ambient control):")
    for regime in ["Water", "Jute", "SAP"]:
        d = cohens_d(df["Ambient"], df[regime])
        pct = ((np.mean(df[regime]) - np.mean(df["Ambient"])) 
               / np.mean(df["Ambient"])) * 100
        print(f"   {regime:8s}: d = {d:.3f} | "
              f"Strength change: {pct:+.1f}%")

    print("=" * 50)


if __name__ == "__main__":
    run_analysis(df)
