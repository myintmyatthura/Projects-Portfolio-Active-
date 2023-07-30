'''
Counting Sort

This sorting algorithm will
create a counting array of size max(og_array)+1
It will then count the occurences of each element in the og list
Then it will create a final array and add each element to the right place

Time Complexity - O(logn)

Space Complexity - O(n+m) where n in the input list and m is the counting
list

Space complexity - O(m) where we dont count the input list

The way this algorithm differs is that we are going to use a range for loop.
Consider this to be the counting arrray.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
countar = [0, 2, 1, 1, 0, 0, 1, 2, 1]

For loop goes range(countar[i]), therefore, if the index is 0, then we will not
go into the for loop. For example, there are 2 instances of 1, which means we will
go into the for loop once, set value, increment, all done 2 times. 

Main issues - Large data inputs. If the min is 200 and max is 300. Everything below
200 is wasted space [0,1,....,200]. Counting array space becomes huge.

This algorithm is unstable. But we can make it stable.

We use something called a bucket variant. Instead of setting count array to be a list with 
length 1+max_item (lets say 8 for example). We create 8 lists within the count_array. To prevent a mess
with the mini-lists, we make sure to add a line where we make sure all the mini-lists are empty. Then we use
append to append the numbers inside the list. Same numbers will go inside the same mini-list. Then we will modify the
final for loop so that it becomes a for loop to traverse a 2d array. Frequency will be changed to len(mini_list) And we 
will use that value to decide whether we enter the loop or not. If len(mini_list) < 1, then we do not enter. Same principals with 
different changes.

Space complexity change - Due to the multiple mini-lists formed, the pay-off for making counting sort stable is the change in auxilary space.
                          It is quite similar to seperate chaining. Total space remains at O(N+M) but auxilary space changes to O(N+M).
                          There is going to be N number of items in the count_arr anyway, its just that these elements are spread out.
                          

'''

def counting_sort(og_list):
    # finding maximum
    max_item = og_list[0]
    for item in og_list:
        if item>max_item:
            # if new max is found, set it to new max
            max_item = item
    # create a count array with length max+1
    count_array = [0]*(1+max_item)
    
    # update count array
    for item in og_list:
        count_array[item] = count_array[item]+1
    print([0,1,2,3,4,5,6,7,8])
    print(f"this is the count array\n{count_array}")
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            og_list[index]=item
            index+=1
    return og_list

def counting_sort_stable(og_list):
    # finding maximum
    max_item = og_list[0]
    for item in og_list:
        if item>max_item:
            # if new max is found, set it to new max
            max_item = item
    # create a count array with length max+1
    count_array = [None]*(1+max_item)
    for i in range(len(count_array)):
        count_array[i] = []
    
    # update count array
    for item in og_list:
        count_array[item].append(item)
    print([0,1,2,3,4,5,6,7,8])
    print(f"this is the count array\n{count_array}")
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = len(count_array[i])
        for j in range(frequency):
            og_list[index]=count_array[i][j]
            index+=1
    return og_list

def counting_sort_alpha(og_list):
    # finding maximum
    max_item = ord(og_list[0])-97
    for item in og_list:
        item = ord(item)-97
        if item>max_item:
            # if new max is found, set it to new max
            max_item = item
    # create a count array with length max+1
    count_array = [0]*(1+max_item)
    
    # update count array
    for item in og_list:
        item = ord(item)-97
        count_array[item] = count_array[item]+1
    print([0,1,2,3,4,5,6,7,8])
    print(f"this is the count array\n{count_array}")
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            og_list[index]=chr(item+97)
            index+=1
    return og_list

        
list1 = [1,3,2,2,6,5]
print(f"this is the original list \n{list1}")                 
list1 = counting_sort_stable(list1)
print(list1)


    
