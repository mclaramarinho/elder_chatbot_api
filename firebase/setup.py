from firebase_admin import initialize_app, db, credentials
from firebase.config import firebase_config
from os import environ
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"https://{environ['PROJECT_ID']}-default-rtdb.firebaseio.com"

cred = credentials.Certificate(firebase_config)

def init_firebase_app():
  initialize_app(cred, options={'databaseURL': DATABASE_URL})

