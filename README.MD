##GetEm - Get Electronic Music
downloads music in chosen billboard charts from youtube.

```
getem.py --showplaylists > list.m3u  #create playlists file then uncomment playlists for downloading
getem.py --plfile list.m3u           #download all the uncommented playlists
```

#Details
The playlists are scraped from Billboards website.  It is javascript driven so the page can't be statically scraped.
Webkit is used to get everything after the data is async fetched.  Then lxml is used for parsing - scraping is fragile
as always.
  
The songs for the playlist are fetched using the unofficial billboard api - thank you sir!
  
The download candidates are based on youtube searching.  Initially, the plan was to create a scoring system to increase
the likelihood of getting the official video (e.g. search for vevo) but so far testing shows that the first in the list
is the one we want. "I'm Feeling Lucky"
  
The actual downloading is done via the youtube-dl library.  Truly awesome.
A 0 padded number is prefixed to easily preserve order.
mp3 was causing headaches on my android devices so I switched to vorbis/ogg and things seem to work fine.
TODO:make that a commandline option
