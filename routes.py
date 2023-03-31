from asyncio import gather
from fastapi import APIRouter, Path, Query
from converter import async_converter
from schamas import ConverterInput, ConverterOutput
router = APIRouter()

@router.get('/convert/{from_currency}')
async def convert(
    from_currency: str = Path(max_length=50, regex='^[A-Z]{3}$'),
    to_currencies: str = Query(max_length=50, regex='^[A-Z]{3}(,[A-Z]{3})*$'),
    price: float = Query(gt=0)
):
    to_currencies = to_currencies.split(',')
    
    corotines = []
    
    for currency in to_currencies:
        response = async_converter(
            from_currency=from_currency,
            to_currencies=currency,
            price=price
        )
        corotines.append(response)
                
    result = await gather(*corotines)
    return result

@router.get('/async/v2/{from_currency}',response_model=ConverterOutput)
async def converter(
    body: ConverterInput,
    from_currency: str = Path(max_length=50, regex='^[A-Z]{3}$'),
):    
    corotines = []
    
    to_currencies = body.to_currencies
    price = body.price

    for currency in to_currencies:
        response = async_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        corotines.append(response)

    result = await gather(*corotines)
    
    return ConverterOutput(
        response_message='Successfully converted',
        converted_prices=result
    )