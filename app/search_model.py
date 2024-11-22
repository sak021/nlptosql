import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
THRESHOLD_MATCHING=50

# Initialize the sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Function to match the query to the relevant column
def match_column_to_query(query, data):
    # Encode the query and column names using the sentence transformer model
    query_embedding = model.encode([query])
    corpus_embeddings = model.encode(data)

    # Compute cosine similarities between query and column names
    similarities = np.dot(query_embedding, corpus_embeddings.T)

    # Get indices of columns with similarity scores above the threshold
    matching_indices = np.where(similarities[0] > THRESHOLD_MATCHING)[0]

    # Retrieve all matches above the threshold
    matches = [data[i] for i in matching_indices if i < len(data)]

    return matches

if __name__ == "__main__":
    data = ["Johannesburg"]
    query = "Johanesbarg"
    match_column_to_query(query, data)
