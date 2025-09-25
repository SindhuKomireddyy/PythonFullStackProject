#dp_manager.py
import os
from supabase import create_client
from dotenv import load_dotenv

#load environment variables
load_dotenv()
url=os.getenv("https://lmrokoumgaepcjmxwxwp.supabase.co")
key=os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxtcm9rb3VtZ2FlcGNqbXh3eHdwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODI0MTAsImV4cCI6MjA3MzY1ODQxMH0.Ym5VurS4gNRqQEG9UzTRXwzvjOba6ZqzsWS3vs60CIM")

supabase=create_client(url,key)

# ======================================================
# REVIEWPRODUCTS TABLE CRUD
# ======================================================
def create_reviewproduct(source_product_id: str, name: str, metadata: dict = None):
    response = supabase.table("reviewproducts").insert({
        "source_product_id": source_product_id,
        "name": name,
        "metadata": metadata or {}
    }).execute()
    return response.data

def get_reviewproducts():
    response = supabase.table("reviewproducts").select("*").execute()
    return response.data

def update_reviewproduct(product_id: str, updates: dict):
    response = supabase.table("reviewproducts").update(updates).eq("id", product_id).execute()
    return response.data

def delete_reviewproduct(product_id: str):
    response = supabase.table("reviewproducts").delete().eq("id", product_id).execute()
    return response.data

# ======================================================
# REVIEWERS TABLE CRUD
# ======================================================
def create_reviewer(source_reviewer_id: str, name: str, profile_url: str = None):
    response = supabase.table("reviewers").insert({
        "source_reviewer_id": source_reviewer_id,
        "name": name,
        "profile_url": profile_url
    }).execute()
    return response.data

def get_reviewers():
    response = supabase.table("reviewers").select("*").execute()
    return response.data

def update_reviewer(reviewer_id: str, updates: dict):
    response = supabase.table("reviewers").update(updates).eq("id", reviewer_id).execute()
    return response.data

def delete_reviewer(reviewer_id: str):
    response = supabase.table("reviewers").delete().eq("id", reviewer_id).execute()
    return response.data


# ======================================================
# REVIEWS TABLE CRUD
# ======================================================
def create_review(product_id: str, reviewer_id: str, rating: int, text: str,
                  fake_prob: float = 0.0, trust_score: int = 50, is_flagged: bool = False):
    response = supabase.table("reviews").insert({
        "product_id": product_id,
        "reviewer_id": reviewer_id,
        "rating": rating,
        "text": text,
        "fake_prob": fake_prob,
        "trust_score": trust_score,
        "is_flagged": is_flagged
    }).execute()
    return response.data

def get_reviews():
    response = supabase.table("reviews").select(
        "id, rating, text, fake_prob, trust_score, is_flagged, "
        "reviewproducts(name), reviewers(name)"
    ).execute()
    return response.data

def update_review(review_id: str, updates: dict):
    response = supabase.table("reviews").update(updates).eq("id", review_id).execute()
    return response.data

def delete_review(review_id: str):
    response = supabase.table("reviews").delete().eq("id", review_id).execute()
    return response.data
