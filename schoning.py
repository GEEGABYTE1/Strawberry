

from email.utils import formatdate

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



test = Schoning()
print(test.experiment())