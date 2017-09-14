import math
import copy
import random

import g,c
import util

logo='''
-----personal SecreTary-----
'''


help_topics='''
help 단어를 프롬프트에 입력해서 어떤 명령들이 있는지 볼 수 있습니다.

아래와 같이 크게 3개의 명령어가 있습니다.

'help cd' , 'help directory'와 같이 프롬프트에 입력하면 명령어 사용법을 확인할 수 있습니다.


Help Topics

Enter help <topic> for specific help:

    cd           : go to start screen
    directory    : Add file path that you want to store or Find file path you stored

    youtube_dl    : download youtube playlist as mp4 file
'''

help_cd='''
Change Screen

    cd - move to first screen
'''

help_directory='''
Add file path that you want to store or Find file path you stored

    directory add <file path> <nickname>  -  Add file
    directory delete <nickname> / <number> - delete file path you stored
    
    directory list  -  show stroed file path and nickname that you added
    directory copy <number> - copy the file path to clibboard
    n and p  -  continue search next/previous pages
'''

help_youtube_dl='''
Add internet URL that yout wnat to download playlist

    youtube_dl -u <URL>   - download youtube play list in the current directory
'''


