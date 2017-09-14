import sys
import os
import shlex
import subprocess
import struct
import platform


def get_terminal_size():
    """getTerminalsize().

    -get width and height of console
    """

    """
    if sys.version_info>=(3,3):
        return get_terminal_size()
        """

    current_os = platform.system()
    tuple_xy=None

    if current_os =='Windows':
        tuple_xy = _get_terminal_size_windows()

        if tuple_xy is None:
            tuple_xy = _get_terminal_size_windows()

    
    if tuple_xy is None:
        tuple_xy=(80,25) #default value

    return tuple_xy


def _get_terminal_size_windows():
    """ Get terminal size on MS windows. """
    try:
        from ctypes import windll, create_string_buffer
        #stdin handle is -10
        #stdout handle is -11
        #stderr handle is -12
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h,csbi)

        if res:
            (bufx,bufy,curx,cury,wattr,left,top,right,bottom,maxx,maxy)=struct.unpack("hhhhHhhhhhh",csbi.raw)
            sizex=right-left+1
            sizey=bottom-top+1
            return sizex,sizey
    except:
        pass
    
def _get_terminal_size_tput():
    """Get terminal size using tput."""
    try:
        cols =int(subprocess.check_call(shlex.split('tput cols')))
        rows =int(subprocess.check_call(shlex.split('tput lines')))
        return (cols,rows)
    except:
        pass
