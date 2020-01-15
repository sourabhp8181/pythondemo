n= input('Enter a number:')
sum=0
j=n

while(j>0):
    fact=1
    i=1
    rem=i%10

    while(i<rem):
        fact=fact*i
        i=i+1
    j=j//10 
    sum = sum+fact

    
if (sum==n):
    print("This is a Strong Number")
else:
    print("This is not a Strong Number")