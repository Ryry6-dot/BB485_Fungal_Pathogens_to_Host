#Import needed modules
import pandas as pd

#Read in the fungus_host_network.csv and store as a dataframe
fungus_host_table_repeats_path =  '/scratch/boldajir/BB485/Fun_Path/fungus_host_network_repeats.tsv'
df = pd.read_csv(fungus_host_table_repeats_path, sep="\t")
#Make a list of unique values in the fungi column
fungus_list = df['fungus'].unique()

#Make a list of the unique values in host column
host_list = df['host'].unique()
'''
host_genus_list = [name.split()[0] for name in host_list]
host_genus_list_U = list(set(host_genus_list))
print(host_genus_list_U)
'''
#Create a new dataframe with column headers set by unique host list
plot_df = pd.DataFrame(columns=host_list)
plot_df['fungus'] = fungus_list

#loop through all of the fungus and get counts
for index, row in plot_df.iterrows():

    temp_fungus = row["fungus"]

    subset_df = df[df["fungus"] == temp_fungus]

    # Do something with subset_df
    
    
    for temp_host in host_list:
        temp_count = list(subset_df['host']).count(temp_host) 
        plot_df.loc[index, temp_host] = temp_count

plot_df.to_csv(
    "fungal_host_counts.tsv",
    sep="\t",
    index=False)

print(plot_df)
