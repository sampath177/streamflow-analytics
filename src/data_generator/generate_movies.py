from faker import Faker
import pandas as pd
import random

from config import (
    NUM_MOVIES,
    MOVIES_DIR,
    RANDOM_SEED
)

from utils import (
    save_dataframe,
    set_random_seed
)

fake = Faker()

set_random_seed(RANDOM_SEED)

GENRES = [
    "Action", "Comedy", "Drama", "Thriller",
    "Romance", "Sci-Fi", "Horror", "Animation"
]

LANGUAGES = [
    "English", "Hindi", "Telugu",
    "Tamil", "Spanish", "French"
]

AGE_RATINGS = [
    "U", "U/A 13+", "U/A 16+", "A"
]


def generate_movies():
    movies = []

    for movie_number in range(1, NUM_MOVIES + 1):

        movie = {
            "movie_id": f"M{movie_number:06d}",
            "title": fake.sentence(nb_words=3).replace(".", ""),
            "genre": random.choice(GENRES),
            "release_year": random.randint(1980, 2026),
            "duration_minutes": random.randint(80, 180),
            "language": random.choice(LANGUAGES),
            "imdb_rating": round(random.uniform(5.0, 9.8), 1),
            "age_rating": random.choice(AGE_RATINGS)
        }

        movies.append(movie)

    df = pd.DataFrame(movies)

    save_dataframe(df, MOVIES_DIR / "movies.parquet")


if __name__ == "__main__":
    generate_movies()