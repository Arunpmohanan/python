"""ou and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4 , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits."""

DIGITS    = '0123456789'

def validate(card_no):
    # if hyphen found call Hyphen check and remove hyphen
    if "-" in card_no:
        card_no = hyphenCheck(card_no)
        if card_no == False:
           return False 
    # return false if any of the function returns false.               
    return (checkDigits(card_no) and  
            startCheck(card_no) and 
            repeat(card_no))

# if card no contains a char other than digits or length is not 16 return False 
def checkDigits(card_no):
    dig = 0 
    for i in card_no:       
        if i not in  DIGITS:    
           return False   
        else:
           dig= dig +1   
    if dig != 16:    
        return False

    return True 

# if card no start with 4.5 or 6  return False 
def startCheck(card_no):             
    if int(card_no[0:1]) in range(4,7):        
        return True 
    else:
        return False    

# if hyphen found remove hyphen and if number of digits separeted by hyphen are greater then 4 return False 
def hyphenCheck(card_no):     
   
    card_no_split =card_no.split("-")  
    card_no = card_no.replace("-","")      
    for i in card_no_split:
        if len(i) != 4:
            return False  
    return card_no

# if any consecutive digt repeat more than 3  return False 
def repeat(card_no):
    count = 0 
    for i in range(0,len(card_no)-3):              

       for j in range(i+1,i+4):


           if card_no[i] == card_no[j] :
                count = count + 1     
       if count == 3:                
           return False              
       count = 0
       
    return True


if __name__ == '__main__':
   t = int(input())
   for _ in range(t):
        print('Valid' if validate(input()) else 'Invalid')
        
  











