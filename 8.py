"""Write a program to find the sum of all the odd numbers for a given limit
Program should accept an input as limit from the user and display the sum of all the odd numbers within that limit
For example if the input limit is 10 then the result is 1+3+5+7+9 = 25
Output: Enter a limit
Input: 10
Output: Sum of odd numbers = 25 """
limit=int(input("enter a limit"))
i=1
sum=0
while i<=limit:
    sum=sum+i
    i=i+2
print("The sum = "+str(sum))