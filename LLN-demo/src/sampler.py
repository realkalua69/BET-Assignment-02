"""Sample from [1, n] and compute running means."""
import argparse
import csv
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--draws", type=int, required=True)
    parser.add_argument("--trials", type=int, required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    with open(args.out, "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["draws", "trial", "sample_mean"])
        for t in range(1, args.trials + 1):
            vals = random.choices(range(1, args.n + 1), k=args.draws)
            avg = sum(vals) / args.draws
            writer.writerow([args.draws, t, round(avg, 4)])

if __name__ == "__main__":
    main()
