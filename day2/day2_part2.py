#read in data
data = open('day2_input.txt', 'r').read().split('\n')[:-1]

#set scores for each move
move_scores = {"A":1,"B":2,"C":3}

#translate column 2 to column 1 values
move_translation = {"X":"A","Y":"B","Z":"C"}

#for each move, set opponent value that beats it
loss_values = {"A":"B","B":"C","C":"A"}

#define my move given result=loss and opponent move 
#i.e reverse the loss values dict
my_move_to_lose = {v: k for k, v in loss_values.items()}

#set new definition of XYZ
required_result = {"X":"L","Y":"D","Z":"W"}

#set points outcome of results
result_points = {"L":0,"D":3,"W":6}

#given result and oppo move, get input (my move)
def input_needed(result_needed, opponent_move):
    
    if result_needed == "D":
        
        my_move = opponent_move
        
    elif result_needed == "W":
        
        my_move = loss_values[opponent_move]
        
    else:
        
        my_move = my_move_to_lose[opponent_move]
        
    return my_move
    
scores_list = []

#loop over rounds
for i in data:
    
    #get choices
    my_move, opponent_move = i.split(" ")[-1], i.split(" ")[0]
    
    #given column 2 value, get result needed
    result_needed = required_result[my_move]
    
    #from result, opponent move get my input (move) required
    input_needed_value = input_needed(result_needed, opponent_move)
    
    #get user score for shape chosen
    shape_score = move_scores[input_needed_value]
    
    #given result, get score
    score = result_points[result_needed]
    
    scores_list.append(score+shape_score)

total = sum(scores_list)


