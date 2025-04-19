#!/bin/bash
# setup.sh

# Exit on any error
set -e

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Installing Poetry..."
    pip install --user poetry
fi

# Install dependencies and set up virtual environment
echo "Installing dependencies with Poetry..."
poetry install --no-root

# Check if .env exists
if [ ! -f .env ]; then
    echo "Error: .env file not found. Please create .env from .env.example and add your API keys."
    exit 1
fi

# Run database migrations
echo "Setting up database..."
poetry run flask db init || true  # Ignore if already initialized
poetry run flask db migrate
poetry run flask db upgrade

# Start the app
echo "Starting the app..."
poetry run flask run