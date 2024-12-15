from robocorp import vault

class email_handler:
    def __init__(self):
        secret = vault.get_secret("secrets")
        apiKey = secret['emailKey']

    def form_mail(self,content: str):
        pass
    
    def send_mail(self,sender: str, receiver: str):
        self.form_mail()
        pass