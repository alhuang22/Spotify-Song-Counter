#Updates the pickle file with new song counts.

import pickle
from datetime import datetime

def view_count():
    with open('songCount.txt.pickle','rb') as handle:
        song_dict = pickle.load(handle)
    with open('viewDict.txt', 'w') as text:
        text.write('Started counting as of May 3, 2020 \n')
        now = datetime.now()
        text.write('Last updated:  %s \n\n' % (now))
        for key, value in song_dict.items():
            text.write(str(key) + '  :  ' + str(value // 2) + '\n')
    print('Updated viewDict.txt file!')

view_count()
