def find_inverse(starting_number,mod_number):
    var = starting_number
    while var%mod_number != 1:
        print(var/starting_number)
        var+=starting_number
    print(f"{var/starting_number} is the inverse number")
        
find_inverse(15,56)
        
        
    
    
    