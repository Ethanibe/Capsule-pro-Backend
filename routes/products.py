from fastapi import APIRouter, HTTPException
from database import db
from schemas import ProductCreate, ProductUpdate
router = APIRouter()


@router.get("/")
async def get_products(
    search: str | None = None,
    category: str | None = None
):
    products = await db.product.find_many()

    if search:
        products = [
            product for product in products
            if search.lower() in product.name.lower()
        ]

    if category:
        products = [
            product for product in products
            if category.lower() in product.category.lower()
        ]

    return {
        "count": len(products),
        "data": products
    }


@router.get("/{product_id}")
async def get_product(product_id: int):
    product = await db.product.find_unique(
        where={"id": product_id}
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {"data": product}

@router.post("/")
async def create_product(product: ProductCreate):
    new_product = await db.product.create(
        data=product.model_dump()
    )

    return {
        "message": "Product created successfully",
        "data": new_product
    }

@router.put("/{product_id}")
async def update_product(product_id: int, product: ProductUpdate):
    existing_product = await db.product.find_unique(
        where={"id": product_id}
    )

    if not existing_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    updated_product = await db.product.update(
        where={"id": product_id},
        data=product.model_dump(exclude_unset=True)
    )

    return {
        "message": "Product updated successfully",
        "data": updated_product
    }

@router.delete("/{product_id}")
async def delete_product(product_id: int):
    existing_product = await db.product.find_unique(
        where={"id": product_id}
    )

    if not existing_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    await db.product.delete(
        where={"id": product_id}
    )

    return {
        "message": "Product deleted successfully"
    }