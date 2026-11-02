from database import db

products = [
    {
        "name": "Premium Wireless Headphones",
        "price": 85000,
        "category": "electronics",
        "image": "headphone.jpg"
    },
    {
        "name": "Classic Everyday Sneakers",
        "price": 65000,
        "category": "fashion",
        "image": "sneaker.jpg"
    },
    {
        "name": "Minimal Designer Watch",
        "price": 120000,
        "category": "fashion",
        "image": "watch.jpg"
    },
    {
        "name": "Modern Everyday Backpack",
        "price": 48000,
        "category": "fashion",
        "image": "bagpackjpg.jpg"
    },
    {
        "name": "portable playstation(ps-5)",
        "price": 200000,
        "category": "electronics",
        "image": "playstation (ps5).jpg"
    },
    {
        "name": "brand iphone",
        "price": 150000,
        "category": "electronics",
        "image": "iphone.jpg"
    },
    {
        "name": "brand iphone-17",
        "price": 180000,
        "category": "electronics",
        "image": "iphone17.jpg"
    },
    {
        "name": "motocycle",
        "price": 180000,
        "category": "electronics",
        "image": "motocycle.jpg"
    },
    {
        "name": "motocycle",
        "price": 180000,
        "category": "electronics",
        "image": "motocycle.jpg"
    },
    {
        "name": "Camera",
        "price": 10000,
        "category": "electronics",
        "image": "digital.jpg"
    },
    {
        "name": "lamp",
        "price": 10000,
        "category": "home and living",
        "image": "lamps.jpg"
    }
]


async def seed_products():
    await db.connect()

    try:
        for product in products:
            await db.product.create(data=product)

        print("Successfully inserted 11 products!")

    finally:
        await db.disconnect()


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_products())