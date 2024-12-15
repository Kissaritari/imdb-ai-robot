from RPA.Robocorp.Vault import Vault
import os
import google.generativeai as genai

class gemini_handler:
    def __init__(self):
        secret = Vault().get_secret("secrets")
        apiKey = secret['apikey']

''' Get review score for the movie.
    Inputs 
    name : str the name of the movie.
    year : str (optional) the year the movie was released.
'''

def get_review_score(self, name : str , year : str):
    genai.configure(api_key = self.GEMINI)
    if year:
        year = f"that is released on {year}"
    else:
        year = ""

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"Get the IMDB review score for the movie {name} {year}.")
    return(response.text)