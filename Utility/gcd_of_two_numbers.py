def gcd_of_two_numbers(a,b):
    if a > b:
        pass
    else:
        a, b = b , a

    if b == 0:
        return 0
      
    while True:
        if a % b == 0:
            return b
        else:
            a, b = b, a % b
            
    return gcd
