import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_CONNECTION_STRING = os.environ["MONGODB_CONNECTION_STRING"]
