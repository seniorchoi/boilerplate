:: setup.bat
@echo off

:: Check if Poetry is installed
where poetry >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Installing Poetry...
    pip install --user poetry
)

:: Install dependencies
echo Installing dependencies with Poetry...
poetry install --no-root

:: Check if .env exists
if not exist .env (
    echo Error: .env file not found. Please create .env from .env.example and add your API keys.
    exit /b 1
)

:: Run database migrations
echo Setting up database...
poetry run flask db init || echo Database already initialized
poetry run flask db migrate
poetry run flask db upgrade

:: Start the app
echo Starting the app...
poetry run flask run