from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import math

app = FastAPI()


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


class Product(BaseModel):
    name: str
    image: str
    price: float


class Place(BaseModel):
    name: str
    address: str
    image: str
    latitude: float
    longitude: float
    products: List[Product]


places = [
    Place(
        name="Cafe Aroma",
        address="123 Street, Cairo",
        image="https://example.com/aroma.jpg",
        latitude=30.0444,
        longitude=31.2357,
        products=[
            Product(name="Cappuccino", image="https://example.com/cappuccino.jpg", price=50),
            Product(name="Croissant", image="https://example.com/croissant.jpg", price=30),
        ]
    ),
    Place(
        name="Pizza Corner",
        address="456 Street, Giza",
        image="https://example.com/pizza.jpg",
        latitude=30.0131,
        longitude=31.2089,
        products=[
            Product(name="Margherita", image="https://example.com/margherita.jpg", price=80),
            Product(name="Pepsi", image="https://example.com/pepsi.jpg", price=10),
        ]
    )
]

# http://127.0.0.1:8000/places?user_lat=30.05&user_lon=31.25
@app.get("/places")
def get_places(user_lat: float = Query(...), user_lon: float = Query(...)):
    response = []
    for place in places:
        distance = calculate_distance(user_lat, user_lon, place.latitude, place.longitude)
        place_data = place.dict()
        place_data["distance_km"] = round(distance, 2)
        response.append(place_data)
    return response


# http://127.0.0.1:8000/search_by_product?product_name=pepsi
@app.get("/search_by_product")
def search_by_product(product_name: str):
    result = []
    for place in places:
        matched_products = [p for p in place.products if product_name.lower() in p.name.lower()]
        if matched_products:
            place_data = place.dict()
            place_data["products"] = matched_products
            result.append(place_data)
    return result
