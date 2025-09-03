 # Input a number and count how many digits are even and how many are odd.

number=int(input("Enter Number : "))
odd_count=0
even_count=0
for i in range (1,number+1):
    if(i%2==0):
        even_count+=1
    else:
        odd_count+=1

print("Even Count : ",even_count)
print("Odd Count : ",odd_count)
