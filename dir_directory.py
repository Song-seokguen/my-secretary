import g
import message
import os
import sys
import traceback
import instruction_analyze as iana
import instruction_set as iset
import screen
import pyperclip

"""
add, delete, view(list)
File path and File path's nickname
"""

def directory_instruction():
    command = iana.tokenizer(g.user_command)
    if len(command)==1:
        g.content='Command has lack of argument, complete the Sentecne'
    elif command[1]=='add':
        add_directory()
    elif command[1]=='list':
        list_directory()
    elif command[1]=='copy':
        copy_directory()
    else:
        g.content='Command has wrong argument, Check again'

def copy_directory():
    command = iana.tokenizer(g.user_command)
    addFile=open('add_directory.txt','r')
    addFile.readline()
    addFile.readline()
    for i in range(int(command[2])-1):
        addFile.readline()
    content = addFile.readline().split('\t')
    pyperclip.copy(content[1])
    g.content= g.content+content[1]+' was copied to clipboard'

def add_directory():
    command = iana.tokenizer(g.user_command)
    if len(command)!=4:
        g.content='Command has lack of argument, complete the Sentence'
        return
    if os.path.exists('add_directory.txt'):
        addFile = open('add_directory.txt','a')
        addFile.close()
    else :
        addFile = open('add_directory.txt','a')
        addFile.write(r'''File - File path and nickname
''')
        addFile.write(r'''|| number || File Path || nickname ||

''')
        addFile.close()
    """
    file_path - nickname file 가져와서 번호순으로 나눠 분석 후 새로운 내용 추
    """
    addFile=open('add_directory.txt','r')
    content = addFile.read().split('\n')
    addFile.close()

    addFile=open('add_directory.txt','r')
    num=1
    g.content = g.content+addFile.readline()
    g.content = g.content+addFile.readline()
    for i in content[2:]:
        cur_content = i.split('\t')
        if cur_content[0]=='':
            g.content=g.content+str(num)+'\t'+command[2]+'\t'+command[3]+'\n'
            break
        else:
            g.content=g.content+addFile.readline()
        num=num+1
    g.content = g.content+addFile.read()
    addFile.close()

    updateFile = open('add_directory.txt','w')
    updateFile.write(g.content)
    updateFile.close()
    

    

def list_directory():
    """
    show file_paht - nickname list
    """
    if os.path.exists('add_directory.txt'):
        addFile = open('add_directory.txt','a')
        addFile.close()
    else :
        addFile = open('add_directory.txt','a')
        addFile.write(r'''File - File path and nickname
''')
        addFile.write(r'''|| number || File Path || nickname ||

''')
        addFile.close()
    addFile = open('add_directory.txt','r')
    g.content = addFile.read()
