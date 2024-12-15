from robocorp import vault
from email.message import EmailMessage
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class EmailHandler:
    def __init__(self):
        secret = vault.get_secret("secrets")
        apiKey = secret["emailKey"]

    def form_mail(self, title: str, summary: str, score: str):
        pass

    def send_mail(self, sender: str, receiver: str):
        self.form_mail()
        pass
