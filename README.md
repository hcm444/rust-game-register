# Game Registration System

A simple Flask web application with Bulma CSS for user registration that communicates with an Elixir server over TCP port 4520.

## Setup

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Make sure your Elixir server is running and listening on port 4520

2. Start the Flask application:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## Features

- Clean and responsive UI using Bulma CSS framework
- User registration form with username, email, and password fields
- TCP communication with Elixir server
- Form validation and error handling
- Flash messages for success/error feedback

## Note

Make sure to update the `secret_key` in `app.py` with a secure key in production. 