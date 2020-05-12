if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print('Usage: %s username' % (sys.argv[0],))
    sys.exit()
scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope, client_id='00e7ddb7fe1844bba151f6898d13909d',
                                    client_secret='c32ded404f61477b984795ad6eeafc3a',
                                    redirect_uri='http://google.com/')

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    ranges = ['short_term', 'medium_term', 'long_term']
    for range in ranges:
        print('range:', range)
        results = sp.current_user_top_artists(time_range=range, limit=5)
        for i, item in enumerate(results['items']):
            print(i+1, item['name'])
        print()
    for range in ranges:
        print('range: ', range)
        tracks = sp.current_user_top_tracks(time_range=range,limit=5)
        for i, item in enumerate(tracks['items']):
            print(i+1, item['name'], item['artists'][0]['name'])
        print()
else:
    print('Can\'t get token for ', username)




lisa_uri = 'spotify:artist:0blbVefuxOGltDBa00dspv'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
artist = spotify.artist(lisa_uri)
url = artist['images'][0]['url']
results = spotify.artist_top_tracks(lisa_uri)
top = spotify.current_user_top_artists()
print(top)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()

link = results['tracks'][0]['preview_url']
#webbrowser.open(url, new=1)
