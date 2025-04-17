import os

class BaseConfig:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'change‑me')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Keys for gating access
    LICENSE_KEYS = os.getenv('LICENSE_KEYS', '').split(',')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class DevConfig(BaseConfig):
    DEBUG = True
    # Ensure 'instance' folder exists and use absolute file path for SQLite
    INSTANCE_PATH = os.path.join(os.getcwd(), 'instance')
    if not os.path.exists(INSTANCE_PATH):
        os.makedirs(INSTANCE_PATH, exist_ok=True)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(INSTANCE_PATH, 'database.db')

class ProdConfig(BaseConfig):
    DEBUG = False
    # Replace old-style Postgres URI prefix if present
    SQLALCHEMY_DATABASE_URI = (
        os.getenv('DATABASE_URL', '')
        .replace('postgres://', 'postgresql://', 1)
    )
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True