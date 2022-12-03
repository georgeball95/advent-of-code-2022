import string

#read in data
data = open('day3_input.txt', 'r').read().split('\n')

#get strings of alphabet
lowercase, uppercase = string.ascii_lowercase,string.ascii_uppercase

#assign values to the letters
letter_value = {}

for letter, value in zip(list(lowercase)+list(uppercase),range(1,53)):
    
    letter_value[letter]=value
    
grand_total = 0

#loop over packs
for i in data[:-1]:
    
    half_length = int(len(i)/2)
    
    #get first/second half
    first_half, second_half = i[:half_length], i[half_length:]
    
    #get items contained in both
    common_letters = list(set([i for i in list(first_half) if i in list(second_half)]))
    
    score = 0
    
    #get score from common letter and add to total
    for letter in common_letters:
        
        score += letter_value[letter]
                               
    grand_total += score
    
#part 2
    
#every three lines is a new group
#identified by a single common item in each group
#get priority score and total

#get list of sets of three packs
sets_of_three = []

for x, pack in zip(range(1,len(data[:-1])+1),data[:-1]):
    
    if x% 3 == 0:
        
        set_of_three = data[:-1][(x-3):x]
    
        sets_of_three.append(set_of_three)

total_score = 0

for group in sets_of_three:
    
    #get common letter
    common_letter = list(set([i for i in group[0] if i in group[1] and i in group[2]]))[0]
    
    #add value for letter to total score
    total_score += letter_value[common_letter]
    