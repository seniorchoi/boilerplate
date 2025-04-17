from flask import Blueprint, render_template

# Name it “main” and no URL prefix → it handles `/`
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/demo')
def demo():
    return render_template('demo.html')