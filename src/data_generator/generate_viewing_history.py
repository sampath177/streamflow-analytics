from faker import Faker
import pandas as pd
import random

from config import (
    NUM_USERS,
    NUM_MOVIES,
    NUM_TV_SHOWS,
    NUM_VIEWING_EVENTS,
    VIEWING_HISTORY_DIR,
    RANDOM_SEED
)

from utils import (
    save_dataframe,
    set_random_seed
)

fake = Faker()
set_random_seed(RANDOM_SEED)


def generate_viewing_history():

    viewing_history = []

    for event_id in range(1, NUM_VIEWING_EVENTS + 1):

        content_type = random.choice(["Movie", "TV Show"])

        if content_type == "Movie":
            content_id = f"M{random.randint(1, NUM_MOVIES):06d}"
        else:
            content_id = f"T{random.randint(1, NUM_TV_SHOWS):06d}"

        viewing_history.append({
            "event_id": event_id,
            "user_id": f"U{random.randint(1, NUM_USERS):06d}",
            "content_type": content_type,
            "content_id": content_id,
            "watch_date": fake.date_between(start_date="-2y", end_date="today"),
            "watch_duration_minutes": random.randint(5, 180),
            "device": random.choice([
                "Mobile",
                "TV",
                "Laptop",
                "Tablet"
            ])
        })

    df = pd.DataFrame(viewing_history)

    save_dataframe(
        df,
        VIEWING_HISTORY_DIR / "viewing_history.parquet"
    )


if __name__ == "__main__":
    generate_viewing_history()