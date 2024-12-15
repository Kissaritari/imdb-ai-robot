import os
from robocorp.tasks import task
from robocorp import workitems
from email_handler import email_handler
import gemini_handler 

@task
def get_movie_review_score_from_email():
    environment = os.getenv("ENV", "local")

    if environment == "local":
        os.environ['RPA_SECRET_MANAGER'] = 'RPA.Robocorp.Vault.FileSecrets'
        os.environ['RPA_SECRET_FILE'] = 'secrets.json'
   
    gemini = gemini_handler()
    mail = email_handler()

    for item in workitems.inputs:
        workitems.outputs.create(payload={"key": "value"})
        gemini.get_review_score()
