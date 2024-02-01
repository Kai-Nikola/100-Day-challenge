from bs4 import BeautifulSoup
import requests

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
