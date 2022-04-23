import random
from unittest import result

from bs4 import ResultSet
from matplotlib.font_manager import list_fonts
import prompt_toolkit


class Schoning:

    total_string = None     # Input and 
    bit_form = None         # Bits are Parallel
    initial_string = None

    def experiment(self):
        self.get_input()
        resulted_string = self.get_string(self.num_bits, self.num_clauses)
        self.initial_string = resulted_string
        print('Resulting String:  ')
        print(resulted_string)
        print('\n') 
        print('Resulting Bits: ')
        resulting_bits = self.result(resulted_string)
        print(resulting_bits)
        print('\n')
        fetched_inputs = self.fetch_numbers(resulted_string)
        print(fetched_inputs)
 


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
    
    def result(self, strings):
        bits = []
        for lst in strings:
            binary_num = []
            for dictionary in lst:
                for number, state in dictionary.items():
                    state = state.strip(' ')
                    state = state.title()
                    if state == 'True':
                        binary_num.append(1)
                    else:
                        binary_num.append(0)
            
            bits.append(binary_num)
        
        return bits 

    def fetch_numbers(self, strings):
        lst_of_inputs = []
        for lst in strings:
            for dictionary in lst:
                for number in list(dictionary.keys()):
                    number = int(number)
                    lst_of_inputs.append(number)

        new_lst = []
        length = len(self.initial_string[0])
        random_idx = []
        for i in range(length):
            idx = random.randint(0, length - 1)
            random_idx.append(idx)
    
        for input_idx in range(len(lst_of_inputs)):
            for idx in random_idx:
                if idx == input_idx:
                    new_lst.append(lst_of_inputs[input_idx])
                else:
                    continue 
        
        lst_of_inputs = new_lst          
        
        return lst_of_inputs

    
    def goal(self, lst_of_inputs):
        params = {}
        length = len(self.initial_string[0])
        counter = 0 
        for input_num in lst_of_inputs:
            pass 

            

test = Schoning()
print(test.experiment())