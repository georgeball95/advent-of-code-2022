#read in data
data = open('day6_input.txt', 'r').read().split('\n')[:-1]

#pos of first char where in set of 4 unique chars
first_marker_chars = []

#part 1 n=4, part 2 n=14
n=14

sets = []

for pos,char in enumerate(list(data[0])):

    #ignore first 3 chars (as <4) + python indexing
    if pos > n-2:
                
        p = list(data[0][pos-(n-1):pos+1])
        
        if len(set(p)) == n:
        
            #if all unique
            #+1 due to python indexing
            first_marker_chars.append(pos+1)
        
    else:
        
        pass
    
ans = first_marker_chars[0]

    