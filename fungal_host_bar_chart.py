import pandas as pd
import matplotlib.pyplot as plt

# ---- Load TSV ----
file_path = "/scratch/boldajir/BB485/Fun_Path/fungal_host_counts.tsv"
df = pd.read_csv(file_path, sep="\t")

# Ensure "fungus" is treated as an identifier column
id_col = "fungus"
host_cols = [c for c in df.columns if c != id_col]

# ---- Convert to long format ----
long_df = df.melt(
    id_vars=id_col,
    value_vars=host_cols,
    var_name="host",
    value_name="count"
)

# Remove zero counts (so they don't appear in stacks)
long_df = long_df[long_df["count"] > 0]

# ---- Pivot for stacked bar chart ----
pivot_df = long_df.pivot_table(
    index=id_col,
    columns="host",
    values="count",
    aggfunc="sum",
    fill_value=0
)

# Optional: drop hosts that are all zero after filtering
pivot_df = pivot_df.loc[:, (pivot_df != 0).any(axis=0)]

# ---- Plot ----
ax = pivot_df.plot(
    kind="bar",
    stacked=True,
    figsize=(30, 30)
)

ax.set_xlabel("Fungus")
ax.set_ylabel("Host association count")
ax.set_title("Host associations per fungus (stacked)")
plt.legend(title="Host", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

plt.savefig("stacked_bar.pdf", format="pdf")

