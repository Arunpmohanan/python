''''An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5'''

def sort_negative(test_list):
  
   
    for i in test_list:
        if i < 0:
            test_list.remove(i)
            test_list.insert(0,i)
    
    return test_list

test_list= [10, -11, 2, -12, -1, 2]

print(sort_negative(test_list))

test_list= [-12, 11, -13, -5, 6, -7, 5, -3, -6]

print(sort_negative(test_list))
