
# coding: utf-8

# https://975pride.iheart.com/music/recently-played/

# In[1]:

#class="playlist-img"
import requests

page = requests.get("https://975pride.iheart.com/music/recently-played/")
page


# In[2]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())


# In[5]:

mydivs = soup.findAll("div", { "class" : "playlist-img" })


# In[6]:

print(mydivs)


# In[8]:

myimg = soup.findAll("img")


# In[9]:

myimg


# In[10]:

myimg.pop(0)
myimg


# In[11]:

n=5
del myimg[-n:]
myimg


# In[12]:

imgAlt = []
for img in myimg:
    imgAlt.append(img.get('alt', ''))


# In[13]:

imgAlt


# In[14]:

imgAlt


# In[15]:

import youtube_dl

def genYouTubeQuery (searchAlt):
    searchAlt.replace("''", "")
    searchAlt.replace("   ", "+")
    searchAlt.replace("  ", "+")
    searchAlt.replace(" ", "+")
    return searchAlt




for search in imgAlt:
    search = genYouTubeQuery(search)
    search
    searchContent = requests.get("https://www.youtube.com/results?search_query="+search)
    searchContentSoup = BeautifulSoup(searchContent.content, 'html.parser')

    #print(searchContentSoup.prettify())
    query = "https://www.youtube.com/results?search_query="+search
    print(query)
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([query])

#  def quadcube (x):
# ...     return x**2, x**3




# In[27]:

import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=lqj7pRnRcp8'])


# In[17]:

get_ipython().system('pip install cv2')


# In[19]:

class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = "MP4"

movie = Movie_MP4(r"testVid.mp4")
movie.play()


# In[24]:

get_ipython().system('pip install mplayer')


# In[20]:

class VideoPlayback_MPlayer:
    def __init__(self, path):
        self.path = path

    def playAsync(self):
        import mplayer #pip install mplayer.py and also setup choco install mplayer myself via http://downloads.sourceforge.net/project/mplayer-win32/MPlayer%20and%20MEncoder/r37451%2Bg531b0a3/MPlayer-x86_64-r37451%2Bg531b0a3.7z?r=http%3A%2F%2Foss.netfarm.it%2Fmplayer%2F&ts=1442363467&use_mirror=tcpdiag
        self.isPlaying = True

        EOFDetectionArgs = "-msglevel global=6"
        self.player = mplayer.Player(args=EOFDetectionArgs.split(), stderr=None, autospawn=True)
        self.player.stdout.connect(self._EOFDetector)
        self.player.loadfile(self.path) 
        self.player.pause() # someone says online this kicks in the audio http://stackoverflow.com/questions/16385225/play-mp4-using-python-and-check-if-while-it-is-still-playing       

    def _EOFDetector(self, stream):
        if stream.startswith('EOF code:'):
            self.isPlaying = False

    @property
    def done(self):
        return not self.isPlaying


    def play(self):
        self.playAsync()
        while self.isPlaying:
            time.sleep(0.00001)        

    @staticmethod
    def FromPath(path):
        return VideoPlayback_MPlayer(path)


# In[23]:

import mplayer 

p = 'testVid.mp4'
v = VideoPlayback_MPlayer.FromPath(p)
v.playAsync()
while v.isPlaying:
    time.sleep(0.1)


# In[3]:

get_ipython().system('pip install youtube_dl')


# In[5]:

import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www .youtube.com/watch?v=BaW_jenozKc'])


# In[6]:

get_ipython().system('pwd')


# In[7]:

get_ipython().system('ll')


# In[8]:

get_ipython().system('dir')


# In[1]:

get_ipython().system('pwd')


# In[ ]:



