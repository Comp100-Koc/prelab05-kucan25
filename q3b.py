def binary_to_decimal(n):
    n=n[::-1]
    total=0
    for i in range(len(n)-2):
        if n[i]=='1':
            total+=2**i
    return total
def decimal_to_binary(n):
    k=0
    binary=''
    while 2**k<=n:
        k+=1
    k-=1
    while k>=0:
        if 2**k>n:
            binary+='0'
            k-=1
        if 2**k<=n:
            binary+='1'
            n-=2**k
            k-=1      
    return binary
def add_binary(a, b):
    total=binary_to_decimal(a)+binary_to_decimal(b)
    return '0b'+decimal_to_binary(total)
    