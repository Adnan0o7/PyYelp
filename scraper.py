import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
number = 1
for question in questions:
    print(f"{number})",question.select_one(".question-hyperlink").getText())
    print("Votes:", question.select_one(".vote-count-post").getText()+"\n")
    number+=1