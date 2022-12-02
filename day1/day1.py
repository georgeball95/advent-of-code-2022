#read in data
data = open('day1_input.txt', 'r').read().split('\n')

#empty strings for list of packs and individualelf packs

packs = []
pack = []

#loop over rows 

for calorie_value in data:
    
    #if not a blank
    if len(calorie_value) != 0:
        
        pack.append(int(calorie_value))
    
    #when get to blank, add list of calorie figures to packs and empty list
    else:
        
        packs.append(pack)
        pack = []
        
#get max total
total = sorted([sum(pack) for pack in packs])[:-1]

#get value of top three
total = sum(sorted([sum(pack) for pack in packs])[-3:])
        
        
    