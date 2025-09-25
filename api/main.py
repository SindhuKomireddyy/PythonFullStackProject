# api/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Add src folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))
from logic import TaskManager  # Import TaskManager

# ----------------- App Setup -----------------
app = FastAPI(title="ReviewRadar API", version="1.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# TaskManager instance
task_manager = TaskManager()

# ======================= Pydantic Models =======================
class ProductCreate(BaseModel):
    source_product_id: str
    name: str
    metadata: dict = None

class ProductUpdate(BaseModel):
    name: str = None
    metadata: dict = None

class ReviewerCreate(BaseModel):
    source_reviewer_id: str
    name: str
    profile_url: str = None

class ReviewerUpdate(BaseModel):
    name: str = None
    profile_url: str = None

class ReviewCreate(BaseModel):
    product_id: str
    reviewer_id: str
    rating: int
    text: str
    fake_prob: float = 0.0
    trust_score: int = 50
    is_flagged: bool = False

class ReviewUpdate(BaseModel):
    rating: int = None
    text: str = None
    fake_prob: float = None
    trust_score: int = None
    is_flagged: bool = None

# ======================= Endpoints =======================

@app.get("/")
def home():
    return {"success": True, "message": "ReviewRadar API is running", "data": None}

# ----------------- Products -----------------
@app.get("/products")
def get_products():
    try:
        products = task_manager.products.get_all()
        return {"success": True, "message": "Products fetched successfully", "data": products}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch products: {e}")

@app.post("/products")
def create_product(product: ProductCreate):
    try:
        result = task_manager.products.add(
            source_product_id=product.source_product_id,
            name=product.name,
            metadata=product.metadata
        )
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create product: {e}")

@app.put("/products/{product_id}")
def update_product(product_id: str, updates: ProductUpdate):
    try:
        result = task_manager.products.update(product_id, updates.dict(exclude_none=True))
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update product: {e}")

@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    try:
        result = task_manager.products.delete(product_id)
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete product: {e}")

# ----------------- Reviewers -----------------
@app.get("/reviewers")
def get_reviewers():
    try:
        reviewers = task_manager.reviewers.get_all()
        return {"success": True, "message": "Reviewers fetched successfully", "data": reviewers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch reviewers: {e}")

@app.post("/reviewers")
def create_reviewer(reviewer: ReviewerCreate):
    try:
        result = task_manager.reviewers.add(
            source_reviewer_id=reviewer.source_reviewer_id,
            name=reviewer.name,
            profile_url=reviewer.profile_url
        )
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create reviewer: {e}")

@app.put("/reviewers/{reviewer_id}")
def update_reviewer(reviewer_id: str, updates: ReviewerUpdate):
    try:
        result = task_manager.reviewers.update(reviewer_id, updates.dict(exclude_none=True))
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update reviewer: {e}")

@app.delete("/reviewers/{reviewer_id}")
def delete_reviewer(reviewer_id: str):
    try:
        result = task_manager.reviewers.delete(reviewer_id)
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete reviewer: {e}")

# ----------------- Reviews -----------------
@app.get("/reviews")
def get_reviews():
    try:
        reviews = task_manager.reviews.get_all()
        return {"success": True, "message": "Reviews fetched successfully", "data": reviews}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch reviews: {e}")

@app.post("/reviews")
def create_review(review: ReviewCreate):
    try:
        result = task_manager.reviews.add(
            product_id=review.product_id,
            reviewer_id=review.reviewer_id,
            rating=review.rating,
            text=review.text,
            fake_prob=review.fake_prob,
            trust_score=review.trust_score,
            is_flagged=review.is_flagged
        )
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create review: {e}")

@app.put("/reviews/{review_id}")
def update_review(review_id: str, updates: ReviewUpdate):
    try:
        result = task_manager.reviews.update(review_id, updates.dict(exclude_none=True))
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update review: {e}")

@app.delete("/reviews/{review_id}")
def delete_review(review_id: str):
    try:
        result = task_manager.reviews.delete(review_id)
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete review: {e}")

#----run----
if __name__ == "__main__":
    import uvicorn
uvicorn.run("main.app",host="0.0.0.0",port=8000,reload=True)