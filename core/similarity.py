from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

poets = ["Fuzuli", "Nazim Hikmet", "Yunus Emre", "Şehriyar"]

def find_similar(vector):

    # fake embedding demo
    db = np.random.rand(4, 384)

    scores = cosine_similarity([vector], db)[0]

    return sorted(
        zip(poets, scores),
        key=lambda x: x[1],
        reverse=True
    )
