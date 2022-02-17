# Demo User App
This demo app demonstrates the use of Flask-Login for a simple login system for a Flask application.

## Setup
**Note:** This app uses a PostgreSQL database along with `Flask-SQLAlchemy` and `Flask-Migrate`.

To begin using this app you can do the following:

1. Clone the repository to your local machine.
2. Create a Python virtual environment e.g. `python -m venv venv` (or `python3 -m venv venv`)
3. Enter the virtual environment using `source venv/bin/activate` (or `.\venv\Scripts\activate` if you are using Windows) 
4. Install the dependencies using Pip. e.g. `pip install -r requirements.txt`. __Note:__ Ensure you have PostgreSQL already installed and a database created.
5. Copy the `.env.sample` file and rename to `.env`. Edit the file and enter your database credentials and database name.
6. Run the migrations by typing `flask db upgrade`
7. Ensure you add a user to your database to test the login system.
8. Start the development server using `python run.py`.
