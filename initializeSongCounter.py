#Initializes the counter dictionary and stores it in a pickle file.

import pickle

song_counter = {}
with open('songCount.txt.pickle', 'wb') as handle:
    pickle.dump(song_counter, handle)
print('Initialized empty counter.')
