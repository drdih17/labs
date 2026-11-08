from connstans import DIH_SMALL_LIMIT, DIH_LARGE_LIMIT
from typing import Annotated

def get_mass(
    l: Annotated[float, "List length"], 
    w: Annotated[float, "List width"], 
    t: Annotated[float, "List thickness"], 
    q: Annotated[int, "Quantity"], 
    p: Annotated[float: "Material P"]
    ) -> float:
    '''
    Evaluate mass
    '''
    return l * w * (t / 1000) * p * q


def thickness_class(
    t: Annotated[float, "List thickness"]
    ) -> str:
    '''
    Evaluate thickness class
    '''
    if t < DIH_SMALL_LIMIT:
        return "Thin list"
    elif t > DIH_LARGE_LIMIT:
        return "Thick list"
    else:
        return "Normal list"