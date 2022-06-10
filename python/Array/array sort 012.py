'''Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.
Examples: 
 

Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}'''

def sort_012(test_list):
    indexOfOne = 0 
    temp_list=[]
    for i in test_list:
        if i == 0:
            temp_list.insert(0,i)
            indexOfOne += 1

        if i == 1:
            temp_list.insert(indexOfOne,i)
            indexOfOne += 1

        if i == 2:
            temp_list.append(i)
            
    
    return temp_list

test_list= [0, 1, 2, 0, 1, 2]

print(sort_012(test_list))

test_list= [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

print(sort_012(test_list))

           