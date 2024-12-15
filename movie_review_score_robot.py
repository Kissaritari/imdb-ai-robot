import os
from robocorp.tasks import task
from robocorp import workitems, browser
from email_handler import EmailHandler
from gemini_handler import GeminiHandler


@task
def get_movie_review_score_from_email():

    gemini = GeminiHandler()
    mail = EmailHandler()
    
    title = parse_input_email()
    print(title)
    get_movie_summary(title)
    gemini.get_review_score(title)


def parse_input_email() -> str:
     for item in workitems.inputs:
        email = item.payload["email"]
        return email["text"]

def get_movie_summary(title) -> str:
    """Get the movie summary from rotten tomatoes. The site search does not work well with years, so it is left out here."""
    browser.goto("https://www.rottentomatoes.com/")
    search_selector = "#header-main > search-results-nav:nth-child(3) > search-results-controls:nth-child(1) > input:nth-child(1)"  # selectors generated with firefox inspect
    browser.page().fill(search_selector, title)
    first_result_selector = "#header-main > search-results-nav:nth-child(3) > search-results:nth-child(2) > search-results-item:nth-child(2) > rt-link:nth-child(2)"
    browser.page().click(first_result_selector)

    text = browser.page().inner_text(
        'div[slot="description"] drawer-more rt-text[slot="content"]'
    )
    print(text)
    return text
