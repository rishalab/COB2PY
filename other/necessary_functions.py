# necessary_functions.py


    
# -----------------------------  replace_hyphen_with_underscore ---------------------
def replacehypwund(input_string):
    return input_string.replace('-', '_')
# -----------------------------  INDENtATION PART  ----------------------------------

def add_indentation(indentation_level):
    return  '\t' * indentation_level

def increase_indentation(indentation_level):
    return indentation_level + 1

def decrease_indentation(indentation_level):
    if indentation_level > 0:
        return indentation_level - 1
    return indentation_level
class Inden:
    def __init__(self):
        self.loop_indentation_level = 0
    # self.loop_inden = 0
    def add_indentation(self):
        return add_indentation(self.indentation)

    def increase_indentation(self):
        self.indentation = increase_indentation(self.indentation)

    def decrease_indentation(self):
        self.indentation = decrease_indentation(self.indentation)
        
    def loop_inden_increment(self):
        self.loop_indentation_level+=1
    def loop_inden_decrement(self):
        self.loop_indentation_level-=1
    def get_loop_inden(self):
        return self.loop_indentation_level
# -----------------------------------------------------------------------------------------------------