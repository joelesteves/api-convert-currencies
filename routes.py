from asyncio import gather
from fastapi import APIRouter
from converter import sync_converter
router = APIRouter()

@router.get('/convert/{from_currency}')
async def convert(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(',')
    
    corotines = []
    
    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_currencies=currency,
            price=price
        )
        corotines.append(response)
                
    result = await gather(*corotines)
    return result