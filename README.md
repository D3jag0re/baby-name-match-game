# Baby Name Match Game 

## Description 

The Baby Name Match Game is a web application that allows two users to independently select their preferences ("yes", "maybe", "no") for a list of baby names. At the end of the selection process, the application displays the names that both users selected as "yes" or "maybe".

## Workflow of the App

1. User 1 makes their selections for the list of names and submits their choices.
2. User 1 is redirected to a "submitted" page with a button to proceed to User 2.
3. User 2 makes their selections for the same list of names and submits their choices.
4. User 2 is redirected to a "submitted" page with a button to view the results.
5. The results page displays the names that both users selected as "yes" or "maybe".
6. The results page includes a "Start Over" button that wipes the database and returns to the homepage.

## Stack

* <ins>Frontend:</ins> HTML, CSS
* <ins>Backend:</ins> Flask (Python)
* <ins>Database:</ins> SQLite
* <ins>Server:</ins> Gunicorn (for deployment)
* <ins>Infrastructure:</ins> Terraform, Azure App Service
* <ins>CI/CD:</ins> GitHub Actions


## To Run Locally for Testing: 

1. Clone the repository:

    ```bash
    git clone https://github.com/D3jag0re/baby-name-match-game.git
    cd <your_repository>
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:

    ```bash
    python initialize_db.py
    ```

5. Run the Flask application:

    ```bash
    export FLASK_APP=app/main.py
    export FLASK_ENV=development
    flask run
    ```

    On Windows:

    ```bash
    set FLASK_APP=app/main.py
    set FLASK_ENV=development
    flask run
    ```

6. Open your browser and navigate to http://127.0.0.1:5000/ 

## To Deploy to Azure 

### Prerequisites

* Azure account
* Azure CLI installed
* Terraform installed

### Steps

* Blank
* Blank 
