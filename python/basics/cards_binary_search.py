from ast import Return
from urllib.parse import quote_from_bytes


def locate_card(card,query):

  mid_pos = len(card)//2
  
  while mid_pos > 0:
   
   print (f'mid pos {mid_pos} card {card} query {query}') 

   if card[mid_pos]  == query:
     return mid_pos
   else:
      if card[mid_pos] >  query:
        card = card[mid_pos:]

      else:
        card = card[:mid_pos]  
   mid_pos = len(card)//2

  return -1
        
#Test cases
tests =  []
tests .append ({ 'input' : {
            'cards' : [13,11,9,8,7,4,3,1],
            'query' : 7
        } ,
       'output':4
})

tests .append ({ 'input' : {
            'cards' : [13,11,9,8,7,4,3,1],
            'query' : 13
        } ,
       'output':0
})

tests .append ({ 'input' : {
            'cards' : [13,11,9,8,7,4,3,1],
            'query' : 0
        } ,
       'output':-1
})

tests .append ({ 'input' : {
            'cards' : [13,11,9,8,7,4,3,1],
            'query' : 1
        } ,
       'output':7
})

tests .append ({ 'input' : {
            'cards' : [],
            'query' : 1
        } ,
       'output':-1
})


tests .append ({ 'input' : {
            'cards' : [13,11,9,8,7,4,3,1],
            'query' : 15
        } ,
       'output':-1
})

tests .append ({ 'input' : {
            'cards' : [13,13,11,9,8,7,4,3,1],
            'query' : 13
        } ,
       'output':0
})


tests .append ({ 'input' : {
            'cards' : [13,11,9,8,7,4,3,1],
            'query' : 11
        } ,
       'output':1
})

for testcase in tests:

    result = locate_card(testcase['input']['cards'],testcase['input']['query']) == testcase['output']

    print (result)

