'''Given two unsorted arrays that represent two sets (elements in every array are distinct), find the union and intersection of two arrays.

For example, if the input arrays are: 
arr1[] = {7, 1, 5, 2, 3, 6} 
arr2[] = {3, 8, 6, 20, 7} '''


from operator import contains


class set_test():

     union = []
     inter = []



def union_and_intersecion(test_list1,test_list2):
 
   test_list = set_test()
   test_list.union = test_list1
   
   for i in test_list1:

       if i in test_list2:
           test_list.inter.append(i)
       
   for i in test_list2:

       if i not in test_list.union:
            test_list.union.append(i)    

   return test_list



arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7] 

result = union_and_intersecion(arr1,arr2)

print(f'Union {result.union} /n Intersection {result.inter} ')
      








