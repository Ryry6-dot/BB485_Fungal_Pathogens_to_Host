#Import needed modules
import pandas as pd


# Create a string object that is a full path to a tsv file
Pathogen_Host_File_Path = "/scratch/boldajir/BB485/Fun_Path/Path-Host.tsv"

#make Path-Host df
df2 = pd.read_csv(Pathogen_Host_File_Path, sep="\t")

# Create a string object that is a full path to a tsv file
North_Star_File_Path = "/scratch/boldajir/BB485/Fun_Path/North_Star.tsv"

# Read the tsv file in as a dataframe
df1 = pd.read_csv(
    North_Star_File_Path,
    delimiter="\t",
    header=1)

df1["True_Species_name"] = df1["Species_name"].apply(lambda x: ' '.join(x.split()[:2]))

###############################################
results = []

for fungus in df1["True_Species_name"].unique():

    matches = df2[df2["fungus"] == fungus]

    for host in matches["hostFamily"]:

        results.append([fungus, host])

network_df = pd.DataFrame(
    results,
    columns=["fungus", "host"]
)

print(network_df.head())
#########################################
network_df.to_csv(
    "fungus_host_network_repeats.tsv",
    sep="\t",
    index=False)
##############################################
'''
import networkx as nx
import matplotlib.pyplot as plt

G = nx.from_pandas_edgelist(
    network_df,
    source="fungus",
    target="host"
)

plt.figure(figsize=(12,12))
nx.draw(
    G,
    node_size=20,
    with_labels=False
)

plt.show()

network_df.to_csv(
    "fungus_host_network_repeats.csv",
    index=False)
'''
