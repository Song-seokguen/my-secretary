import os
import re
import sys
import ctypes
import time
import subprocess
import unicodedata
import logging
import collections
import terminalsize

mswin = os.name=="nt"
not_utf8_environment=mswin or "UTF-8" not in sys.stdout.encoding
XYTuple = collections.namedtuple('XYTuple','width height max_results')

def xenc(stuff): 
    """ Replace unsupported characters. """ 
    return utf8_replace(stuff) if not_utf8_environment else stuff

def xprint(stuff, end=None): 
    """ Compatible print. """ 
    print(xenc(stuff), end=end)

def set_window_title(title): 
    """ Set terminal window title. """ 
    if mswin: 
        ctypes.windll.kernel32.SetConsoleTitleW(xenc(title)) 
    else: 
        sys.stdout.write(xenc('\x1b]2;' + title + '\x07')) 


def getxy():
    """
    Get terminal size
    :rtype: :class:'XYTuple'
    """
    import config
    if g.detectable_size:
        x,y=terminalsize.get_terminal_size()
        max_results = y-4 if y<54 else 50
        max_results = 1 if y<=5 else max_results

    else:
        x,max_results=config.CONSOLE_WIDTH.get, config.MAX_RESULTS.get
        y=max_results+4

    return XYTuple(x,y,max_results)
    
