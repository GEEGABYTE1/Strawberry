import random


class Schoning:

    total_string = None     # Input and 
    bit_form = None         # Bits are Parallel
    initial_string = None
    goal_ref = None

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
        print('Fetched Inputs: ')
        fetched_inputs = self.fetch_numbers(resulted_string)
        print(fetched_inputs)
        print('\n')
        print('Goal Parameter: ')
        goal = self.goal(fetched_inputs)
        self.goal_ref = goal
        print(goal)
        print('\n')
        print('Solution: ')
        solution = self.solution(resulted_string, goal)
        print(solution)



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
        params = []
        length = len(self.initial_string[0])
        counter = 0 
        for input_num in lst_of_inputs:
            if counter >= length:
                break 
            else:
                input_num = int(input_num)
                boolean_setter = random.randint(1, 2)
                if boolean_setter == 1:
                    dictionary = {input_num:True}
                    params.append(dictionary)
                else:
                    dictionary = {input_num:False}
                    params.append(dictionary)

            
            counter += 1

        return params 

    
    def solution(self, lst_of_inputs, goal):
        solution_indicies = []
        goal_ref = []
        #goal_bit_one = goal[0]
        #goal_bit_two = goal[-1]
        counter = 0 
        for string in lst_of_inputs:
            boolean_trues = []
            if counter >= 1:
                goal = goal_ref
                goal_ref = []
            relative_counter = 0
            for dictionary in string:
                    for relative_name, relative_string in dictionary.items():
                        for goal_bit in goal:
                            goal_bit_one = goal_bit
                            goal_bit_one_name = str(list(goal_bit_one.keys())[0])
                            goal_bit_one_state = str(list(goal_bit_one.values())[0])

                            if relative_name == goal_bit_one_name and goal_bit_one_state == relative_string:
                                boolean_trues.append(True)
                                break
                            elif relative_name == goal_bit_one_name and goal_bit_one_state != relative_string:
                                print('Updating {relative} to {desired}'.format(relative=relative_string, desired=goal_bit_one_state))
                                lst_of_inputs[counter][relative_counter][relative_name] = goal_bit_one_state
                                boolean_trues.append(True)
                                break
                            elif relative_name != goal_bit_one_name and goal_bit_one_state == relative_string:
                                print('Updating {relative} to {desired}'.format(relative=relative_name, desired=goal_bit_one_name))
                                new_dict = {int(goal_bit_one_name):relative_string}
                                lst_of_inputs[counter][relative_counter] = new_dict 
                                boolean_trues.append(True)
                                break
                            else:
                                break
                            
                        goal_ref.append(goal.pop(0))
                    relative_counter += 1

            counter += 1 
            bool_counter = 0
            for boolean in boolean_trues:
                if boolean == True:
                    bool_counter += 1
                else:
                    continue 
            
            if bool_counter == len(self.initial_string[0]):
                solution_indicies.append(counter)
            else:
                continue


                    
                    
            
        
        return solution_indicies
                    




                        
            

    

            

test = Schoning()
print(test.experiment())