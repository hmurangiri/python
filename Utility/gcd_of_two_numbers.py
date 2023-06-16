def gcd_of_two_Numbers(a,b):
    if a < b:
        a, b = b , a

    if b == 0:
        return 0
        
    while(b != 0):
        a, b = b, a % b
        return a
