# File: app/ai/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
import bleach

# Blueprint setup
ai_bp = Blueprint('ai', __name__)

# Form
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

class AIToolForm(FlaskForm):
    prompt = TextAreaField('Prompt', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Run AI')

@ai_bp.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@ai_bp.route('/tool', methods=['GET', 'POST'])
@login_required
def ai_tool():
    form = AIToolForm()
    result = None

    if current_user.credits <= 0:
        flash('No credits left!')
        return redirect(url_for('payments.buy'))

    if form.validate_on_submit():
        prompt = bleach.clean(form.prompt.data)
        openai_client = current_app.openai_client
        resp = openai_client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role':'user', 'content': f"Write a professional email: '{prompt}'"}],
            max_tokens=150,
        )
        result = resp.choices[0].message.content
        current_user.credits -= 1
        from ..models import db
        db.session.commit()

    return render_template('ai_tool.html',
                           form=form,
                           result=result,
                           credits=current_user.credits)
