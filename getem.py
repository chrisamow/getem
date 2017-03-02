#!/usr/bin/env python3

import os
import os.path
import json
import slugify      #pip awesome-slugify, pipreqs did not detect?
import easyargs
from distutils.spawn import find_executable
import findsource
import download
import songlist
import playlists


def processSong(songdesc, path):
    descstr = str(songdesc)
    songs = findsource.songSource(descstr)
    top = next(iter(songs.items()))
    print('***** Selected = {}'.format(top))
    ytcode = top[0]
    info = top[1]
    download.getInfo(ytcode, info)

    #include rank with leading zeros so they easily are sorted by mp3 player
    prettyname = '{:03d}_{}_{}'.format(songdesc.rank, songdesc, ytcode)
    fname = path + slugify.slugify(prettyname)
    j = json.dumps(info)
    #view json file with: cat info.json | python -m json.tool | less
    with open(fname+'.json', 'w') as f:
        f.write(j)
    download.getAudio(ytcode, fname+'.ogg')

def processPlaylists(charts):
    for chart in charts:
        sl = songlist.getSongs(chart)
        if len(sl) < 1:
            print('no playlist found with title: {}'.format(chart))
        else:
            if os.path.exists(chart):
                if not os.path.isdir(chart):
                    print('file in the way of new dir: {}'.format(chart))
                    exit(13)
            else:
                os.mkdir(chart)
            path = chart + '/'  #todo: os ind sep
            print('{} songs to download'.format(len(sl)))
            for s in sl:
                songdesc = s   #'sometitle someartist'
                processSong(songdesc, path)



@easyargs
def main(src='billboard', showplaylists=False, pl=None, plfile=None):
    """                                                                              
    GetEm - get electronic music\n
    download songs and info within the playlist - e.g. billboard charts\n
    for now in ogg - since android was not working well with mp3\n
    1. getem.py --showplaylists > list.m3u  #create playlists file then uncomment playlists for downloading\n
    2. getem.py --plfile list.m3u           #download all the uncommented playlists\n
    \n
    :param src: source for the playlist - for now only 1 src supported
    :param showplaylists: the available playlists, direct it to a file, to send with plfile option
    :param pl: one or more comma separated playlists
    :param plfile: a playlist to get
    """                                                                              
    if not src == 'billboard':
        print('Unsupported source: {}'.format(src))
        exit(10)
    if not (find_executable("ffmpeg") or (find_executable("avconv"))):
        print("ffmpeg or avconv needed")
        exit(11)

    if showplaylists:
        lists = playlists.getPlaylists()
        print('\n'.join(lists))
    elif pl:
        charts = pl.split(',')	#'dance-electronic-albums'  #'dance-electronic-songs'
        processPlaylists(charts)
    elif plfile:
        if not os.path.isfile(plfile):
            print('{} not found'.format(plfile))
            exit(12)
        charts = [ ]
        with open(plfile, 'r') as f:
            charts = [line.rstrip() for line in f if not line.startswith('#')]
        processPlaylists(charts)
    else:
        print('-h for help, follow the 2 steps model of use')



if __name__ == '__main__':
    main()

