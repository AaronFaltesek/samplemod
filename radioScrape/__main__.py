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

def url_to_soup(url):
    soupObj = Requester(url)
    soup = soupObj.get()
    return soup

def genYouTubeQuery(searchAlt):
    searchAlt.replace("''", "")
    searchAlt.replace("   ", "+")
    searchAlt.replace("  ", "+")
    searchAlt.replace(" ", "+")
    return searchAlt

def gen_pride_song_list(url):
     soup = url_to_soup(url)
     mydivs = soup.findAll("div", {"class": "playlist-img"})
     myimg = soup.findAll("img")
     myimg.pop(0)
     song_list = []
     for img in myimg:
         song_list.append(img.get('alt', ''))
     song_list.pop()
     return song_list

def gen_dir_extended(dir,inc):
    print(inc.__str__())
    dir_extended=(dir+inc.__str__()+'/').__str__()
    if not os.path.isdir(dir):
        os.mkdir(dir)
    if not os.path.isdir(dir_extended):
        os.mkdir(dir_extended)
    return dir_extended

def first_video_link(query):
    soup = url_to_soup(query)
    print(soup)
    #<a aria-hidden="true" class=" yt-uix-sessionlink spf-link " data-sessionlink="itct=CEgQ3DAYACITCI2GwLn41dgCFQVVPwodJFoLXCj0JFIsQnkgTXkgU2lkZSAoRGVmbGVjdCBPcmlnaW5hbCBNaXgpIC0gRmxhbmRlcnM" href="/watch?v=P-xjICAbiGU">
    mydivs = soup.findAll("a", {"class": " yt-uix-sessionlink spf-link "})
    print(mydivs)
    first_html_a_element=mydivs[0]
    first_link=first_html_a_element['href']
    video_link='https://www.youtube.com'+first_link.__str__()
    return video_link.__str__()

if __name__ == '__main__':
    print("Starting application")

    config = AppConfig()
    config.set_config_yml()

    today = datetime.datetime.now().date().__str__()
    base = config.get_config_item('mp3_repo_base').__str__()
    dir = base + today + '/'

    print("Pull website to parse")

    url = "https://975pride.iheart.com/music/recently-played/"
    song_list = []
    song_list = gen_pride_song_list(url)

    print(song_list)




    inc = 0
    for song in song_list:
        search = genYouTubeQuery(song)

        query = "https://www.youtube.com/results?maxResults=5&search_query=" + search

        link_to_download = first_video_link(query)

        dir_extended = gen_dir_extended(dir,inc)
        inc=inc+1


        ydl_opts = {}
        tgt_path = dir_extended + '%(title)s.%(ext)s'
        ydl_opts = {'outtmpl': tgt_path ,'noplaylist' : True,'format': 'bestaudio/best','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}], }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([link_to_download])
            except:
                print("Error: Unsupported url: " + link_to_download.__str__())

        title='today'
        ext='songo'






