import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval

def load_and_preprocess_data(csv_file_path):
    # Load the dataset
    recipes = pd.read_csv(csv_file_path)

    # Convert ingredients and steps from string representation of list to actual lists
    recipes['ingredients'] = recipes['ingredients'].apply(literal_eval)
    recipes['steps'] = recipes['steps'].apply(literal_eval)

    return recipes

def find_matching_recipes(user_ingredients, recipes, top_n=3):
    # Prepare user ingredients list for matching
    user_ingredients_set = set(ingredient.strip().lower() for ingredient in user_ingredients.split(','))

    # Score each recipe by the number of matching ingredients
    recipes['match_count'] = recipes['ingredients'].apply(lambda ing_list: len(user_ingredients_set.intersection(set(ing_list))))

    # Sort by match_count and return top_n recipes
    return recipes.nlargest(top_n, 'match_count')[['name', 'match_count', 'steps']]

# New function to preprocess the ingredients into a string for TF-IDF
def preprocess_ingredients(ingredients_list):
    return ' '.join(ingredients_list).lower()

# New function to calculate the similarity between the user's ingredients and each recipe
def calculate_similarity(user_ingredients, recipes_df):
    # Preprocess the ingredients from the dataframe for TF-IDF
    recipes_df['processed_ingredients'] = recipes_df['ingredients'].apply(preprocess_ingredients)
    
    # Create the TF-IDF Vectorizer and transform the ingredients data
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(recipes_df['processed_ingredients'])
    
    # Preprocess the user's ingredients and transform to TF-IDF
    user_ingredients = preprocess_ingredients(user_ingredients.split(','))
    user_tfidf_vector = vectorizer.transform([user_ingredients])
    
    # Calculate the cosine similarity
    cosine_similarities = cosine_similarity(user_tfidf_vector, tfidf_matrix).flatten()
    
    # Add the similarity scores to the dataframe
    recipes_df['similarity'] = cosine_similarities
    
    # Return the recipes sorted by similarity, including the steps
    return recipes_df.sort_values(by='similarity', ascending=False)[['name', 'similarity', 'steps']]

if __name__ == '__main__':
    # Replace with the path to your actual data file
    csv_file_path = 'data/Cleaned_raw_recipes_df_preprocessed.csv'
    recipes_df = load_and_preprocess_data(csv_file_path)
    
    # Test the matching function
    test_ingredients = 'milk, butter, flour'
    print(find_matching_recipes(test_ingredients, recipes_df))

    print("Recipes based on TF-IDF cosine similarity:")
    similar_recipes = calculate_similarity(test_ingredients, recipes_df)
    print(similar_recipes[['name', 'similarity', 'steps']].head())