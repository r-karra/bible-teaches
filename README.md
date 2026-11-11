# Flask Authentication App

This is a simple Flask web application that demonstrates a basic user authentication system with registration and login functionality.

## Project Structure

The project is structured using Flask Blueprints and the Application Factory pattern to promote modularity and scalability.

```
/
|-- __init__.py         # Application factory
|-- run.py              # Entry point to run the application
|-- forms.py            # WTForms definitions
|-- models.py           # SQLAlchemy User model
|-- extensions.py       # Flask extension initializations (db, login_manager)
|-- requirements.txt    # Python dependencies
|-- routes/             # Blueprint routes
|   |-- __init__.py
|   |-- auth.py         # Authentication routes (login, register, logout)
|   `-- home.py         # Home page route
|-- templates/          # HTML templates
|   |-- home.html
|   |-- login.html
|   `-- register.html
`-- static/             # Static files (CSS, JS)
```

## Prerequisites

- Python 3
- Virtual Environment

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Activate the Virtual Environment:**
    The project is configured to use a virtual environment located in the `.venv` directory. You must activate it before installing dependencies or running the application.
    ```bash
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    Install all the required Python packages from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Once the setup is complete, you can start the Flask development server.

1.  **Run the application:**
    ```bash
    python run.py
    ```

2.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:3000` or the address provided in your terminal.

## Key Features

- **Application Factory (`__init__.py`):** The `create_app` function initializes the Flask application, configures it, and registers the necessary extensions and blueprints.
- **Blueprints (`routes/`):** The application is divided into Blueprints for better organization. The `auth_bp` handles authentication logic, while the `home_bp` handles the main landing page.
- **Database (`models.py`, `extensions.py`):** Uses Flask-SQLAlchemy for database interactions. The `User` model is defined in `models.py`, and the database connection is managed in `extensions.py`.
- **Forms (`forms.py`):** Uses Flask-WTF to create and validate web forms for user registration and login.
