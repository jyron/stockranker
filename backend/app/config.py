import os

from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.environ["MONGODB_URI"]
MONGODB_DB = os.environ["MONGODB_DB"]
FINNHUB_API_KEY = os.environ["FINNHUB_API_KEY"]
FINNHUB_BASE_URL = os.environ["FINNHUB_BASE_URL"]
SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = os.environ["ALGORITHM"]
