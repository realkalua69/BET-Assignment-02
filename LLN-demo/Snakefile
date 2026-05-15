configfile: "params.yaml"

RANGE_MAX = config["range_max"]
DRAWS = config["draw_sizes"]
TRIALS = config["num_trials"]

rule all:
    input:
        "output/convergence.png"

rule sample:
    output:
        "output/data/draws_{d}.csv"
    params:
        n = RANGE_MAX,
        trials = TRIALS
    shell:
        "python3 src/sampler.py --n {params.n} --draws {wildcards.d} --trials {params.trials} --out {output}"

rule visualize:
    input:
        expand("output/data/draws_{d}.csv", d=DRAWS)
    output:
        "output/convergence.png"
    params:
        n = RANGE_MAX
    shell:
        "python3 src/make_plot.py --data-dir output/data --n {params.n} --output {output}"
