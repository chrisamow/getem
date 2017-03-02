import playlists



def test_getplaylists():
    lists = getPlaylists()
    assert len(lists) > 1

