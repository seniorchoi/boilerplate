from flask import Blueprint, render_template, redirect, url_for, flash, current_app, request
from flask_login import login_required, current_user
import stripe

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/buy', methods=['GET', 'POST'])
@login_required
def buy():
    if request.method == 'GET':
        return render_template('credits.html')
    # POST: create checkout
    try:
        domain = current_app.config.get('APP_DOMAIN', 'http://localhost:5000')
        session_checkout = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': '50 Credits'},
                    'unit_amount': 1000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f'{domain}/payments/success',
            cancel_url=f'{domain}/payments/buy',
        )
        return redirect(session_checkout.url, code=303)
    except Exception as e:
        flash('Payment failed. Please try again.')
        return redirect(url_for('payments.buy'))

@payments_bp.route('/success')
@login_required
def success():
    current_user.credits += 50
    from ..models import db
    db.session.commit()
    flash('50 credits added!')
    return redirect(url_for('ai.dashboard'))