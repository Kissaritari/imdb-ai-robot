from robocorp import Vault

class email_handler:
    def __init__(self):
        secret = Vault().get_secret("secrets")
        apiKey = secret['emailKey']

    def form_mail(self,content: str):
        pass
    
    def send_mail(self,sender: str, receiver: str):
        self.form_mail()
        pass