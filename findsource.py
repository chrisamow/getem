from urllib.request import urlopen  #note python3 version includes urllib2 functionality
from urllib.parse import quote
from bs4 import BeautifulSoup
from collections import OrderedDict


yd = 'youtube-dl' #source of the form https://www.youtube.com/watch?v=yKNxeF4KMsY


def songSource(description):
    """
    description ideally will include title and artist
    """
    textToSearch = description  #'hello world'
    query = quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    ret = OrderedDict()
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        h = vid['href']
        #avoid "https://googleads.g.doubleclick.net/"
        #and https://www.youtube.com/results?search_query=
        if h.startswith('/watch?v='):
            songAndList = h.split(sep='&list=')
            #link = 'https://www.youtube.com' + songAndList[0]
            #print(songAndList[0])
            ytcode = songAndList[0].split('watch?v=')[1]
            ret[ytcode] = { 'source':yd, 'query':description }
    return ret


def testSongSource():
    r = songSource('coldplay yellow')
    assert len(r) > 0

