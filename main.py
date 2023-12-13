import pandas as pd
from pandas import json_normalize

input_file = "/Users/lucievandenbroucke/Library/CloudStorage/OneDrive-Epitech/DIGI1/Sneacker/SNEACKER/data.json"

output_file = "/Users/lucievandenbroucke/Library/CloudStorage/OneDrive-Epitech/DIGI1/Sneacker/SNEACKER/data.csv"

df = pd.read_json(input_file)

attributes_df = json_normalize(df['attributes'])

df = pd.concat([df[['id']], attributes_df], axis=1)

df.to_csv(output_file, sep="\t", index=False)
