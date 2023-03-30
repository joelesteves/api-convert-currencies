from fastapi import APIRouter
from converter import sync_converter
router = APIRouter()

@router.get('/convert/{from_currency}')
def convert(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(',')
    
    result = []
    
    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_currencies=currency,
            price=price
        )
        
        result.append(response)
        
    return result