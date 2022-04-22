import random

from bs4 import ResultSet


class Schoning:

    total_string = None     # Input and 
    bit_form = None         # Bits are Parallel

    def get_input(self):
        self.num_bits = int(input('Number of Bits: '))
        self.num_clauses = int(input('Number of Clauses: '))
        


    def experiment(self):
        result = self.get_input()
        resulted_string = self.get_string(self.num_bits, self.num_clauses)
        self.total_string = resulted_string
        print(resulted_string)
        resulting_bits = self.string_to_bit(resulted_string)
        print(resulting_bits)
        self.bit_form = resulting_bits
        fetched_results = self.fetch_numbers(self.total_string)
        print(fetched_results)
        print('\n')
        print('Goals: ')
        goals = self.goal(fetched_results, resulted_string)


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
                        formatted_lst.append(letter)
                
                if len(formatted_lst) == bits:
                    strings.append(formatted_lst)
                    break 
                else:
                    print('There are not enough inputs')
            
        
        return strings 

    
    def string_to_bit(self, strings):
        bits = []
        for lst in strings:
            binary_num = []
            for number in lst:
                number = int(number)
                if number < 0:
                    binary_num.append(1)
                else:
                    binary_num.append(0)
            
            bits.append(0)
    
        return bits

    def fetch_numbers(self, strings):
        lst_of_inputs = []
        for lst in strings:
            for number in lst:
                number = int(number)
                if not number in lst_of_inputs:
                    lst_of_inputs.append(number)
                else:
                    continue 

        return lst_of_inputs

    def goal(self, lst_of_inputs, resulted_string):
        params = {}
        length = len(resulted_string[0])
        counter = 0 
        for input_num in lst_of_inputs:
            if counter >= length:
                break 
            else:
                print('ON or OFF for desired Result ')
                input_num = int(input_num)
                vals = list(params.keys())
                if input_num not in vals:
                    state = random.randint(1, 2)
                    if state == 1:
                        string = False 
                    else:
                        string = True 
                    
                    params[input_num] = string 
    
            counter += 1

    
        return params
        





test = Schoning()
print(test.experiment())