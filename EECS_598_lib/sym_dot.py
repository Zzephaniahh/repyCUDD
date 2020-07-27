import warnings # eliminate an annoying warning message about bidict.
warnings.filterwarnings("ignore", message="Python 2 support will be dropped in a future release.")
import in_place # used to write the file in place to install us pip install in_place
import re
#from bidict import bidict # to install use pip install bidict

class sym_dot_manager(): # takes a dot file and a bi-directional dict and adds symbolic names to the file
    def __init__(self, dot_filename, variable_dict):
        self.filename = dot_filename
        self.line = []
        self.constants_found_flag = False
        self.bi_direction_variable_dict = variable_dict

    def replace(self, match):
        return self.bi_direction_variable_dict.inverse[match.group(0)]

    def get_constants(self):
        if "CONST NODES" in self.line:
            self.line = re.sub('|'.join(r'\b%s\b' % re.escape(s) for s in self.bi_direction_variable_dict.inverse), self.replace, self.line)
            self.constants_found_flag = True



    def add_syms(self):
        with in_place.InPlace(self.filename) as file:
            for self.line in file:
                if "[style = invis]" in self.line: # a line in the dot format we would like to avoid.
                    file.write(self.line)
                    continue

                if not(bool(re.search(r'\d', self.line))): # this line uses regex to check if there are any numbers in the line
                    file.write(self.line)
                    continue


                if not self.constants_found_flag: # process the file up to the integer list
                    self.get_constants()

                else:
                    if "rank = same;" in self.line:
                        integer_variable = re.findall('[0-9]+', self.line)

                        self.line = self.line.replace(str(integer_variable[0]), self.bi_direction_variable_dict.inverse[str(integer_variable[0])], 1)
                file.write(self.line)
