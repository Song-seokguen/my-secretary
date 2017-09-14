import g
import message
import os
import sys
import instruction_analyze as iana
import instruction_set as iset
import screen

def help_instruction():
    temp = iana.tokenizer(g.user_command)
    if len(temp) == 1 :
        g.content=g.content+' '+message.help_topics
    elif temp[1]=='directory':
        g.content=g.content+message.help_directory
    elif temp[1]=='cd':
        g.content=g.content+message.help_cd
    elif temp[1]=='youtube_dl':
        g.content=g.content+message.help_youtube_dl
    else:
        g.content='Command has wrong argument, comple the Sentence'
    
    
