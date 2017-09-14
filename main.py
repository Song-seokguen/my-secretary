import colorama as cl
import instruction_analyze as iana
import instruction_set as iset
import message
import sys
import time
import screen
import dir_help
import g


prompt = ">>"


def main():

    while(1):
        #screen
        if g.function_number==0:
            g.content=message.logo
            g.content=g.content+'\n'
            g.content=g.content+message.help_topics
            print(g.content)
        else:
            g.content=''
            screen.path_screen(g.function_number)
            print(g.content)

        g.user_command=''
        
        #prompt line
        g.user_command=(input(prompt))
        if(len(g.user_command)>0):
            if iana.check_instruction(g.user_command):
                g.function_number=iana.what_instruction(g.user_command)
                continue;
            else:
                print('Bad Syntex')


main()
            

    
    
    
