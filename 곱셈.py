a,b=int(input()).split()
total=0

for i in range (1,2,1):
    output_b=b%10
    output_result=a*output_b
    print(f"{output_result}")
    b=b//10
    total=total+output_result

print(f"{total}")
