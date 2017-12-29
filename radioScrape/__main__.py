# from radioScrape import StateCheck
import logging
from bs4 import BeautifulSoup
from DAL.HTTP.requester import Requester
import youtube_dl
import requests
import os
import datetime
from config.config import AppConfig
#get_ipython().system('pip install cv2')
from numba.tests.test_array_constants import dt

import yaml



logging.basicConfig(level=logging.DEBUG,
                    filename='radioScrape.log',
                    filemode='w',
                    format='%(asctime)s : %(name)s :'
                    )



if __name__ == '__main__':
    print("Starting application")
    print("Load config file")

    config = AppConfig()
    config.set_config_yml()
    #set target dir

    today = datetime.datetime.now().date().__str__()
    base = config.get_config_item('mp3_repo_base').__str__()
    dir = base + today + '/'
    print("Pull website to parse")
    soupObj = Requester("https://975pride.iheart.com/music/recently-played/")
    soup = soupObj.get()
    print(soup)
    mydivs = soup.findAll("div", { "class" : "playlist-img" })
    print(mydivs)
    myimg = soup.findAll("img")
    myimg.pop(0)
    imgAlt = []
    for img in myimg:
        imgAlt.append(img.get('alt', ''))


    def genYouTubeQuery(searchAlt):
        searchAlt.replace("''", "")
        searchAlt.replace("   ", "+")
        searchAlt.replace("  ", "+")
        searchAlt.replace(" ", "+")
        return searchAlt

    def gen_dir_extended(dir,inc):
        print(inc.__str__())
        dir_extended=(dir+inc.__str__()+'/').__str__()
        if not os.path.isdir(dir):
            os.mkdir(dir)
        if not os.path.isdir(dir_extended):
            os.mkdir(dir_extended)
        return dir_extended

    inc = 0
    for search in imgAlt:
        search = genYouTubeQuery(search)
        search
        searchContent = requests.get("https://www.youtube.com/results?search_query=" + search)
        searchContentSoup = BeautifulSoup(searchContent.content, 'html.parser')

        # print(searchContentSoup.prettify())
        query = "https://www.youtube.com/results?maxResults=5&search_query=" + search
        print(query)
        # today = datetime.datetime.now().date().__str__()
        # dir = 'd:/Music/radio_repo/pride_radio/' + today + '/'

        dir_extended = gen_dir_extended(dir,inc)
        inc=inc+1


        ydl_opts = {}
        tgt_path = dir_extended + '%(title)s.%(ext)s'
        ydl_opts = {'outtmpl': tgt_path ,'noplaylist' : True,'format': 'bestaudio/best','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}], }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([query])
            except:
                print("Error: Unsupported url: " + query.__str__())

        title='today'
        ext='songo'
        ydl_opts = {'outtmpl': 'd:/Music/radio_repo/pride_radio/%(title)s.%(ext)s',}


    # class Video(object):
    #     def __init__(self, path):
    #         self.path = path
    #
    #     def play(self):
    #         from os import startfile
    #         startfile(self.path)
    #
    #
    # class Movie_MP4(Video):
    #     type = "MP4"
    #
    #
    # movie = Movie_MP4(r"testVid.mp4")
    # movie.play()





