"""
Configuration settings for StreamFlow Analytics dataset generation.
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data" / "raw"

USERS_DIR = DATA_DIR / "users"
MOVIES_DIR = DATA_DIR / "movies"
TV_SHOWS_DIR = DATA_DIR / "tv_shows"
SUBSCRIPTIONS_DIR = DATA_DIR / "subscriptions"
RATINGS_DIR = DATA_DIR / "ratings"
VIEWING_HISTORY_DIR = DATA_DIR / "viewing_history"

NUM_USERS = 10_000
NUM_MOVIES = 2_000
NUM_TV_SHOWS = 500
NUM_RATINGS = 100_000
NUM_VIEWING_EVENTS = 500_000

OUTPUT_FORMAT = "parquet"

RANDOM_SEED = 42