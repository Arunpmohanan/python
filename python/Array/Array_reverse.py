def reverse_array(test_list):
  
  length = len(test_list)
  count = int(length/2)

  for i in range(0,count):
  
    test_list[i] , test_list[length-1-i] =  test_list[length-1-i], test_list[i]
    
  return test_list

def reverse_array_temp(test_list):

    temp_list = []

    for i in test_list:
        temp_list.insert(0,i)
    
    return temp_list 



test_list = [1,2,3,4,5,6,7,8]
print(reverse_array(test_list))
print(reverse_array_temp(test_list))










