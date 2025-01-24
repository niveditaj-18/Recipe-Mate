import pandas as pd

recipe_data_path = 'data/Cleaned_raw_recipes_df.csv'
recipes = pd.read_csv(recipe_data_path)

print(recipes.head())
print(recipes.info())