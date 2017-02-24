import youtube_dl

#http://stackoverflow.com/questions/18054500/how-to-use-youtube-dl-from-a-python-program

def getInfo(ytcode, metadata):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

    with ydl:
        result = ydl.extract_info(
            'https://www.youtube.com/watch?v={}'.format(ytcode),
            download=False # We just want to extract the info
        )
        metadata['youtubedata'] = result
    return result


def getAudio(ytcode, filename):
    """
    this will require avconf or ffmpeg be installed
    """
    print('getAudio for {} file:{}'.format(ytcode, filename))
    ydl_opts = {
        'outtmpl': filename,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'vorbis',     #instead of ogg
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v={}'.format(ytcode)])

