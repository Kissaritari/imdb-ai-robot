from robocorp import vault
import os
import google.generativeai as genai


class GeminiHandler:
    def __init__(self):
        secret = vault.get_secret("secrets")
        self.apiKey = secret["apikey"]


    def get_review_score(self, name: str, year: str = ""): 
        """ Get review score for the movie using the `genai` library with the "gemini-1.5-flash" generative model.
            Parameters:

        name : str
            The name of the movie.
        year : str, optional
            The year the movie was released. If not provided, the year will be excluded from the query.
        """
        genai.configure(api_key=self.apiKey)
        if year:
            year = f"that is released on {year}"
        else:
            year = ""

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            f"get the review score for the movie {name} {year}."
        )
        return response.text
