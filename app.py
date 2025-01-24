import os
import sys
import streamlit as st
import openai

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from scripts.recipe_matching_logic import find_matching_recipes, load_and_preprocess_data, calculate_similarity
from scripts.recipe_adaptation_logic import get_indian_recipe, validate_ingredients, indianize_recipe


def enhance_cooking_steps(steps):
    steps_text = " ".join(f"Step {i+1}: {step}" for i, step in enumerate(steps))
    prompt_text = f"Rewrite the following cooking instructions with complete, grammatically correct steps:\n{steps_text}"

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that rewrites cooking instructions into complete, grammatically correct steps."},
                {"role": "user", "content": prompt_text}
            ]
        )
        enhanced_steps = response.choices[0].message.content
        return enhanced_steps
    except Exception as e:
        return f"Error enhancing cooking steps: {str(e)}"


def main():
    tabs = ["Recipe Recommendation", "Indianization bot"]
    selected_tab = st.sidebar.selectbox("Select a tab", tabs)

    if selected_tab == "Recipe Recommendation":
        recipe_recommendation()
    elif selected_tab == "Indianization bot":
        indianization_bot()

def recipe_recommendation():
    st.title('Recipe Chatbot')

    csv_file_path = "data/Cleaned_raw_recipes_df.csv"
    recipes_df = load_and_preprocess_data(csv_file_path)

    # Streamlit user input for ingredients
    user_input = st.text_area('Enter your ingredients separated by commas:', '')

    if user_input:
        # Find recipes based on matching ingredients count
        matched_recipes = find_matching_recipes(user_input, recipes_df)
        recipe_names_match = matched_recipes['name'].tolist()
        
        # Find recipes based on TF-IDF cosine similarity
        similar_recipes = calculate_similarity(user_input, recipes_df)
        # Show only the top 5 recipes based on similarity
        top_similar_recipes = similar_recipes.head(5)
        recipe_names_similarity = top_similar_recipes['name'].tolist()

        # Display the top 5 TF-IDF cosine similarity scores and names before selection
        st.write("Top recipes based on similarity:")
        for index, row in top_similar_recipes.iterrows():
            st.write(f"{row['name']} - Similarity Score: {row['similarity']:.2f}")

        # Selection box for recipes from TF-IDF similarity
        recipe_selection = st.selectbox('Select a recipe to see the cooking steps:', [''] + recipe_names_similarity)
        
        # When a recipe is selected, display its cooking steps
        if recipe_selection:
            selected_recipe = recipes_df[recipes_df['name'] == recipe_selection].iloc[0]
            st.write('Ingredients:', ', '.join(selected_recipe['ingredients']))
            
            enhanced_steps = enhance_cooking_steps(selected_recipe['steps'])
            
            st.write('Cooking Steps:')
            st.write(enhanced_steps)

def indianization_bot():
    st.title("Indianization bot")
    recipe = {}

    ingredients = st.text_area('Enter your ingredients separated by commas:', '')
    if ingredients:
        recipe['ingredients'] = [x.strip() for x in ingredients.split(',')]

    if recipe.get('ingredients'):
        validated_ingredients = validate_ingredients(recipe['ingredients'])
        ingredients_str = ', '.join(validated_ingredients)
        recipe_text = f"Ingredients: {ingredients_str}"
        adapted_recipe = indianize_recipe(recipe_text)
        st.write(adapted_recipe)

if __name__ == "__main__":
    main()