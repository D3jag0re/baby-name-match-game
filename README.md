# Baby Name Match Game 

## Description 

The Baby Name Match Game is a web application that allows two users to independently select their preferences ("yes", "maybe", "no") for a list of baby names. At the end of the selection process, the application displays the names that both users selected as "yes" or "maybe".

This is a simple app created to demonstrate automated deployments and CI/CD. 

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
* <ins>Infrastructure:</ins> Terraform, Azure App Service, Docker 
* <ins>CI/CD:</ins> GitHub Actions


## To Run Locally (without container) for Testing: 

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
    export FLASK_APP=app/__init__.py
    export FLASK_ENV=development
    flask run
    ```

    On Windows:

    ```bash
    set FLASK_APP=app/__init__.py
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

1. Clone the Repo 

2. Add the following secrets to your GitHub repository:
    * ARM_CLIENT_ID: Your Azure service principal client ID.
    * ARM_CLIENT_SECRET: Your Azure service principal client secret.
    * ARM_SUBSCRIPTION_ID: Your Azure subscription ID.
    * ARM_TENANT_ID: Your Azure tenant ID.
    * AZURE_STORAGE_ACCOUNT: The name of your Azure Storage Account.
    * AZURE_STORAGE_CONTAINER: The name of your Azure Storage Container.
    * AZURE_PUBLISH_PROFILE: The publish profile of your Azure App Service.

3. Commit and Push changes - to trigger the GitHub Actions workflow

4. Monitor the Deployment

5. Access the Application 
