# Initialize the flask app
#from flask import Flask

#app = Flask(__name__)

#from app import main
##############################

# Initialize the flask app
from flask import Flask
import os
import sys

# Ensure the parent directory is in the path so initialize_db can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the initialize_db function
from initialize_db import initialize_db

app = Flask(__name__)

# Call the initialize_db function
initialize_db()

from app import main
