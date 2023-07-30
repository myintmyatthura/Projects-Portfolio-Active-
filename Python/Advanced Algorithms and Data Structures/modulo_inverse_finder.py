def find_inverse(starting_number,mod_number):
    var = starting_number
    while var%mod_number != 1:
        print(var/starting_number)
        var+=starting_number
    print(f"{var/starting_number} is the inverse number")
        

        
        
def find_b_value(a,range_start,range_end,c):
    var = a
    for i in range(range_start,range_end+1):
        if (var-i) % c == 0:
            print(f"{i} is one of the b values")
            
        else:
            print("b value not found yet")

            
find_b_value(912,0,11,11)
        
    
    