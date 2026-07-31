from faker import Faker
import pandas as pd
import random

from config import (
    NUM_TV_SHOWS,
    TV_SHOWS_DIR,
    RANDOM_SEED
)

from utils import (
    save_dataframe,
    set_random_seed
)

fake = Faker()

set_random_seed(RANDOM_SEED)

GENRES = [
    "Drama", "Comedy", "Crime",
    "Sci-Fi", "Thriller", "Fantasy",
    "Documentary"
]

LANGUAGES = [
    "English", "Hindi", "Telugu",
    "Tamil", "Spanish", "French"
]

AGE_RATINGS = [
    "U", "U/A 13+", "U/A 16+", "A"
]


def generate_tv_shows():
    tv_shows = []

    for show_number in range(1, NUM_TV_SHOWS + 1):

        show = {
            "show_id": f"T{show_number:06d}",
            "title": fake.sentence(nb_words=3).replace(".", ""),
            "genre": random.choice(GENRES),
            "seasons": random.randint(1, 10),
            "episodes": random.randint(6, 120),
            "language": random.choice(LANGUAGES),
            "release_year": random.randint(1990, 2026),
            "imdb_rating": round(random.uniform(5.0, 9.8), 1),
            "age_rating": random.choice(AGE_RATINGS)
        }

        tv_shows.append(show)

    df = pd.DataFrame(tv_shows)
    

    save_dataframe(df, TV_SHOWS_DIR / "tv_shows.parquet")


if __name__ == "__main__":
    generate_tv_shows()