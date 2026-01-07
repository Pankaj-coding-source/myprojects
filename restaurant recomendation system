import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Drop rows with missing 'Cuisines'
df=pd.read_csv('Dataset .csv')
df_cleaned = df.dropna(subset=['Cuisines']).reset_index(drop=True)

# Step 2: Apply OneHotEncoder to 'Cuisines'
encoder = OneHotEncoder(sparse_output=False)
cuisine_encoded = encoder.fit_transform(df_cleaned[['Cuisines']])
cuisine_df = pd.DataFrame(cuisine_encoded, columns=encoder.get_feature_names_out(['Cuisines']))

# Step 3: Concatenate encoded features with original DataFrame
df_encoded = pd.concat([df_cleaned, cuisine_df], axis=1)

# Step 4: Get user input
user_cuisine = input("Enter your preferred cuisine (e.g., Indian, Chinese, Italian): ").strip()

# Step 5: Create user preference vector
user_preferences = {col: 0 for col in cuisine_df.columns}
cuisine_column = f'Cuisines_{user_cuisine}'

if cuisine_column in user_preferences:
    user_preferences[cuisine_column] = 1
else:
    print(f"Sorry, '{user_cuisine}' is not available in our dataset.")
    exit()

user_vector = np.array([user_preferences[col] for col in cuisine_df.columns])

# Step 6: Compute similarity
similarity_scores = cosine_similarity([user_vector], cuisine_df.values)[0]
df_encoded['Similarity'] = similarity_scores

# Step 7: Show top recommendations
top_recommendations = df_encoded.sort_values(by='Similarity', ascending=False).head(5)
print("\nTop Restaurant Recommendations for You:")
print(top_recommendations[['Restaurant Name', 'Cuisines', 'Similarity']])
