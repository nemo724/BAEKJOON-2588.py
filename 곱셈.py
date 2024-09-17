a,b=map(int, input().split())
total=0

for i in range (0,3,1):
    output_b=b%10
    output_result=a*output_b
    print(f"{output_result}")
    b=b//10
    total=total+(output_result*(10**i))

print(f"{total}")
