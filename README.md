# ReviewRadar
Description:
ReviewRadar is an AI-powered Fake Review Detection System that helps users identify suspicious or potentially fake product reviews. It analyzes review content, reviewer credibility, and posting patterns to provide a fake probability for each review and a trust score for each reviewer.

## Key features:

-**Fake Review Detection**: Predicts the likelihood of a review being fake using AI/ML.

-**Reviewer Trust Score**: Evaluates reviewer credibility based on history and review patterns.

-**Timeline Analysis**: Detects sudden review spikes to flag suspicious campaigns.

-**Review Clustering**: Groups similar or copy-paste reviews to uncover spam.

-**Dashboard Visualization**: Interactive UI to view products, reviews, and suspicious activity.

## Project Structure
ReviewRadar/
|
|---src/            #core application logic
|   |---logic.py    #Businesss logic and task operations
|   |__db.py        #database operations
|
|---api/            #backend api
|   |__main.py      #FASTAPI endpoints
|
|---frontend/       #Frontend application
|   |__app.py       #Streamlit web interface
|
|___requirements.txt    #Python dependencies
|
|___README.md       #Project documentation
|
|___.env            #Python VariableS

## Quick Start

### Prerequistes
-Python 3.8 or higher
-A Supabase account
-Git(push,cloning)

### 1.Clone or Download the project
# Option 1:Clone with Git
git clone <repository-url>

# Option 2:Download and extract the ZIP file

### 2. Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

### 3.Set Up Supabase Database
1.Create a Supabase Project:
2.Create the Products Table:

-go to the SQL Editor in your Supabase dashboard
-run this SQL command:
    
```sql
create table if not exists products (
    id serial primary key,                 -- auto-increment product ID
    source_product_id text not null,      -- product ID from API or website
    name text                              -- product name
);

create table if not exists reviewers (
    id serial primary key,                 -- auto-increment reviewer ID
    source_reviewer_id text,               -- reviewer ID from source
    name text,                             -- reviewer display name
    profile_url text                        -- reviewer profile link (optional)
);
create table if not exists reviews (
    id serial primary key,                 -- auto-increment review ID
    product_id int references products(id) on delete cascade,   -- link to product
    reviewer_id int references reviewers(id) on delete set null, -- link to reviewer
    
    rating smallint check (rating between 1 and 5),  -- 1–5 stars
    text text,                                      -- raw review text
    clean_text text,                                -- preprocessed text (optional)
    review_created_at timestamptz,                  -- review timestamp
    
    fake_prob real default 0.0,                     -- probability of being fake
    trust_score smallint default 50 check (trust_score between 0 and 100), -- reviewer credibility
    is_flagged boolean default false               -- suspicious review flag
);
```

3. **Get Your credentials:
### 4.configure Environment Variables

1. Create a `.env` file in the project root
2. Add your supabase credentials to `.env`:
SUPABASE_URL="https://lmrokoumgaepcjmxwxwp.supabase.co"
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxtcm9rb3VtZ2FlcGNqbXh3eHdwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODI0MTAsImV4cCI6MjA3MzY1ODQxMH0.Ym5VurS4gNRqQEG9UzTRXwzvjOba6ZqzsWS3vs60CIM


### 5.Run the Application

## Streamlit Frontend
Streamlit run frontend/app.py
The app will open in your browser at `http://localhost:8501`

## FASTAPI Backend

cd api
python main.py
The API will be available at `http://localhost:8000`

## How to use
## Technologies Used
-**Frontend**:Streamlit(python web framework)
-**Backend**: FASTAPI (python rest api framework) 
-**Database**:Supabase (PostgresSQL-based backend-as-a-service)
-**Language**:python 3.8++

### Key Components

1. **`src/db.py`**:Database operations
    -handles all CRUD operations with supabase
2. **`src/logic.py`**:Business logic
    -Task validation and preprocessing

## troubleshooting

## Common Issues

1. **"Module not found" errors**
    -make sure you've installed all dependencies:`pip install -r requirements.txt`
    -check that you are running commands from the current directory

## Future enhancements
Ideas for extending this project:


## Support
if you encounter any issues or hqave questions:
mail id:sindhukomireddy@gmail.com
mobile no:7672049446




