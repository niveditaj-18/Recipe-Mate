# Recipe-Mate
A cutting-edge recipe recommendation system, Recipe Mate, uses natural language processing (NLP) techniques to suggest personalized recipes based on user-provided ingredients and preferences. The project includes TF-IDF vectorization for recipe matching, GPT-3.5-turbo for Indianized adaptations, and Streamlit for a seamless user interface.

## Overview
Recipe Mate is a personalized recipe recommendation system leveraging natural language processing (NLP) to simplify home cooking. Users can input available ingredients, dietary preferences, and cuisine types to receive tailored recipe suggestions. The system adapts recipes for cultural preferences and provides a user-friendly interface for seamless interaction.

## Features
1. **Ingredient-Based Recipe Matching**:
   - Uses TF-IDF vectorization and cosine similarity to match recipes to user-provided ingredients.
2. **Indianization Bot**:
   - Enhances non-Indian recipes by tailoring them to Indian culinary preferences using GPT-3.5-turbo.
3. **Interactive User Interface**:
   - Built with Streamlit for easy navigation and responsive interaction.
4. **Insights from EDA**:
   - Word clouds, unigram and bigram analysis, sentiment analysis, and time-series trends.

## Dataset
- **Source**: [Food.com Recipes and Interactions](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?select=RAW_recipes.csv)
- **Description**:
  - Contains 231,637 recipes with attributes such as ingredients, steps, tags, and user interactions.
  - Columns: Recipe ID, Ingredients, Steps, Tags, Nutrition, etc.

## Methodology
1. **Data Cleaning**:
   - Processed raw datasets to handle null values and remove inconsistencies.
   - Extracted relevant columns for recipe matching.
2. **Exploratory Data Analysis (EDA)**:
   - Analyzed ingredient usage, recipe sentiments, and submission trends.
   - Visualized findings with word clouds, line graphs, and bar charts.
3. **Recipe Matching**:
   - TF-IDF and cosine similarity used for ingredient-based matching.
4. **AI Integration**:
   - GPT-3.5-turbo for adapting recipes to Indian preferences.
5. **Interface**:
   - Developed a user-friendly UI using Streamlit.

## Results
1. **Top Ingredients**:
   - Salt, butter, and sugar were the most frequently used ingredients.
2. **Sentiment Analysis**:
   - Most recipes had overwhelmingly positive sentiments.
3. **Indianization Bot**:
   - Successfully adapted American recipes to Indian flavors using GPT-3.5-turbo.
4. **Recipe Matching**:
   - Achieved accurate recommendations using TF-IDF with over 90% matching accuracy.

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**: pandas, numpy, scikit-learn, Streamlit, OpenAI GPT-3.5-turbo
- **Data Source**: Kaggle (Food.com dataset)

