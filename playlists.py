#!/usr/bin/env python3

import sys  
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebPage
from lxml import html 
from lxml.etree import tostring
from lxml import etree
from io import StringIO     #py2 has it's own import

#we can't do an easy static scrape - billboard site loads data in with javascript, so modified this for py3...
#https://impythonist.wordpress.com/2015/01/06/ultimate-guide-for-scraping-javascript-rendered-web-pages/
#handy tip, PyQt5 is a part of anaconda (easy way to install)


#Take this class for granted.Just use result of rendering.
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  

    #issue:QNetworkReplyImplPrivate::error: Internal problem, this method must only be called once.
    #self.mainFrame().wait_load()   #https://github.com/jeanphix/Ghost.py/issues/62

    self.app.exec_()  

  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

def getPlaylists():
    url = 'http://www.billboard.com/charts'
    r = Render(url)  
    result = r.frame.toHtml()
    #This step is important.Converting QString to Ascii for lxml to process
    page = html.fromstring(str(result))
    innerhtml = tostring(page)
    htmlstr = innerhtml.decode("utf-8")
    f = StringIO(htmlstr)
    tree = etree.parse(f)
    playlists = tree.xpath("//span[contains(@class, 'field-content')]/a/@href")
    key = '/charts/'
    final = [ '##total {} lists. Remove the # prefix for the playlists you want.'.format(len(playlists)) ]
    for playlist in sorted(playlists):
        item = ''
        if playlist.startswith(key):
            item = playlist.split(key)[1]
        else:
            item = '#ERROR list invalid: {}'.format(playlist)
        final.append('#{}'.format(item))
    return final

if __name__ == '__main__':
    lists = getPlaylists() 
    print('\n'.join(lists))
