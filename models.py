from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str
    quantity: int

    model_config = {
        "from_attributes": True
    }
