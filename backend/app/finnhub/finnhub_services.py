import finnhub
from app import config

finnhub_client = finnhub.Client(api_key=config.FINNHUB_API_KEY)


def get_company_profile(symbol: str) -> dict:
    return finnhub_client.company_profile2(symbol=symbol)
