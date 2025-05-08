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
    category: str


class Place(BaseModel):
    name: str
    address: str
    image: str
    latitude: float
    longitude: float
    products: List[Product]


places = [
    Place(
        name="Koshary Sayed Hanafy",
        address="Hadayq elQubba, Cairo",
        image="https://i.postimg.cc/63dcdvbr/Whats-App-Image-2025-05-08-at-09-47-25-5bae8787.jpg",
        latitude=30.0775,
        longitude=31.2835,
        products=[
            Product(name="Small Koshary Box", image="https://i.postimg.cc/cC0mTLPV/Whats-App-Image-2025-05-08-at-09-47-54-aab87256.jpg", price=23.00,category="Koshary"),
            Product(name="Large Koshary Box", image="https://i.postimg.cc/KvcfM4PT/Whats-App-Image-2025-05-08-at-09-49-49-5aa0ec6b.jpg", price=28.00,category="Koshary"),
            Product(name="Star Koshary Plus", image="https://i.postimg.cc/KvcfM4PT/Whats-App-Image-2025-05-08-at-09-49-49-5aa0ec6b.jpg", price=38.00,category="Koshary"),
            Product(name="Meat Casserole", image="https://i.postimg.cc/vHPzLMhN/Whats-App-Image-2025-05-08-at-09-50-07-4c0dd3bc.jpg", price=50.00,category="Casserole"),
            Product(name="Chicken Casserole", image="https://i.postimg.cc/y8kTL5rY/Whats-App-Image-2025-05-08-at-09-51-12-e3a78676.jpg", price=55.00,category="Casserole"),
            Product(name="Rice Pudding", image="https://i.postimg.cc/T3FJF9Zj/Whats-App-Image-2025-05-08-at-09-51-44-a553deaa.jpg", price=22.00,category="Pudding"),
            Product(name="Lotus Rice Pudding", image="https://i.postimg.cc/vmntsnsJ/Whats-App-Image-2025-05-08-at-09-52-00-52aebb30.jpg", price=40.00,category="Pudding"),
            Product(name="Large Salad", image="https://i.postimg.cc/gjsK7PWr/Whats-App-Image-2025-05-08-at-09-48-19-d3e4a0aa.jpg", price=16.00,category="side"),
            Product(name="Crispy Toast", image="https://i.postimg.cc/DfP501XF/Whats-App-Image-2025-05-08-at-09-48-51-8b7b384b.jpg", price=10.00,category="side"),
        ]
    ),
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
