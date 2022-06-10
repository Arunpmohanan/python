from ast import AnnAssign



def find_min_max(test_list):
    print(f' List {test_list}')

    max_val = test_list[0]
    min_val = test_list[0]
    
    for i in test_list:
        if max_val < i:
           max_val = i
    print(f'Maximum value in list {max_val}')        

    for i in test_list:
        if min_val > i:
           min_val = i
    print(f'Minimum value in list {min_val}')        

    
test_list = [1,2,3,4,8,6,7,9,-1]

find_min_max(test_list) 




