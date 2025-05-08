from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import math

app = FastAPI()


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = (
        math.sin(d_lat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(d_lon / 2) ** 2
    )
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
    category: str
    latitude: float
    longitude: float
    products: List[Product]


places = [
    Place(
        name="Koshary Sayed Hanafy",
        address="Hadayq elQubba, Cairo",
        image="https://i.postimg.cc/63dcdvbr/Whats-App-Image-2025-05-08-at-09-47-25-5bae8787.jpg",
        category="Koshary, Pasta, Desserts",
        latitude=30.0775,
        longitude=31.2835,
        products=[
            Product(
                name="Small Koshary Box",
                image="https://i.postimg.cc/cC0mTLPV/Whats-App-Image-2025-05-08-at-09-47-54-aab87256.jpg",
                price=23.00,
                category="Koshary",
            ),
            Product(
                name="Large Koshary Box",
                image="https://i.postimg.cc/KvcfM4PT/Whats-App-Image-2025-05-08-at-09-49-49-5aa0ec6b.jpg",
                price=28.00,
                category="Koshary",
            ),
            Product(
                name="Star Koshary Plus",
                image="https://i.postimg.cc/KvcfM4PT/Whats-App-Image-2025-05-08-at-09-49-49-5aa0ec6b.jpg",
                price=38.00,
                category="Koshary",
            ),
            Product(
                name="Meat Casserole",
                image="https://i.postimg.cc/vHPzLMhN/Whats-App-Image-2025-05-08-at-09-50-07-4c0dd3bc.jpg",
                price=50.00,
                category="Pasta",
            ),
            Product(
                name="Chicken Casserole",
                image="https://i.postimg.cc/y8kTL5rY/Whats-App-Image-2025-05-08-at-09-51-12-e3a78676.jpg",
                price=55.00,
                category="Pasta",
            ),
            Product(
                name="Rice Pudding",
                image="https://i.postimg.cc/T3FJF9Zj/Whats-App-Image-2025-05-08-at-09-51-44-a553deaa.jpg",
                price=22.00,
                category="Dessert",
            ),
            Product(
                name="Lotus Rice Pudding",
                image="https://i.postimg.cc/vmntsnsJ/Whats-App-Image-2025-05-08-at-09-52-00-52aebb30.jpg",
                price=40.00,
                category="Dessert",
            ),
            Product(
                name="Large Salad",
                image="https://i.postimg.cc/gjsK7PWr/Whats-App-Image-2025-05-08-at-09-48-19-d3e4a0aa.jpg",
                price=16.00,
                category="side",
            ),
            Product(
                name="Crispy Toast",
                image="https://i.postimg.cc/DfP501XF/Whats-App-Image-2025-05-08-at-09-48-51-8b7b384b.jpg",
                price=10.00,
                category="side",
            ),
        ],
    ),
    Place(
        name="AlMa3alem Abu Mazen AlSory",
        address="Hadayq elQubba, Cairo",
        image="https://i.postimg.cc/tJNrHxhq/Whats-App-Image-2025-05-08-at-09-53-50-d99a2a37.jpg",
        category="Shawarma, Chicken",
        latitude=30.0785,
        longitude=31.2845,
        products=[
            Product(
                name="Pomme frites potates sandwich",
                image="https://i.postimg.cc/NFncmSz2/Whats-App-Image-2025-05-08-at-09-43-40-a7e6b519.jpg",
                price=39.00,
                category="Potatoes",
            ),
            Product(
                name="Large Chicken Shawarma sandwich",
                image="https://i.postimg.cc/qRdXM7Bz/Whats-App-Image-2025-05-08-at-09-54-34-9b44414c.jpg",
                price=94.00,
                category="Shawarma",
            ),
            Product(
                name="Super Large Chicken Shawarma Sandwich",
                image="https://i.postimg.cc/Kzr7Ky4Q/Whats-App-Image-2025-05-08-at-09-54-51-e0df48af.jpg",
                price=105.00,
                category="Shawarma",
            ),
            Product(
                name="Shawarma Mix Chicken On Meat sandwich",
                image="https://i.postimg.cc/zvxnjSCg/Whats-App-Image-2025-05-08-at-09-57-12-0129bd37.jpg",
                price=105.00,
                category="Shawarma",
            ),
            Product(
                name="Meat Shawarma Sandwich",
                image="https://i.postimg.cc/4x7z6cmY/Whats-App-Image-2025-05-08-at-09-57-43-32536dc0.jpg",
                price=116.00,
                category="Shawarma",
            ),
            Product(
                name="Super Syrian Meat Shawarma sandwich",
                image="https://i.postimg.cc/XqjfdDCW/Whats-App-Image-2025-05-08-at-09-56-11-a8283be6.jpg",
                price=127.00,
                category="Shawarma",
            ),
            Product(
                name="Hawawshi Abu Mazen",
                image="https://i.postimg.cc/MpC1dGQd/Whats-App-Image-2025-05-08-at-09-58-09-d1888704.jpg",
                price=88.00,
                category="Hawawshi",
            ),
            Product(
                name="2 Fried Chicken Meal",
                image="https://i.postimg.cc/C1TThbfk/Whats-App-Image-2025-05-08-at-10-04-58-6ee007c8.jpg",
                price=116.00,
                category="Fried Chicken",
            ),
            Product(
                name="4 Fried Chicken Meal",
                image="https://i.postimg.cc/nz48CMv5/Whats-App-Image-2025-05-08-at-10-05-42-e9a8fa4a.jpg",
                price=231.00,
                category="Fried Chicken",
            ),
            Product(
                name="6 Fried Chicken Meal",
                image="https://i.postimg.cc/Zn4G3ZHq/Whats-App-Image-2025-05-08-at-10-06-19-a574d893.jpg",
                price=330.00,
                category="Fried Chicken",
            ),
        ],
    ),
    Place(
        name="Hamzawy",
        address="Hadayq elQubba, Cairo",
        image="https://i.postimg.cc/kGskvZYv/Whats-App-Image-2025-05-08-at-10-07-35-a95538fa.jpg",
        category="Burgers, Fried Chicken, Fast Food",
        latitude=30.0775,
        longitude=31.2835,
        products=[
            Product(
                name="Hamzawi Beef",
                image="https://i.postimg.cc/CM4T0BMn/Whats-App-Image-2025-05-08-at-10-08-45-0a2ffb1a.jpg",
                price=105.00,
                category="Burger",
            ),
            Product(
                name="Mushroom Land Beef",
                image="https://i.postimg.cc/gkk92zrS/Whats-App-Image-2025-05-08-at-10-08-59-12af841b.jpg",
                price=120.00,
                category="Burger",
            ),
            Product(
                name="Original Beef",
                image="https://i.postimg.cc/132bBDB2/Whats-App-Image-2025-05-08-at-10-09-47-30390a8e.jpg",
                price=150.00,
                category="Burger",
            ),
            Product(
                name="Cheese Bomb Beef",
                image="https://i.postimg.cc/43cqSnFd/Whats-App-Image-2025-05-08-at-10-10-21-da7d2e7d.jpg",
                price=155.00,
                category="Burger",
            ),
            Product(
                name="Chicken bacon",
                image="https://i.postimg.cc/02tT6Tw8/Whats-App-Image-2025-05-08-at-10-09-16-4c9c25b3.jpg",
                price=120.00,
                category="Fried Chicken",
            ),
            Product(
                name="Turkey Chicken",
                image="https://i.postimg.cc/G21VwrZj/Whats-App-Image-2025-05-08-at-10-10-41-7f0e64ed.jpg",
                price=130.00,
                category="Fried Chicken",
            ),
            Product(
                name="Cheese Boom Fried Chicken",
                image="https://i.postimg.cc/Pxzcd9Hn/Whats-App-Image-2025-05-08-at-10-10-59-98d26d42.jpg",
                price=150.00,
                category="Fried Chicken",
            ),
             Product(
                name="Potatoes Packet",
                image="https://i.postimg.cc/6pyDCMrC/Whats-App-Image-2025-05-08-at-10-09-31-ce21084c.jpg",
                price=35.00,
                category="Potatoes",
            ),
            Product(
                name="Spicy Sauce",
                image="https://i.postimg.cc/bw7FkpNj/Whats-App-Image-2025-05-08-at-10-11-22-66a5ac6f.jpg",
                price=10.00,
                category="Sauce",
            ),
            Product(
                name="Ranch Sauce",
                image="https://i.postimg.cc/fyzPyCWt/Whats-App-Image-2025-05-08-at-10-11-38-02023d88.jpg",
                price=15.00,
                category="Sauce",
            ),
            Product(
                name="Tastey Sauce",
                image="https://i.postimg.cc/tJBMx67r/Whats-App-Image-2025-05-08-at-10-11-48-2d67831a.jpg",
                price=15.00,
                category="Sauce",
            ),
        ],
    ),
]


# http://127.0.0.1:8000/places?user_lat=30.05&user_lon=31.25
@app.get("/places")
def get_places(user_lat: float = Query(...), user_lon: float = Query(...)):
    response = []
    for place in places:
        distance = calculate_distance(
            user_lat, user_lon, place.latitude, place.longitude
        )
        place_data = place.dict()
        place_data["distance_km"] = round(distance, 2)
        response.append(place_data)
    return response


# http://127.0.0.1:8000/search_by_product?product_name=pepsi
@app.get("/search_by_product")
def search_by_product(product_name: str):
    result = []
    for place in places:
        matched_products = [
            p for p in place.products if product_name.lower() in p.name.lower()
        ]
        if matched_products:
            place_data = place.dict()
            place_data["products"] = matched_products
            result.append(place_data)
    return result


# http://127.0.0.1:8000/search_by_category?category=Koshary
@app.get("/search_by_category")
def search_by_category(category: str):
    result = []
    for place in places:
        matched_products = [
            p for p in place.products if category.lower() == p.category.lower()
        ]
        if matched_products:
            place_data = place.dict()
            place_data["products"] = matched_products
            result.append(place_data)
    return result
