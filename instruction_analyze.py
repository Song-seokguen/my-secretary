import instruction_set as iset
import g

"""
analyze the instruction that users typed


"""

def tokenizer(command):
    command=command.strip().split()
    return command

def check_instruction(command):
    command=tokenizer(command)
    for i in iset.instruction:
        if i==command[0]:
            g.instruction_available = True
            return True
            break
        else:
            g.instruction_available = False
        
    return g.instruction_available

def what_instruction(command):
    command=tokenizer(command)
    return iset.instruction[command[0]]

    
        
        

