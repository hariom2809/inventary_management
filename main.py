from fastapi import FastAPI
from models import Products

app = FastAPI()

@app.get('/')
def greeting():
    return {'message': 'hello workd!'}

products= [
    Products(
        id=1,
        name= "phne",
        description= "Use for the far away communication",
        price= 25000,
        quantity= 5
    ),
    Products(
        id=2,
        name= "laptop",
        description= "use for the proessional work",
        price= 40000,
        quantity= 1
    ),
    Products(
        id=3,
        name= "tv",
        description= "Use for the entertainment purpose",
        price= 35000,
        quantity= 2
    ),
    Products(
        id=4,
        name= "desktop",
        description= "Use for heavy professional task whcih require more computational power",
        price= 450000,
        quantity= 1
    )
]

@app.get('/products')
def get_all_products():
    return products