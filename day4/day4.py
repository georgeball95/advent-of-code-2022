#read in data
data = open('day4_input.txt', 'r').read().split('\n')[:-1]

#function to get list of numbers from assignment 
def get_list(assignment):
    
    first_number, last_number = assignment.split("-")
    
    list_of_numbers = list(range(int(first_number), int(last_number)+1))
    
    return list_of_numbers

fully_contained_pairs = 0

overlapping_pairs = 0

for pair in data:

    first_elf, second_elf = pair.split(",")
    
    first_list, second_list = get_list(first_elf), get_list(second_elf)
    
    #get numbers in both lists
    common_numbers = [i for i in first_list if i in second_list]
    
    #check if fully contained pair
    if sorted(first_list) == common_numbers or sorted(second_list) == common_numbers:
        
        fully_contained_pairs +=1
        
    else:
        
        pass

    #check for overlapping_pairs
    if len(common_numbers) > 0:
        
        overlapping_pairs +=1
            
    
    

