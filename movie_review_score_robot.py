import os
from robocorp.tasks import task
from robocorp import workitems
from email_handler import EmailHandler
from gemini_handler import GeminiHandler 

@task
def get_movie_review_score_from_email():
    environment = os.getenv("ENV", "local")

    if environment == "local":
        os.environ['RPA_SECRET_MANAGER'] = 'RPA.Robocorp.Vault.FileSecrets'
        os.environ['RPA_SECRET_FILE'] = 'secrets.json'
   
    gemini = GeminiHandler()
    mail = EmailHandler()

    for item in workitems.inputs:
        workitems.outputs.create(payload={"key": "value"})
        gemini.get_review_score(item.payload)
