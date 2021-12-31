print("hello world")
print("Hello","world",sep='*',end='#')
print("Test")
print("Test")
def add(a,b):
    return a+b

a= 0
b =2 
list1 = [1,2,3]
if a != 1:
    print ("a is not 1")

for i  in range(0,len(list1)):
    print (list1[i])

while(a<1):
    print (list1[a])
    a=2
print("sum", add(a,b))

list1.append(4)
list1.insert(0,0)


for i in list1:
    print(list1[i])

list1.pop()

print ("after pop")
for i in list1:
    print(list1[i])


str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

if 'H' in str:
    print("h Found")


file_text = raw_input("Enter text: ")
print(file_text)
