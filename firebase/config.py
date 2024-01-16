import os
from os import environ
from dotenv import load_dotenv
load_dotenv()



# Create the Firebase configuration dictionary
firebase_config = {
  "type": "service_account",
  "project_id": environ["PROJECT_ID"],
  "private_key_id": environ["PRIVATE_KEY_ID"],
  "private_key": environ["PRIVATE_KEY"],
  "client_email": f"firebase-adminsdk-mcrds@{environ["PROJECT_ID"]}.iam.gserviceaccount.com",
  "client_id": environ["CLIENT_ID"],
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": environ["X509"],
  "universe_domain": "googleapis.com"
}
