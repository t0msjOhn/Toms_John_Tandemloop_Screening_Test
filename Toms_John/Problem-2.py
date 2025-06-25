a = int(input("Enter a number: "))

for i in range(a):
    odd_number = 2*i+1
    
    if i<a-1:
        print(odd_number,end=",")
    else:
        print(odd_number)
