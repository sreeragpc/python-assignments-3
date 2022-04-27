"""Write a program to print the multiplication table of given numbers.
Accept an input from the user and display its multiplication table
"""

number=int(input("enter a number"))

i=1
while i<11:
    result=i*number
    print(str(i)+"x"+str(number)+"="+str(result))
    i=i+1
