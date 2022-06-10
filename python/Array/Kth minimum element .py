
def k_min(test_list,k):

    max_val = 0 
    temp_list = []
    length = len(test_list)
    for j in range(0,length):
       max_val = 0 
       length = len(test_list) 
       for i in range(0,length):
           if max_val < test_list[i]:
               max_val = test_list[i]

       print (f'maxval {max_val}')
       temp_list.insert(0,max_val) 
       test_list.remove(max_val)  
    print (f' temp_list {temp_list}')     
       
    return temp_list[k+1]



test_list = [15,13,10,8,3,21]


print(k_min(test_list,1))





         
         

