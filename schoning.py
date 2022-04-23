import random

from bs4 import ResultSet
import prompt_toolkit


class Schoning:

    total_string = None     # Input and 
    bit_form = None         # Bits are Parallel

    def experiment(self):
        self.get_input()
        resulted_string = self.get_string(self.num_bits, self.num_clauses)
        print(resulted_string)

    def get_input(self):
        self.num_bits = int(input('Number of Bits: '))
        self.num_clauses = int(input('Number of Clauses: '))

    def get_string(self, bits, clauses):
        strings = []
        for num in range(clauses):
            while True:
                clause = str(input('Inputs: ')) 
                clause = clause.strip(' ')
                clause_split = clause.split(' ')
                formatted_lst = []
                for letter in clause_split:
                    if letter == '' or letter == ' ':
                        continue 
                    else:
                        prompt_input = str(input('True or False: '))
                        prompt_input = prompt_input.strip(' ')
                        dictionary = {letter:prompt_input}
                        formatted_lst.append(dictionary)

                    
                if len(formatted_lst) == bits:
                    strings.append(formatted_lst)
                    break 
                else:
                    print('There aren not enough inputs')

        
        return strings

test = Schoning()
print(test.experiment())