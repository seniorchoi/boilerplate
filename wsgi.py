# wsgi.py (project root)
import os
from dotenv import load_dotenv

# 1️⃣ Load .env so Flask-CLI sees LICENSE_KEY, FLASK_ENV, DATABASE_URL, etc.
project_root = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(project_root, '.env'))

# 2️⃣ Import & create the app
from app import create_app, db, migrate  # note: import migrate too

app = create_app()

# 3️⃣ Re‑init migrate on the app & db so Flask-Migrate commands are registered
migrate.init_app(app, db)
