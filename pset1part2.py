#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

length = len(s)

counter = 0
for i in range(0,length-1):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        counter = counter + 1
    else:
        pass
               
    
print("Number of times bob occurs is: ",counter)    
    
