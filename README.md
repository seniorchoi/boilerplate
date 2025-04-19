# BlitzShip: AI Email Drafter

A boilerplate for an AI-powered email drafting app.

## Setup (2 Minutes)

### Linux/macOS
1. Clone: `git clone https://github.com/seniorchoi/boilerplate && cd boilerplate`
2. Create `.env` file and add API keys.
```bash
FLASK_SECRET_KEY=your_random_string
STRIPE_SECRET_KEY=sk_test_your_stripe_key
OPENAI_API_KEY=sk-your_openai_key
```
3. Run: `./setup.sh`

### Windows
1. Clone: `git clone <repo-url> && cd boilerplate`
2. Create `.env` file and add API keys.
```bash
FLASK_SECRET_KEY=your_random_string
STRIPE_SECRET_KEY=sk_test_your_stripe_key
OPENAI_API_KEY=sk-your_openai_key
```
3. Run: `setup.bat`

Open: `http://localhost:5000`

## Prerequisites
- Python 3.12+ (Poetry handles this).
- `pip` (comes with Python).

## Troubleshooting
- Python version issue? Install Python 3.12.7 from python.org.
- Email: support@blitzship.com

## Deploy (Optional)
- Use Render.com with your repo and `.env` variables.