import findsource


def testSongSource():                                                           
    res = findsource.songSource('coldplay yellow')                                           
    assert len(res) > 0                                                           

    for r in res:
        assert res[r]['source'] == 'youtube-dl' #only thing supported so far

