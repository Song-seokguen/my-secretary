import g
import os
import sys
import instruction_set
import dir_help
import dir_directory
import dir_youtube_dl


def path_screen(num):
    if int(num)==1:
        dir_help.help_instruction()
    elif int(num)==2:
        dir_directory.directory_instruction()
    elif int(num)==3:
        dir_youtube_dl.youtube_instruction()
    
    
