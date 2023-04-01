import finnhub
from app import config

finnhub_client = finnhub.Client(api_key=config.FINNHUB_API_KEY)


def get_company_profile(symbol: str) -> dict:
    return finnhub_client.company_profile2(symbol=symbol)

# write  functinon to get sp500 list from finnhub


def get_sp500_list():
    return finnhub_client.indices_const(symbol="^GSPC")
