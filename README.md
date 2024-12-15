# IMBD - Rotten tomatoes lookup Robot

## Process
The process to be automated is as follows:  
Name a movie 
Find the review score for it (internet movie database in this case)  
Find the summary for it (rotten tomatoes in this case)  
Assemble a readable document of the info

## Robot
The robot is triggered via email, containing the title of the movie, and optionally the release year to single down movies with the same title. When triggered, the robot will first use gemini ai to get the review scores for the movie, and then use robocorp.browser to scrape the summary for the movie from rotten tomatoes website.

~~when the data is collected, the robot will assemble a readable html document of it, and email it to the sender of the trigger email.~~


## Running
send an email with a movie title and an optional release year in the body to  
process.koulu.imdbreviewro.2atpxvvimfv@mail.eu1.robocloud.eu

## Notes
Rotten tomatoes is not the best source of summaries, but it is what it is, and its not relevant to the task.
TIME RAN OUT FOR THE EMAIL, WOULD HAVE USED THE GMAIL-API

## Going forward
New functionalities could include
- multiple movies on the same email
- including the poster of the movie in the response
- including some bits of trivia in the response
- expanding the scope to the cast of the movies, or other forms of media such as video games or music