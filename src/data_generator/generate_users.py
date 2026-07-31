from faker import Faker
import pandas as pd
import random

from config import (
    NUM_USERS,
    USERS_DIR,
    RANDOM_SEED
)


from utils import (
    save_dataframe,
    set_random_seed
)

fake = Faker()

set_random_seed(RANDOM_SEED)


def generate_users():
    users = []
    COUNTRY_CITY_MAP = {
    "India": [
        "Hyderabad",
        "Bengaluru",
        "Chennai",
        "Mumbai",
        "Delhi"
    ],
    "USA": [
        "New York",
        "Seattle",
        "Chicago",
        "San Francisco"
    ],
    "UK": [
        "London",
        "Manchester",
        "Liverpool"
    ]
}

    for user_number in range(1, NUM_USERS + 1):

        country = random.choice(list(COUNTRY_CITY_MAP.keys()))
        city = random.choice(COUNTRY_CITY_MAP[country])

        user = {
            "user_id": f"U{user_number:06d}",
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "gender": random.choice(["Male", "Female"]),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=75),
            "country": country,
            "city": city,
            "signup_date": fake.date_between(start_date="-5y", end_date="today"),
            "subscription_id": random.choice(["S001", "S002", "S003"]),
            "status": random.choice(["Active", "Inactive"])
        }
        users.append(user)

    df = pd.DataFrame(users)

    save_dataframe(df, USERS_DIR / "users.parquet")
    print(len(users))

if __name__ == "__main__":
    generate_users()