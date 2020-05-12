#Runs every 10 seconds to check current song.

import webbrowser
import spotipy
import sys
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import pickle
import time


if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print('Usage: %s username' % (sys.argv[0],))
    sys.exit()
scope = 'user-read-currently-playing'
token = util.prompt_for_user_token(username, scope, client_id='PASTE CLIENT ID HERE',
                                    client_secret='PASTE CLIENT SECRET HERE',
                                    redirect_uri='http://google.com/')



sp = spotipy.Spotify(auth=token)
sp.trace = False
def check():
    #10,000 milliseconds = 10 seconds
    current = sp.currently_playing()
    if current == None:
        return False
    song = current['item']['name']
    artist = current['item']['artists'][0]['name']
    songAndArtist = song + '  -  ' + artist
    progress = current['progress_ms']
    duration = current['item']['duration_ms']
    threshold = duration - 10000
    if progress > threshold:
        with open('songCount.txt.pickle','rb') as handle:
            song_count = pickle.load(handle)
        if songAndArtist in song_count:
            song_count[songAndArtist] += 1
        else:
            song_count[songAndArtist] = 1
        with open('songCount.txt.pickle','wb') as handle:
            pickle.dump(song_count,handle)
    return True


while True:
    check()
    if not check():
        break
    time.sleep(10)
