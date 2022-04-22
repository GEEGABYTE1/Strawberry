

from email.utils import formatdate


class Schoning:

    def get_input(self):
        self.num_bits = int(input('Number of Bits: '))
        self.num_clauses = int(input('Number of Clauses: '))
        


    def experiment(self):
        result = self.get_input()
        resulted_string = self.get_string(self.num_bits, self.num_clauses)
        print(resulted_string)


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


test = Schoning()
print(test.experiment())