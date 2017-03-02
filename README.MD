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
  
The list.m3u might look like this:
  
```
##total 123 lists. Remove the # prefix for the playlists you want.
#adult-contemporary
#adult-pop-songs
#alternative-albums
#alternative-songs
#americana-folk-albums
#artist-100
#billboard-200
#billboard-twitter-realtime
#bluegrass-albums
#blues-albums
#canadian-albums
#canadian-hot-100
#catalog-albums
#china-v-chart
#christian-airplay
#christian-albums
#christian-digital-song-sales
#christian-songs
#christian-streaming-songs
#classical-albums
#comedy-albums
#country-airplay
#country-albums
#country-digital-song-sales
#country-songs
#country-streaming-songs
#dance-club-play-songs
#dance-electronic-albums
#dance-electronic-digital-song-sales
#dance-electronic-songs
#dance-electronic-streaming-songs
#digital-albums
#digital-song-sales
#france-songs
#german-albums
#germany-songs
#gospel-airplay
#gospel-albums
#gospel-digital-song-sales
#gospel-songs
#gospel-streaming-songs
#greatest-adult-pop-artists
#greatest-adult-pop-songs
#greatest-billboard-200-albums
#greatest-billboard-200-artists
#greatest-country-albums
#greatest-country-artists
#greatest-country-songs
#greatest-hot-100-artists
#greatest-hot-100-singles
#greatest-hot-latin-songs
#greatest-hot-latin-songs-artists
#greatest-top-dance-club-artists
#hard-rock-albums
#heatseekers-albums
#holiday-albums
#holiday-season-digital-song-sales
#holiday-songs
#holiday-streaming-songs
#hot-100
#hot-adult-r-and-b-airplay
#hot-canada-digital-song-sales
#hot-dance-airplay
#hot-holiday-songs
#hot-mainstream-rock-tracks
#hot-r-and-b-hip-hop-airplay
#independent-albums
#japan-hot-100
#jazz-albums
#jazz-songs
#kids-albums
#latin-airplay
#latin-albums
#latin-digital-song-sales
#latin-pop-albums
#latin-pop-songs
#latin-songs
#latin-streaming-songs
#lyricfind-global
#lyricfind-us
#new-age-albums
#next-big-sound-25
#on-demand-streaming-songs
#pop-songs
#r-and-b-albums
#r-and-b-hip-hop-digital-song-sales
#r-and-b-hip-hop-streaming-songs
#r-and-b-songs
#r-and-b-streaming-songs
#r-b-hip-hop-albums
#r-b-hip-hop-songs
#radio-songs
#rap-albums
#rap-song
#rap-streaming-songs
#reggae-albums
#regional-mexican-albums
#regional-mexican-songs
#rhythmic-40
#rock-airplay
#rock-albums
#rock-digital-song-sales
#rock-songs
#rock-streaming-songs
#social-50
#soundtracks
#spotify-rewind
#spotify-velocity
#spotify-viral-50
#streaming-songs
#summer-songs
#tastemaker-albums
#top-album-sales
#triple-a
#tropical-albums
#tropical-songs
#twitter-emerging-artists
#twitter-top-tracks
#united-kingdom-albums
#united-kingdom-songs
#vinyl-albums
#world-albums
#youtube
```
  
  
btw, the tests are not in their own directory because I think python3.6 has some py.test problems with the way modules are found - but I don't have time to hunt that down right now - there are some related googled/stackoverflow issues out there

