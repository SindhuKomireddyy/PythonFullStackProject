# src/logic.py

import src.db as db  # Make sure db_manager.py is in the same folder

class ProductManager:
    """CRUD operations for products"""

    def add(self, source_product_id: str, name: str, metadata: dict = None):
        if not name or not source_product_id:
            return {"success": False, "message": "name and source_product_id required"}
        result = db.create_reviewproduct(source_product_id, name, metadata)
        return {"success": True, "message": "Product added", "data": result}

    def get_all(self):
        return db.get_reviewproducts()

    def update(self, product_id: str, updates: dict):
        result = db.update_reviewproduct(product_id, updates)
        return {"success": True, "message": "Product updated", "data": result}

    def delete(self, product_id: str):
        result = db.delete_reviewproduct(product_id)
        return {"success": True, "message": "Product deleted", "data": result}


class ReviewerManager:
    """CRUD operations for reviewers"""

    def add(self, source_reviewer_id: str, name: str, profile_url: str = None):
        result = db.create_reviewer(source_reviewer_id, name, profile_url)
        return {"success": True, "message": "Reviewer added", "data": result}

    def get_all(self):
        return db.get_reviewers()

    def update(self, reviewer_id: str, updates: dict):
        result = db.update_reviewer(reviewer_id, updates)
        return {"success": True, "message": "Reviewer updated", "data": result}

    def delete(self, reviewer_id: str):
        result = db.delete_reviewer(reviewer_id)
        return {"success": True, "message": "Reviewer deleted", "data": result}


class ReviewManager:
    """CRUD operations for reviews"""

    def add(self, product_id: str, reviewer_id: str, rating: int, text: str,
            fake_prob: float = 0.0, trust_score: int = 50, is_flagged: bool = False):
        result = db.create_review(product_id, reviewer_id, rating, text,
                                  fake_prob, trust_score, is_flagged)
        return {"success": True, "message": "Review added", "data": result}

    def get_all(self):
        return db.get_reviews()

    def update(self, review_id: str, updates: dict):
        result = db.update_review(review_id, updates)
        return {"success": True, "message": "Review updated", "data": result}

    def delete(self, review_id: str):
        result = db.delete_review(review_id)
        return {"success": True, "message": "Review deleted", "data": result}


class TaskManager:
    """Aggregate manager to access all three managers"""

    def __init__(self):
        self.products = ProductManager()
        self.reviewers = ReviewerManager()
        self.reviews = ReviewManager()


# ================= TEST =================
if __name__ == "__main__":
    tm = TaskManager()

    print("📦 Products:", tm.products.get_all())
    print("👤 Reviewers:", tm.reviewers.get_all())
    print("⭐ Reviews:", tm.reviews.get_all())
