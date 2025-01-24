import pandas as pd
from ast import literal_eval

def preprocess_data(csv_file_path):
    recipes = pd.read_csv(csv_file_path)

    # Convert ingredient strings to lists
    recipes['ingredients'] = recipes['ingredients'].apply(literal_eval)

    # Save the preprocessed DataFrame
    preprocessed_file_path = csv_file_path.replace('.csv', '_preprocessed.csv')
    recipes.to_csv(preprocessed_file_path, index=False)

    print(f"Preprocessed data saved to {preprocessed_file_path}")

    return preprocessed_file_path

if __name__ == '__main__':
    
    recipe_data_path = "data/Cleaned_raw_recipes_df.csv"
    preprocess_data(recipe_data_path)