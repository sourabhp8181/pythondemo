n= input('Enter a number:')
sum = 0
i=n
temp=n

while(i>0):
    Factorial = 1
    i = 1
    Reminder = Temp % 10

    while(i <= Reminder):
        Factorial = Factorial * i
        i = i + 1

    print("\n Factorial of %d = %d" %(Reminder, Factorial))
    Sum = Sum + Factorial
    Temp = Temp%10

print("\n Sum of Factorials of a Given Number %d = %d" %(Number, Sum))
    
if (sum == n):
    print(" %d is a Strong Number" %Numb)
else:
    print(" %d is not a Strong Number" %Number)