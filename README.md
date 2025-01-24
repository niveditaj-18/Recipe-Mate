# Recipe Mate

## Problem Statement
1. Users often have ingredients on hand but lack recipe ideas that utilize those ingredients.
2. Existing recipes may not cater to specific regional preferences (e.g., Indian cuisine).
3. Cooking instructions in recipes may lack clarity and grammatical correctness.

## Solution
Recipe Mate is a comprehensive solution that addresses these challenges by providing:

1. **Ingredient-based Recipe Recommendation System**: This system suggests recipes based on the ingredients provided by the user, ensuring that they can utilize the ingredients they already have.

2. **Recipe Enhancement and Indianization**: Recipe Mate utilizes OpenAI's GPT-3.5-turbo language model to enhance the cooking instructions, making them more complete and grammatically correct. Additionally, it can adapt recipes to an Indian style, catering to regional preferences.

## Examples

### Recipe Recommendation
Input:
tomatoes, crackers, mayonnaise, black pepper
Output:
Top recipes based on TF-IDF cosine similarity:

munch without guilt tomatoes - Similarity Score: 1.00 grilled cheese crackers - Similarity Score: 0.65 cracker eggs - Similarity Score: 0.59 old fashioned so georgia cracker salad extremely easy - Similarity Score: 0.59 b l t dip bacon lettuce and tomato bit - Similarity Score: 0.58

Selected Recipe: munch without guilt tomatoes Ingredients: tomatoes, crackers, mayonnaise, black pepper

Cooking Steps:

1. Place a slice of tomato on each biscuit or cracker.
2. Spread a small amount of mayonnaise on top of the tomato and sprinkle with black pepper.
3. Enjoy your snack guilt-free!

### Recipe Indianization
Input:
marinara sauce, pizza base, cheese, salt
Output:
Ingredients: a) Original ingredients: marinara sauce, pizza base, cheese, salt b) Additional Ingredients for Indian recipe: • Garam masala • Cumin • Onions

Steps:

1. Preheat the oven according to the instructions on the pizza base packaging.
2. In a bowl, mix the marinara sauce with a pinch of salt, a tablespoon of garam masala, and a teaspoon of cumin.
3. Spread the sauce mixture onto the pizza base.
4. Top with grated cheese and sliced onions.
5. Bake the pizza in the preheated oven until the cheese is melted and bubbly.
6. Serve hot and enjoy your Indian-style pizza!

## Setup and Running the System

### Prerequisites
- Python 3.7 or later
- Required Python packages: pandas, scikit-learn, openai, streamlit

### Installation
1. Clone the repository or download the source code.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Obtain an OpenAI API key from https://openai.com/ and create a `config.py` file in the project directory with the following content:
   ```python
   OPENAI_API_KEY = "your_openai_api_key"
   ```
4. Download the "Food.com Recipes and Interactions" dataset from Kaggle ([https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions]([https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?select=RAW_recipes.csv))) if the dataset provided in the zip file does not work and rename the downloaded dataset as `Cleaned_raw_recipes_df.csv` and place it in the `data` directory
5. If you are able to access the dataset from the zip file, place the `Cleaned_raw_recipes_df.csv` file in the `data` directory.

### Running the Application
If you are downloading the data from Kaggle:
1. Run the preprocess_data.py and continue with the other steps below

If you are able to access the data directly in the data directory:
1. Navigate to the project directory.
2. Run the Streamlit application by executing `streamlit run app.py`.
3. The application will open in your default web browser, where you can interact with the Recipe Recommendation and Indianization Bot features.

### Dataset

The project utilizes the "Food.com Recipes and Interactions" dataset from Kaggle ([https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions]([https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?select=RAW_recipes.csv))). The dataset is preprocessed and cleaned to extract the ingredients and cooking steps for each recipe.
