import pandas as pd

raw_df = pd.read_csv("fr.openfoodfacts.org.products.csv", error_bad_lines=False, low_memory=False) # raw dataset

print(raw_df.head())