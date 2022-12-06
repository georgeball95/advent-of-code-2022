#read in data
data = open('day5_input.txt', 'r').read().split('\n')[:-1]

#get index of whitespace in list
whitespace = data.index('')

crate_diagram = data[:whitespace]

orders = data[whitespace+1:]

#from crate diagram
#get list of lists of crates in order
#e.g. = {"1":[Q,M,R],"2":[Q,W,E]} ...

#each object takes up 3 chars + a blank

row_dict = {}

for row_number, i in enumerate(crate_diagram[:-1]):

    x = str(i)[::4].index("[")
    
    letter_indexes = []
    blank_indexes = []
    
    for n, character in enumerate(str(i)[::4]):
        
        if character == "[":
            letter_indexes.append(n)
        else:
            blank_indexes.append(n)
    
    #get list of letters
    letter_values = [i for i in list(i[1::4]) if i != ' ']
    
    #blank 9 char white space
    row_string = [' ']*9
    
    for index, char in zip(letter_indexes, letter_values):
        
        row_string[index] = char
        
    row_dict[row_number+1] = row_string
    
#get in column form not row
column_dict = {}

for j in list(range(9)):
    
    col_values = []
    
    #loop over all keys in dict
    for i in row_dict:
        
        #get jth item of ith value
        
        #don't need blanks
        if row_dict[i][j] == ' ':
            
            pass
        
        else:
            
            col_values.append(row_dict[i][j])
    
    column_dict[j+1] = col_values

#start of list == top of pile

def parse_instruction(instruction):

    n_boxes, start_pos, end_pos = instruction.split(" ")[1],instruction.split(" ")[3],instruction.split(" ")[5]
    
    return (n_boxes, start_pos, end_pos)

list_of_orders = []

for i in orders:
    
    list_of_orders.append(parse_instruction(i))
    
#move n boxes from x to y
def get_n_boxes(n, column):
    
    box_list = column[:n]
    
    return box_list[:n]

def move_boxes(instructions, current_pile_setup):
    
    n, x, y = int(instructions[0]),int(instructions[1]),int(instructions[2])   
    
    boxes_to_move = get_n_boxes(n, current_pile_setup[x])
    
    stack_setup = current_pile_setup[y]
        
    #reverse due to order picked up in
    #new_arrangement = boxes_to_move[::-1] + stack_setup
    
    #part 2 - don't reverse boxes
    new_arrangement = boxes_to_move + stack_setup
    
    #define new arrangement
    current_pile_setup[y] = new_arrangement
    
    #remove boxes from original column - i.e. take n boxes off
    #define column where boxes removed from
    current_pile_setup[x] = current_pile_setup[x][n:]
        
    return current_pile_setup

new_setup = column_dict

for x in list_of_orders:
    
    new_setup = move_boxes(x,new_setup)

ans = ""

for i in new_setup:
    
    ans += new_setup[i][0]
    


    
    
    
    
    
    
            
    
    
    
    
    