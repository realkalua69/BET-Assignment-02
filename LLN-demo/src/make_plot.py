"""Create boxplot showing LLN convergence."""
import argparse
import os
import glob
import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", required=True)
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    groups = defaultdict(list)
    for fp in glob.glob(os.path.join(args.data_dir, "*.csv")):
        with open(fp) as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                groups[int(row["draws"])].append(float(row["sample_mean"]))

    sorted_k = sorted(groups.keys())
    box_data = [groups[k] for k in sorted_k]
    labels = [f"k={k}" for k in sorted_k]

    expected = (args.n + 1) / 2

    fig, ax = plt.subplots(figsize=(11, 5.5))
    bp = ax.boxplot(box_data, tick_labels=labels, widths=0.45, patch_artist=True)

    for patch in bp["boxes"]:
        patch.set_facecolor("#d4e6f1")
        patch.set_edgecolor("#2c3e50")
    for median in bp["medians"]:
        median.set_color("#e74c3c")
        median.set_linewidth(1.5)

    ax.axhline(y=expected, color="#27ae60", ls=":", lw=1.5,
               label=f"Expected mean = {expected}")

    ax.set_title(f"Testing Draws for {args.n}", fontsize=14, fontweight="bold")
    ax.set_xlabel("Number of draws", fontsize=12)
    ax.set_ylabel("Sample mean", fontsize=12)
    ax.legend(fontsize=11)

    plt.tight_layout()
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    plt.savefig(args.output, dpi=200, bbox_inches="tight")
    print(f"saved {args.output}")

if __name__ == "__main__":
    main()
