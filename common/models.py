from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price_required: int
    url: str
