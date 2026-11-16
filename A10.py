import math

# Define two vectors
A = [1, 2, 3]
B = [2, 4, 6]

# Calculate dot product
dot_product = sum(a * b for a, b in zip(A, B))

# Calculate magnitude of vector A
magnitude_A = math.sqrt(sum(a * a for a in A))

# Calculate magnitude of vector B
magnitude_B = math.sqrt(sum(b * b for b in B))

# Calculate Cosine Similarity
cosine_similarity = dot_product / (magnitude_A * magnitude_B)

# Display the result
print("Vector A:", A)
print("Vector B:", B)
print("Cosine Similarity:", cosine_similarity)
