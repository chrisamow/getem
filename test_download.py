from os import path
import download



def test_download():
    song = 'ohno.ogg'
    download.getAudio('dQw4w9WgXcQ', song)

    assert path.getsize(song) > 3000000
    #makes sense, about a MB a minute, should be about 3494754

