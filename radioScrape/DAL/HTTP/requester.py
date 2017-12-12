#class="playlist-img"
import requests
import bs4
from bs4 import BeautifulSoup

class Requester(object):

    def __init__(self,url):
        self.page = requests.get(url)


    def get(self):
        soup = BeautifulSoup(self.page.content, 'html.parser')
        print("soupified")
        print(soup.prettify())
        return soup


# def request():
#     def __init__(url):
#         page = requests.get("https://975pride.iheart.com/music/recently-played/")
#         page
#
#         soup = BeautifulSoup(page.content, 'html.parser')
#
#         print(soup.prettify())
#
#         mydivs = soup.findAll("div", {"class": "playlist-img"})


