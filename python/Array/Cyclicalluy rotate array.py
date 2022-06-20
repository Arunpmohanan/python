''''Given an array, cyclically rotate the array clockwise by one. 

Examples:  

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}'''

def rotate(test_list):

    length = len(test_list)
    test_list.insert(0, test_list[length -1 ])
    test_list.pop()
    
    return test_list


arr1 = [1, 2, 3, 4, 5]
print (f'array {arr1}')

print (f'rotated  array {rotate(arr1)}')


arr2 =  [5, 1, 2, 3, 4]

print (f'array {arr2}')

print (f'rotated  array {rotate(arr2)}')









  
