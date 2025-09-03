number=int(input("Enter number : "))
odd_sum=0
even_sum=0

for i in range(1,number+1):
    if(i %2==0):
        even_sum+=i
    else:
        odd_sum+=i

print("Even Sum : ",even_sum)
print("Odd Sum : ",odd_sum)