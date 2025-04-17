import os
# Determine project root to locate templates and static folders
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask
import stripe
from openai import OpenAI

from .models import db, migrate, login_manager
from .main.routes import main_bp
from .auth.routes import auth_bp
from .ai.routes import ai_bp
from .payments.routes import payments_bp

def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder=os.path.join(root_dir, 'templates'),
        static_folder=os.path.join(root_dir, 'static')
    )

    # Config
    if os.getenv('FLASK_ENV') == 'prod':
        app.config.from_object('config.ProdConfig')
    else:
        app.config.from_object('config.DevConfig')

    # License‑key check
    provided = os.getenv('LICENSE_KEY', '')
    if provided not in app.config['LICENSE_KEYS']:
        raise RuntimeError("❌ Invalid or missing LICENSE_KEY—access denied.")

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # External services
    stripe.api_key = app.config['STRIPE_SECRET_KEY']
    app.openai_client = OpenAI(api_key=app.config['OPENAI_API_KEY'])

    # Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp,     url_prefix='/auth')
    app.register_blueprint(ai_bp,       url_prefix='/ai')
    app.register_blueprint(payments_bp, url_prefix='/payments')

    return app