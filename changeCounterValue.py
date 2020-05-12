#Changes a value for a specified key.

import pickle
from datetime import datetime


def change_value(key, value):
    with open('songCount.txt.pickle','rb') as handle:
        song_dict = pickle.load(handle)
        song_dict[key] = int(value)
    print('Changed ' + key + ' value to ' + str(value) + '.')
    with open('viewDict.txt', 'w') as text:
        text.write('Started counting as of May 3, 2020 \n')
        now = datetime.now()
        text.write('Last updated:  %s \n\n' % (now))
        for key, value in song_dict.items():
            text.write(str(key) + '  :  ' + str(value // 2) + '\n')
    print('Updated the file.')
#Must be double the desired amount
change_value('Re:Re: - 2016 Rerecorded  -  ASIAN KUNG-FU GENERATION', 2)
