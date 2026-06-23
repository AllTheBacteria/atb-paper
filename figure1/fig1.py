import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

scale = 2

mpl.rcParams["font.size"] = 10 * scale
mpl.rcParams["axes.titlesize"] = 12 * scale
mpl.rcParams["axes.labelsize"] = 10 * scale
mpl.rcParams["xtick.labelsize"] = 10 * scale
mpl.rcParams["ytick.labelsize"] = 10 * scale
mpl.rcParams["legend.fontsize"] = 10 * scale
mpl.rcParams["figure.titlesize"] = 12 * scale

surveillance_counts = pd.read_csv("surveillance_counts.csv", index_col="Species")

human_pathogen_pc = pd.read_csv("human_pathogen_pc.csv", index_col="human_pathogen")
experimental_pc = pd.read_csv("experimental_pc.csv", index_col="Experimental",  dtype={"Experimental": str})
surveillance_pc = pd.read_csv("surveillance_pc.csv", index_col="Surveillance",  dtype={"Surveillance": str})

# panel a

plt.rcParams["svg.fonttype"] = "none"
surveillance_counts['total'] = surveillance_counts.sum(axis=1)
surveillance_counts_sorted = surveillance_counts.sort_values('total', ascending=False).drop(columns='total')


#surveillance_counts_661k['total'] = surveillance_counts_661k.sum(axis=1)
#surveillance_counts_661k_sorted = surveillance_counts_661k.sort_values('total', ascending=False).drop(columns='total')

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
plt.savefig("./atb_species.svg", bbox_inches="tight")

# panel b

# Parameters for plotting
plt.figure(figsize=(10, 6))

# Plot single stacked bar
plt.bar(0, human_pathogen_pc.loc[False], color='#1a9850', label='Non-pathogen')
plt.bar(0, human_pathogen_pc.loc[True], bottom=human_pathogen_pc.loc[False], color='#d73027', label='Human Pathogen')

plt.bar(1, surveillance_pc.loc[np.nan], color='grey', label='Unknown')
plt.bar(1, surveillance_pc.loc["False"], bottom=surveillance_pc.loc[np.nan], color='skyblue', label='Research')
plt.bar(1, surveillance_pc.loc["True"], bottom=(surveillance_pc.loc[np.nan] + surveillance_pc.loc["False"]), color='orange', label='Surveillance')

plt.bar(2, experimental_pc.loc[np.nan], color='grey', label='Unknown')
plt.bar(2, experimental_pc.loc["False"], bottom=experimental_pc.loc[np.nan], color='#984ea3', label='Non-experimental')
plt.bar(2, experimental_pc.loc["True"], bottom=(experimental_pc.loc[np.nan] + experimental_pc.loc["False"]), color='#ffff33', label='Lab Experiment')

plt.ylabel('Percentage')
plt.xticks([0,1,2], ['Human Pathogen', 'Sequencing Aim', 'Isolate type'])

plt.xlabel("AllTheBacteria Sequenced Isolates")

plt.ylim(0, 1)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y*100)}%'))

# Remove only top and right spines
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Unique legend on the right
handles, labels = ax.get_legend_handles_labels()
unique = dict(zip(labels, handles))
plt.legend(unique.values(), unique.keys(),
           bbox_to_anchor=(1.02, 1), loc='upper left')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("./overall_composition.svg", bbox_inches="tight")
