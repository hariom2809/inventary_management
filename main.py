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

@app.get('/product/{id}')
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
        else:
            return "product not found"

@app.post("/products")
def get_data_from_user(product: Products):
    products. append(product)
    return product

@app.put("/products")
def update_products(id: int, product: Products):
    for i in range(len(products)):
        if products[i].id == id:
            products[i]= product
            return "updated successfull"
    return "failed"