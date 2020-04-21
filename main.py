# https://pythonhosted.org/pafy/
# https://bigl.es/tooling-tuesday-pafy/

# TODO: How to stop the script after 12 hours
#       preferably without counting out 12 hours in the script

import vlc
import pafy
import random

_URL_ = 'https://www.youtube.com/playlist?list=PL0nQIgtfi8hrg5Kk4ZXmkR6svR04QHAOW'

def main():
    playlist = pafy.get_playlist(_URL_)
    urls = [i['pafy'].getbest().url for i in playlist['items']]
    random.shuffle(urls)
    while True:
        for i in urls:
        media = vlc.MediaPlayer(i)
        media.play()


if __name__ == '__main__':
    main()