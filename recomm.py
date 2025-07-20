# Tiny movie dataset
movies = [
    {
        'title': 'The Matrix',
        'description': 'computer hacker reality war sci-fi action'
    },
    {
        'title': 'The Terminator',
        'description': 'cyborg assassin time travel sci-fi action'
    },
    {
        'title': 'Inception',
        'description': 'dream thief corporate secrets sci-fi thriller'
    },
    {
        'title': 'Interstellar',
        'description': 'space wormhole humanity survival sci-fi adventure'
    },
    {
        'title': 'The Dark Knight',
        'description': 'batman joker crime action drama'
    },
    {
        'title': 'Pulp Fiction',
        'description': 'mob hitmen crime drama bandits'
    }
]

# Simple tokenizer
def tokenize(text):
    return text.lower().split()

# Simple similarity: count matching words
def compute_similarity(desc1, desc2):
    words1 = set(tokenize(desc1))
    words2 = set(tokenize(desc2))
    common = words1.intersection(words2)
    return len(common)

# Recommendation function
def recommend(title):
    # Find movie description
    target_movie = None
    for movie in movies:
        if movie['title'].lower() == title.lower():
            target_movie = movie
            break
    if not target_movie:
        print("Movie not found.")
        return

    similarities = []
    for movie in movies:
        if movie['title'] == target_movie['title']:
            continue
        score = compute_similarity(target_movie['description'], movie['description'])
        similarities.append((movie['title'], score))

    # Sort by similarity score
    similarities.sort(key=lambda x: x[1], reverse=True)

    print(f"Because you watched '{title}', you may like:")
    for movie, score in similarities[:3]:
        print(f"- {movie} (similarity: {score})")

# Example
recommend('Inception')
