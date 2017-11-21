#class="playlist-img"
import requests
import bs4
from bs4 import BeautifulSoup

def request():
    def __init__(url):
        page = requests.get("https://975pride.iheart.com/music/recently-played/")
        page

        soup = BeautifulSoup(page.content, 'html.parser')

        print(soup.prettify())

        mydivs = soup.findAll("div", {"class": "playlist-img"})

page = requests.get("https://975pride.iheart.com/music/recently-played/")
page
