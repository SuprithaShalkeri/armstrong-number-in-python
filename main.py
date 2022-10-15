
number=int(input("enter the number:"))
result=0
n=0
temp=number;
while(temp!=0):
  temp=int(temp/10)
  n=n+1

temp=number
while(temp!=0):
    remainder=temp%10
    result=result+pow(remainder,n)
    temp=int(temp/10)
if(result==number):
    print("armstrong number")
else:
    print("not an armstrong number")
    