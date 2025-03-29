import pandas as pd
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

# Load the data
file_path = "Persian_Dishes_Ingredients.xlsx"  # Ensure the correct file path
df = pd.read_excel(file_path)

# Transpose the dataframe to have dishes as rows and ingredients as columns
df_dishes = df.set_index("Ingredient").T

# Compute the hierarchical clustering
linkage_matrix = sch.linkage(df_dishes, method='ward')

# Plot the dendrogram
plt.figure(figsize=(12, 6))
sch.dendrogram(linkage_matrix, labels=df_dishes.index, leaf_rotation=90, leaf_font_size=10)
plt.title("Evolutionary Tree of Persian Dishes Based on Ingredient Similarity")
plt.ylabel("Distance")
plt.show()
