import pandas as pd

from config import SUBSCRIPTIONS_DIR
from utils import save_dataframe

def generate_subscriptions():

    subscriptions = [
        {
            "subscription_id": "S001",
            "plan_name": "Basic",
            "price": 199,
            "video_quality": "HD",
            "screens": 1
        },
        {
            "subscription_id": "S002",
            "plan_name": "Standard",
            "price": 499,
            "video_quality": "Full HD",
            "screens": 2
        },
        {
            "subscription_id": "S003",
            "plan_name": "Premium",
            "price": 649,
            "video_quality": "4K",
            "screens": 4
        }
    ]

    df = pd.DataFrame(subscriptions)

    save_dataframe(df, SUBSCRIPTIONS_DIR / "subscriptions.parquet")


if __name__ == "__main__":
    generate_subscriptions()