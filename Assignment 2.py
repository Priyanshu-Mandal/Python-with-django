'Q1. Write a program to print all the natural numbers from 1 to n (user input). Then print the same in reverse order.'


a=int(input("Enter the number: "))
for i in range(1,a+1):
    print(i,end=" ")
print()
for i in range(a,0,-1):
    print(i,end=" ")
    
    
    
    
    
'Q2. Print all odd numbers and even numbers between 1 to 100.'


print("Odd numbers: ",end="")
for i in range(1,100,2):
    print(i,end=" ")
print()
print("Even numbers: ",end="")
for i in range(2,101,2):
    print(i,end=" ")
    
    
    


'Q3. Write a program to check if a number is prime or not. Example: 7 ==> True, 6 ==> False'


a=int(input("Enter the number: "))
fact=0
for i in range(1,a+1):
    if(a%i==0):
        fact+=1
if (fact==2):
    print("True")
else:
    print("False")





'''Q4. Write a program that asks the user for a number n and prints the sum of the numbers 1 to n such that only
multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17.'''


a=int(input("Enter the number: "))
z=0
for i in range(1,a+1):
    if(i%3==0 or i%5==0):
        z=z+i
print(z)





''''Q5. Write a program that asks the user for a number n and gives them the possibility to choose between computing the
sum and computing the product of 1,…,n.'''


a=int(input("Enter the number n: "))
b=input("Enter your choice: ")

if (b=="sum" or b=="Sum"):
    z=0
    for i in range(1,a+1):
        z=z+i
    print(z)
elif(b=="product" or b=="Product"):
    z=1
    for i in range(1,a+1):
        z=z*i
    print(z)
else:
    print("Invalid input. Please choose between sum and product")






'Q6. Find the sum of all the multiples of 3 or 5 below 1000.'


z=0
for i in range(1001):
    if(i%3==0 or i%5==0):
        z+=i
print(z)





'''Q7. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between
2000 and 3200 (both included).'''


for i in range(2000, 3201):
    if i%7 == 0 and i%5 != 0:
        print(i, end = " ")
        
        
        
        
        
'''Q8. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the
sum.'''


z=0
a=(sum(range(1,101)))**2

for i in range(1,101):
    z+=i**2
print(z-a)






'Q9. Write a program which can compute the factorial of a given number.'


a=int(input("Enter the number: "))
z=1
while(a!=1):
    z=z*a
    a=a-1
print(z)
    





'''Q10. Pattern:

- >

1

2 2

3 3 3

4 4 4 4

5 5 5 5 5'''


a=int(input("Enter a number: "))
for i in range(1,a+1):
    for j in range(i):
        print(i,end=" ")
    print()






'''->
5 5 5 5 5 
5 4 4 4 5 
5 4 3 4 5 
5 4 4 4 5 
5 5 5 5 5'''


a=int(input("Enter a number: "))
for i in range(a+1):
    for j in range(a+1):
        print(max(i,j,a-i,a-j),end=" ")
    print()






'''->
* 
* * 
* * * 
* * * * 
* * * * * '''


a=int(input("Enter a number: "))
for i in range(a+1):
    for j in range(i):
        print("* ",end="")
    print()






'''->
****
***
**
*'''


a=int(input("Enter a number: "))
for  i in range(a+1,0,-1):
    for j in range(1,i):
        print("*",end=" ")
    print()







'''->
#####
#####
#####
#####
#####'''


a=int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        print("#", end="")
    print()







'''Q11. Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Suppose the
following input is supplied to the program: 9, Then, the output should be: 9 + 99 + 999 + 9999 =  11106.'''


a=input("Enter the number: ")
z=0
for i in range(1,5):
    z+=int(a*i)
print(z)







'Q12. Find the length of a string using loops (not len()).'


a=input("Enter the string: ")
b=0
for _ in a:
    b+=1
print(b)







'''Q13. Write a program that accepts a sentence (string) and calculate the number of letters and digits.
Example: ‘this is a test sentence number 389’ ==> letters = 25 and digits = 3.'''


a=input("Enter the statement: ")
l=0
d=0
for i in a:
    if(i.isdigit()):
        d+=1
    else:
        l+=1
        
print("Number of digits: ",d)
print("Number of letters: ",l)







'''Q14.  Write a program that accepts a string and outputs the string with all capital letters.

      Example: ‘hello’ ==> ‘HELLO’. (using loop)'''
      
      
a=input("Enter the string: ")
b=""
for i in a:
    b+=i.upper()
print(b)








'Q15. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.'


a=input("Enter the statement: ")
l=0
u=0
for i in a:
    if(i.islower()==True):
        l+=1
    elif(i.isupper()==True):
        u+=1
print("Upper: ",u)
print("Lower: ",l)








'''Q16. Write  a program that counts the occurrence of a character in a string. Example: ‘This is a test string.’ count
of i = 3.'''


count=0
a=input("Enter the string: ")
b=input("Enter the charecter: ")
for i in a:
    if(i==b):
        count+=1
print("The charecter occured: ",count," times")







'Q17. Write a program to find if a given string is a palindrome or not.'


a=input("Enter the string: ")
if(a==a[::-1]):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
        






'Q18. Write a program which accepts two strings s1 and s2 and checks if s2 is a substring of s1.'


a=input("Enter the main string: ")
b=input("Enter the smaller string: ")
if b in a:
    print("Substring")
else:
    print("Not a substring")






'''Q19. Make a password validator with the following checks. A website requires the users to input username and password
to register. Write a program to check the validity of password input by users.

    Following are the criteria for checking the password:
1. At least  1 letter between [a-z]     
2. At least 1 number between [0-9]     
3. At least 1 letter between [@$#%&]'''


a=input("Enter the password: ")
l=0
n=0
c=0
for i in a:
    if i.isalpha()==True:
        l=1
    elif i.isdigit()==True:
        n=1
    elif i in "@$#%&":
        c=1

if(l==1 and n==1 and c==1):
    print("Valid password")
else:
    print("Invalid password")








'''Q20. s = "Hello how are you all". For this given string write a code such that it prints the vowels present in the
string s if any. ex: "i", "a" etc.'''


s=input("Enter the string: ")
print("Vowels present are: ",end="")
for i in s:
    if i in "aeiouAEIOU":
        print(i,end=" ")







