import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline

scale = 2

mpl.rcParams["font.size"] = 10 * scale
mpl.rcParams["axes.titlesize"] = 12 * scale
mpl.rcParams["axes.labelsize"] = 10 * scale
mpl.rcParams["xtick.labelsize"] = 10 * scale
mpl.rcParams["ytick.labelsize"] = 10 * scale
mpl.rcParams["legend.fontsize"] = 10 * scale
mpl.rcParams["figure.titlesize"] = 12 * scale

surveillance_counts = pd.read_csv(surveillance_counts.csv, index_col="Species")

human_pathogen_pc = pd.read_csv(human_pathogen_pc.csv, index_col="human_pathogen")
experimental_pc = pd.read_csv(experimental_pc.csv, index_col="Experimental")
surveillance_pc = pd.read_csv(surveillance_pc.csv, index_col="Surveillance")

# panel a

plt.rcParams["svg.fonttype"] = "none"
surveillance_counts['total'] = surveillance_counts.sum(axis=1)
surveillance_counts_sorted = surveillance_counts.sort_values('total', ascending=False).drop(columns='total')


surveillance_counts_661k['total'] = surveillance_counts_661k.sum(axis=1)
surveillance_counts_661k_sorted = surveillance_counts_661k.sort_values('total', ascending=False).drop(columns='total')

# Parameters for plotting
bar_width = 0.35
x = np.arange(len(surveillance_counts))  # the x locations for the original bars
plt.figure(figsize=(10, 6))


# Plot first stacked bar
bottom1 = np.zeros(len(surveillance_counts_sorted))
for col in surveillance_counts_sorted.columns:
    plt.bar(x, surveillance_counts_sorted[col], bottom=bottom1, width=bar_width*2, label=f'AllTheBacteria {col}')
    bottom1 += surveillance_counts_sorted[col]
# Labels and formatting

plt.xticks(x, surveillance_counts_sorted.index, rotation=45, ha='right', fontstyle="italic")
plt.ylabel('Sequenced Isolates')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.legend()

# panel b

plt.rcParams["svg.fonttype"] = "none"
surveillance_counts['total'] = surveillance_counts.sum(axis=1)
surveillance_counts_sorted = surveillance_counts.sort_values('total', ascending=False).drop(columns='total')


surveillance_counts_661k['total'] = surveillance_counts_661k.sum(axis=1)
surveillance_counts_661k_sorted = surveillance_counts_661k.sort_values('total', ascending=False).drop(columns='total')

# Parameters for plotting
bar_width = 0.35
x = np.arange(len(surveillance_counts))  # the x locations for the original bars
plt.figure(figsize=(10, 6))


# Plot first stacked bar
bottom1 = np.zeros(len(surveillance_counts_sorted))
for col in surveillance_counts_sorted.columns:
    plt.bar(x, surveillance_counts_sorted[col], bottom=bottom1, width=bar_width*2, label=f'AllTheBacteria {col}')
    bottom1 += surveillance_counts_sorted[col]
# Labels and formatting

plt.xticks(x, surveillance_counts_sorted.index, rotation=45, ha='right', fontstyle="italic")
plt.ylabel('Sequenced Isolates')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.legend()
