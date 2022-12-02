#read in data
data = open('day2_input.txt', 'r').read().split('\n')[:-1]

#set scores for each move
move_scores = {"A":1,"B":2,"C":3}

#translate column 2 to column 1 values
move_translation = {"X":"A","Y":"B","Z":"C"}

#for each move, set opponent value that beats it
loss_values = {"A":"B","B":"C","C":"A"}

#define result given moves
def calc_score(my_move, opponent_move):

    #draw
    if my_move == opponent_move:
        
        score = 3
    
    #loss
    elif opponent_move == loss_values[my_move]:
        
        score = 0
    
    #otherwise wins
    else:
        
        score = 6

    return score

scores_list = []

#loop over rounds
for i in data:
    
    #get choices
    my_move, opponent_move = i.split(" ")[-1], i.split(" ")[0]
    
    #convert my move to ABC format
    my_move = move_translation[my_move]
    
    #get user score for move chosen
    shape_score = move_scores[my_move]
    
    #calc result
    score = calc_score(my_move,opponent_move)
    
    #add scores to list
    scores_list.append(score+shape_score)
        
total = sum(scores_list)




