from faker import Faker
import pandas as pd
import random

from config import (
    NUM_USERS,
    NUM_MOVIES,
    NUM_TV_SHOWS,
    NUM_RATINGS,
    RATINGS_DIR,
    RANDOM_SEED
)

from utils import (
    save_dataframe,
    set_random_seed
)

fake = Faker()
set_random_seed(RANDOM_SEED)


def generate_ratings():

    ratings = []

    for rating_id in range(1, NUM_RATINGS + 1):

        content_type = random.choice(["Movie", "TV Show"])

        if content_type == "Movie":
            content_id = f"M{random.randint(1, NUM_MOVIES):06d}"
        else:
            content_id = f"T{random.randint(1, NUM_TV_SHOWS):06d}"

        ratings.append({
            "rating_id": rating_id,
            "user_id": f"U{random.randint(1, NUM_USERS):06d}",
            "content_type": content_type,
            "content_id": content_id,
            "rating": random.randint(1, 5),
            "rating_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            )
        })

    df = pd.DataFrame(ratings)

    save_dataframe(
        df,
        RATINGS_DIR / "ratings.parquet"
    )


if __name__ == "__main__":
    generate_ratings()