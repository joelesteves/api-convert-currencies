from os import getenv
import requests
import aiohttp
from fastapi import HTTPException

ALPHAVANTAGE_APIKEY = getenv('ALPHAVANTAGE_APIKEY')

async def sync_converter(from_currency: str, to_currencies: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currencies}&apikey={ALPHAVANTAGE_APIKEY}'
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()
            
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    
    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail='Realtime Currency Exchange Rate not in data')
    
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate']) 
    
    return price * exchange_rate